from DB import db, query as q
from NLP import nlp
import difflib

conn = db.SihDB_Connect()

def fetch_data(conn, language: str):
    data = db.fetch(conn, q.get_all_data.format(language))
    return data


def generate_report(sentences: list, language: str):
    data = fetch_data(conn, language)
    # data format: article_id, link, metadata, sentence_id, sentence
    # p_words = 0
    p_links = []
    score = 0.0
    highest_score = 0.0
    p_articles = []
    lable = []
    temp_article_sentence = []
    for sentence in sentences:
        for i in data:
            plagarism = difflib.SequenceMatcher(None, sentence, i[-1]).ratio()
            if plagarism > highest_score:
                highest_score = plagarism
                temp_article_sentence = i
        if highest_score > 0.75 and highest_score <= 0.85:
            p_articles.append(temp_article_sentence)
            lable.append("Related Meaning")
            score += highest_score
           
        elif highest_score > 0.85 and highest_score <= 0.95:
            p_articles.append(temp_article_sentence)
            lable.append("Minor changes")
            score += highest_score
        elif highest_score > 0.95:
            p_articles.append(temp_article_sentence)
            lable.append("Plagarism")
            score += highest_score
        else :
            lable.append("Not Related")
            score += highest_score
                
    score = (score/len(sentences))*100
    for article in p_articles:
        if article[1] not in p_articles:
            p_links.append(article)
        
    return lable, p_links, score