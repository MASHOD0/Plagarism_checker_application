# Plagarism_checker_application
This is an application designed to check for plaigarism between text by matching it against a database of articles from the [National digital library](https://ndl.iitkgp.in).
the plagarism checker has 4 modules
![image](https://user-images.githubusercontent.com/63853764/159468592-3d1f4498-572b-4b11-90f5-d76a6c675953.png)
## Database Schema
```mermaid
 erDiagram 
Users{
    id int
    username varchar
}

History{
  search_id int 
  id int
  time timestamp
}
Sentence_history{
  sentence_id int 
  sentence varchar
  search_id int
}
```
```mermaid
erDiagram
Languages{
  language_id int 
  language varchar
}


Articles{
  article_id int 
  language_id int
  article_link varchar
  article_metadata varchar
}
Article_tags{
  article_id int
  tag_id int
}
Tags{
  tag_id int 
  tag varchar
}
Article_sentence{
  sentence_id int 
  article_id int
  sentence varchar
}
```
## Instructions to run the application on your local system
### Requirements
- Python `ver 3.7.1` or newer
- Postgres `ver 13.4` or newer
### Database:
- Create a postgresql database with name `Sih-ver1` 
- [Run this script to add the Schema](https://github.com/MASHOD0/Plagarism_checker_application/blob/main/src/DB/sql/create.sql)
- update the user credentials in `src/DB/db.py`
- If the credentials are not updated 
    - by default the user is `postgres`
    - by default the password is `postgres`
### Python package requirements:
- All the required python packages can be installed by using pip to install the requirements in [requirements.txt](https://github.com/MASHOD0/Plagarism_checker_application/blob/main/src/requirements.txt)
- Run this command:
```bash
pip install -r requirements.txt
```
### Running the application:
Run this command to start the server and run the application
```bash
python src/main.py
```
this will run the program on `localhost:5000`
## File Structure
```
π¦src
 β£ π.ipynb_checkpoints
 β£ πDB
 β β£ πsql
 β β β πcreate.sql
 β β£ π__pycache__
 β β β£ πdb.cpython-39.pyc
 β β β πquery.cpython-39.pyc
 β β£ πdb.py
 β β πquery.py
 β£ πdemo.py
 β£ πhistory.py
 β£ πinput.py
 β£ πmain.py
 β£ πreport.py
 β£ πtest.py
 β£ πNLP
 β β£ π.ipynb_checkpoints
 β β β πindic_nlp_examples-checkpoint.ipynb
 β β£ πindic_nlp_library
 β β β£ πcontrib
 β β β β£ πcorrect_moses_tokenizer.py
 β β β β£ πhindi_to_kannada_transliterator.py
 β β β β£ πindic_scraper_project_sample.ipynb
 β β β β πREADME.md
 β β β£ πdocs
 β β β β£ πcmd.rst
 β β β β£ πcode.rst
 β β β β£ πconf.py
 β β β β£ πindex.rst
 β β β β£ πindicnlp.cli.rst
 β β β β£ πindicnlp.MD
 β β β β£ πindicnlp.morph.rst
 β β β β£ πindicnlp.normalize.rst
 β β β β£ πindicnlp.pdf
 β β β β£ πindicnlp.rst
 β β β β£ πindicnlp.script.rst
 β β β β£ πindicnlp.syllable.rst
 β β β β£ πindicnlp.tokenize.rst
 β β β β£ πindicnlp.transliterate.rst
 β β β β£ πmake.bat
 β β β β£ πMakefile
 β β β β πmodules.rst
 β β β£ πindicnlp
 β β β β£ πcli
 β β β β β£ πcliparser.py
 β β β β β π__init__.py
 β β β β£ πmorph
 β β β β β£ π__pycache__
 β β β β β β£ πunsupervised_morph.cpython-39.pyc
 β β β β β β π__init__.cpython-39.pyc
 β β β β β£ πunsupervised_morph.py
 β β β β β π__init__.py
 β β β β£ πnormalize
 β β β β β£ π__pycache__
 β β β β β β£ πindic_normalize.cpython-39.pyc
 β β β β β β π__init__.cpython-39.pyc
 β β β β β£ πindic_normalize.py
 β β β β β π__init__.py
 β β β β£ πscript
 β β β β β£ π__pycache__
 β β β β β β£ πenglish_script.cpython-39.pyc
 β β β β β β£ πindic_scripts.cpython-39.pyc
 β β β β β β£ πphonetic_sim.cpython-39.pyc
 β β β β β β π__init__.cpython-39.pyc
 β β β β β£ πenglish_script.py
 β β β β β£ πindic_scripts.py
 β β β β β£ πphonetic_sim.py
 β β β β β π__init__.py
 β β β β£ πsyllable
 β β β β β£ π__pycache__
 β β β β β β£ πsyllabifier.cpython-39.pyc
 β β β β β β π__init__.cpython-39.pyc
 β β β β β£ πsyllabifier.py
 β β β β β π__init__.py
 β β β β£ πtest
 β β β β β£ πunit
 β β β β β β π__init__.py
 β β β β β π__init__.py
 β β β β£ πtokenize
 β β β β β£ π__pycache__
 β β β β β β£ πindic_detokenize.cpython-39.pyc
 β β β β β β£ πindic_tokenize.cpython-39.pyc
 β β β β β β£ πsentence_tokenize.cpython-39.pyc
 β β β β β β π__init__.cpython-39.pyc
 β β β β β£ πindic_detokenize.py
 β β β β β£ πindic_tokenize.py
 β β β β β£ πsentence_tokenize.py
 β β β β β π__init__.py
 β β β β£ πtransliterate
 β β β β β£ π__pycache__
 β β β β β β£ πsinhala_transliterator.cpython-39.pyc
 β β β β β β£ πunicode_transliterate.cpython-39.pyc
 β β β β β β π__init__.cpython-39.pyc
 β β β β β£ πacronym_transliterator.py
 β β β β β£ πscript_unifier.py
 β β β β β£ πsinhala_transliterator.py
 β β β β β£ πunicode_transliterate.py
 β β β β β π__init__.py
 β β β β£ π__pycache__
 β β β β β£ πcommon.cpython-39.pyc
 β β β β β£ πlanginfo.cpython-39.pyc
 β β β β β£ πloader.cpython-39.pyc
 β β β β β π__init__.cpython-39.pyc
 β β β β£ πcommon.py
 β β β β£ πlanginfo.py
 β β β β£ πloader.py
 β β β β£ πversion.txt
 β β β β π__init__.py
 β β β£ πtest_data
 β β β β£ πmorph
 β β β β β πmr.txt
 β β β β£ πnormalize
 β β β β β£ πbn.txt
 β β β β β£ πen.txt
 β β β β β£ πgu.txt
 β β β β β£ πhi.txt
 β β β β β£ πkK.txt
 β β β β β£ πma.txt
 β β β β β£ πmr.txt
 β β β β β£ πpa.txt
 β β β β β£ πta.txt
 β β β β β£ πte.txt
 β β β β β πur.txt
 β β β β£ πtokenize
 β β β β β πtrivial.txt
 β β β β πtransliterate.ipynb
 β β β£ πLICENSE
 β β β£ πREADME.md
 β β β£ πrequirements.txt
 β β β πsetup.py
 β β£ πindic_nlp_resources
 β β β£ πmorph
 β β β β πmorfessor
 β β β β β£ πbn.model
 β β β β β£ πgu.model
 β β β β β£ πhi.model
 β β β β β£ πkK.model
 β β β β β£ πkn.model
 β β β β β£ πml.model
 β β β β β£ πmr.model
 β β β β β£ πpa.model
 β β β β β£ πsa.model
 β β β β β£ πta.model
 β β β β β£ πte.model
 β β β β β πur.model
 β β β£ πscript
 β β β β£ πall_script_phonetic_data.csv
 β β β β£ πall_script_phonetic_data.xlsx
 β β β β£ πarpabet.pdf
 β β β β£ πenglish_arpabet_list.csv
 β β β β£ πenglish_script_phonetic_data.csv
 β β β β£ πenglish_script_phonetic_data.xlsx
 β β β β£ πtamil_script_phonetic_data.csv
 β β β β πtamil_script_phonetic_data.xlsx
 β β β£ πtransliterate
 β β β β£ πbn-hi.zip
 β β β β£ πen-hi.zip
 β β β β£ πmr-hi.zip
 β β β β£ πoffset_itrans_map.csv
 β β β β£ πREADME.md
 β β β β£ πta-hi.zip
 β β β β πte-hi.zip
 β β β πREADME.md
 β β£ π__pycache__
 β β β πnlp.cpython-39.pyc
 β β£ πindic_nlp_examples.ipynb
 β β πnlp.py
 β£ πstatic
 β β πstyle.css
 β£ πtemplates
 β β£ πhistory.html
 β β£ πhome.html
 β β£ πindex.html
 β β£ πlogin.html
 β β£ πmain.html
 β β£ πregister.html
 β β£ πresults.html
 β β π__init__.py
 β£ π__pycache__
 β β£ πdemo.cpython-39.pyc
 β β£ πhistory.cpython-39.pyc
 β β πreport.cpython-39.pyc
 β πtest1.py
 ```
## Contributors
- [Mashhood Alam](https://github.com/MASHOD0) (Team Lead)
- [Rida Ishtiyaq](https://github.com/rida228/)
- [Rohan KV](https://github.com/rohankatta/)
