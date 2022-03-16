from NLP import nlp
from DB import db, query as q



def input_data(language: str, text: str):
    sentences = nlp.get_sentences(text, language)
    print(len(sentences))
    return sentences


