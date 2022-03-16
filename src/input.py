from NLP import nlp
from DB import db, query as q



def input_data(language: str, text: str):
    sentences = nlp.get_sentences(text, language)
    print(len(sentences))
    return sentences

def add_to_db(conn, language, link, metadata, sentences):
    lang = db.fetch(conn, q.lang)
    for i in lang:
        if i[1] == language:
            language_id = i[0]
        

    db.execute(conn, q.add_article.format(language_id, link, metadata))
    article_id = db.fetch(conn, q.get_article_id.format(link))[0][0]
    for sentence in sentences:
        print(sentence)
        db.execute(conn, q.add_sentence.format(article_id, sentence))
    print("Added to DB")
    

