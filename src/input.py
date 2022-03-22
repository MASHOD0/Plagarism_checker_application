from NLP import nlp
from DB import db, query as q
import demo


def input_data(language: str, text: str):
    sentences = nlp.get_sentences(text, language)
    # print(len(sentences))
    return sentences

def add_to_db(conn, language, link, metadata, sentences):
    lang = db.fetch(conn, q.lang)
    for i in lang:
        if i[1] == language:
            language_id = i[0]
        

    db.execute(conn, q.add_article.format(language_id, link, metadata))
    article_id = db.fetch(conn, q.get_article_id.format(link))[0][0]
    for sentence in sentences:
        #print(sentence)
        db.execute(conn, q.add_sentence.format(article_id, sentence))
    print("Added to DB")
    

if __name__ == "__main__":
    conn = db.SihDB_Connect()
    article1 = demo.article1
    link1 = demo.link1
    metadata1 = demo.metadata1
    language1 = demo.language1
    sentences1 = input_data(language1, article1)
    add_to_db(conn, language1, link1, metadata1, sentences1)
    article2 = demo.article2
    link2 = demo.link2
    metadata2 = demo.metadata2
    language2 = demo.language2
    sentences2 = input_data(language2, article2)

    add_to_db(conn, language2, link2, metadata2, sentences2)
    db.close(conn)
    # print("Added to DB")
    # # article link: https://www.amarujala.com/india-news/after-assembly-poll-victories-bjp-gets-down-to-analysing-results-with-an-eye-on-2024-lok-sabha-election?src=tlh&position=1
    
    # sentences = input_data('hi', text)
    # metadata="first string through the script"
    # link="https://www.amarujala.com"
    # add_to_db(conn, 'hi', link, metadata, sentences)