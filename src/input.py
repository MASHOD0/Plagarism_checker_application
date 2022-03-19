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
    # article link: https://www.amarujala.com/india-news/after-assembly-poll-victories-bjp-gets-down-to-analysing-results-with-an-eye-on-2024-lok-sabha-election?src=tlh&position=1
    text = "जिन चार राज्यों में भाजपा ने जीत हासिल की है, उनके वरिष्ठ नेता राष्ट्रीय राजधानी में गृह मंत्री अमित शाह और पार्टी प्रमुख जेपी नड्डा और पार्टी महासचिव (संगठन) बीएल संतोष सहित पार्टी के केंद्रीय नेताओं के साथ चर्चा कर रहे हैं। गोवा, उत्तराखंड और मणिपुर में पार्टी के मुख्यमंत्रियों की पसंद को लेकर अटकलें लगाई जा रही हैं। सूत्रों ने एएनआई को बताया कि सरकार गठन के अलावा पार्टी की जीत और हार और इसके कारणों और कारकों के बारे में चुनाव परिणामों का विश्लेषण भी कर रही है। "
    sentences = input_data('hi', text)
    metadata="first string through the script"
    link="https://www.amarujala.com"
    add_to_db(conn, 'hi', link, metadata, sentences)