INDIC_NLP_LIB_HOME=r"C:\Users\mashh\Documents\git\Plagarism_checker_application\src\NLP\indic_nlp_library"
INDIC_NLP_RESOURCES=r"C:\Users\mashh\Documents\git\Plagarism_checker_application\src\NLP\indic_nlp_resources"

import sys
from NLP.indic_nlp_library.indicnlp import common
from NLP.indic_nlp_library.indicnlp import loader
from NLP.indic_nlp_library.indicnlp.tokenize import sentence_tokenize
   
def get_sentences(text, language):
    """
    Returns a list of sentences in the text. 
    """
    sys.path.append(r'{}'.format(INDIC_NLP_LIB_HOME))
    
    common.set_resources_path(INDIC_NLP_RESOURCES)
    loader.load()
    sentences=sentence_tokenize.sentence_split(indic_string, lang='hi')
    return sentences
    


indic_string="""तो क्या विश्व कप 2019 में मैच का बॉस टॉस है? यानी मैच में हार-जीत में \
टॉस की भूमिका अहम है? आप ऐसा सोच सकते हैं। विश्वकप के अपने-अपने पहले मैच में बुरी तरह हारने वाली एशिया की दो टीमों \
पाकिस्तान और श्रीलंका के कप्तान ने हालांकि अपने हार के पीछे टॉस की दलील तो नहीं दी, लेकिन यह जरूर कहा था कि वह एक अहम टॉस हार गए थे।"""
sentences=sentence_tokenize.sentence_split(indic_string, lang='hi')
for t in sentences:
    print(t)