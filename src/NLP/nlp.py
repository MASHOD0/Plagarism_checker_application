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
    sentences=sentence_tokenize.sentence_split(text, lang=language)
    return sentences
    