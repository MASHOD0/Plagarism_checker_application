from DB import db, query as q
from NLP import nlp
import difflib

conn = db.SihDB_Connect()


def fetch_data(conn, language: str):
    """
    Fetches data from the database and returns it as a list of tuples.
    :param conn: Database connection
    :param language: Language of the data
    :return: List of tuples
    """
    data = db.fetch(conn, q.get_all_data.format(language))
    return data


def generate_report(sentences: list, language: str):
    """
    Generates a report for the given sentences using Sequence Matcher.
    data format: article_id, link, metadata, sentence_id, sentence
    :param sentences: list of sentences
    :param language: language of the sentences
    :return: report
    """
    data = fetch_data(conn, language)
    
    p_links = []
    score = 0.0
    highest_score = 0.0
    p_articles = []
    label = []
    temp_article_sentence = []
    p_metadata = []

    for sentence in sentences:
        for i in data:
            plagarism = difflib.SequenceMatcher(None, i[-1], sentence).ratio()
            if plagarism > highest_score:
                highest_score = plagarism
                temp_article_sentence = i

        if highest_score > 0.75 and highest_score <= 0.85:
            p_articles.append(temp_article_sentence)
            label.append("Related Meaning")
            score += highest_score
        elif highest_score > 0.85 and highest_score <= 0.95:
            p_articles.append(temp_article_sentence)
            label.append("Minor changes")
            score += highest_score
        elif highest_score > 0.95:
            p_articles.append(temp_article_sentence)
            label.append("Identical")
            score += highest_score
        else :
            label.append("Not Related")
            score += highest_score

    if len(sentences) != 0:
        score = (score/len(sentences))*100

    for article in p_articles:
        if article[1] not in p_links:
            p_links.append(article[1])
            p_metadata.append(article[2])
        
    return label, p_links, score, p_metadata