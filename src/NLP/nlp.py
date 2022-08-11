import sys
import os
cwd = os.getcwd()
INDIC_NLP_LIB_HOME=os.path.join(cwd, "src", "NLP", "indic_nlp_library")
INDIC_NLP_RESOURCES=os.path.join(cwd, "src","NLP", "indic_nlp_resources") 

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
    # x
    return sentences
    
