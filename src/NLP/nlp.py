import sys
from indic_nlp_library.indicnlp import common, loader
from indic_nlp_library.indicnlp.tokenize import sentence_tokenize

INDIC_NLP_LIB_HOME=r"C:\Users\mashh\Documents\git\Plagarism_checker_application\src\NLP\indic_nlp_library"
INDIC_NLP_RESOURCES=r"C:\Users\mashh\Documents\git\Plagarism_checker_application\src\NLP\indic_nlp_resources"

def load_nlp():
    sys.path.append(r'{}'.format(INDIC_NLP_LIB_HOME))
    common.set_resources_path(INDIC_NLP_RESOURCES)
    loader.load()







def get_sentences(language, text):
    sentences = sentence_tokenize(text, lang=language)
    return sentences

if __name__ == '__main__':
    load_nlp()
    indic_string="""तो क्या विश्व कप 2019 में मैच का बॉस टॉस है? यानी मैच में हार-जीत में \
टॉस की भूमिका अहम है? आप ऐसा सोच सकते हैं। विश्वकप के अपने-अपने पहले मैच में बुरी तरह हारने वाली एशिया की दो टीमों \
पाकिस्तान और श्रीलंका के कप्तान ने हालांकि अपने हार के पीछे टॉस की दलील तो नहीं दी, लेकिन यह जरूर कहा था कि वह एक अहम टॉस हार गए थे।"""
    sentences = get_sentences('hi', indic_string)
    for sentence in sentences:
        print(sentence)