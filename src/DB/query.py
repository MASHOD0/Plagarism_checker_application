add_new_user="""
            INSERT INTO "Users" (username, password) VALUES ('{}', '{}');
            """
get_pw="""
        SELECT password FROM "Users" WHERE username = '{}';
        """
# get_history="""
#             SELECT "Sentence_history".sentence_id, "Sentence_history".sentence, "History".search_id, "History".time
#                 FROM "History"
#                 JOIN "Sentence_history" ON "History".search_id="Sentence_history".search_id
#                 WHERE id = (SELECT id FROM "Users" WHERE username='{}');
#             """

add_history="""INSERT INTO public."History"( id, "time", language)
                VALUES ((SELECT id from "Users" where username='{}'), TIMESTAMP '{}', '{}');
                """
get_search_id="""SELECT search_id FROM "History" WHERE "time" = '{}' AND id = (select "id" from "Users" where username= '{}');""" 
add_sentence_history="""INSERT INTO public."Sentence_history"( sentence, search_id)
	                VALUES ( '{}', {});"""

get_history="""SELECT "History".search_id, "History".language, "History".time, "Sentence_history".sentence_id, "Sentence_history".sentence
                FROM "History"
                JOIN "Sentence_history" ON "History".search_id = "Sentence_history".search_id
                WHERE "History".id = (SELECT "id" FROM "Users" WHERE username = '{}')"""

get_all_data="""SELECT "Articles".article_id, "Articles".article_link, "Articles".article_metadata, "Article_sentence".sentence_id, "Article_sentence".sentence
                FROM "Articles"
                JOIN "Article_sentence"
                ON "Article_sentence".article_id = "Articles".article_id
                WHERE "Articles".language_id = (SELECT language_id FROM "Languages" WHERE "language" = '{}');
                """

## Library end queries

lang="""SELECT * FROM "Languages";"""
add_lang="""INSERT INTO public."Languages"(language) VALUES ('{}');"""
add_article="""INSERT INTO public."Articles"( language_id, article_link, article_metadata)
	        VALUES ({}, '{}', '{}');"""
add_sentence="""INSERT INTO public."Article_sentence"( article_id, sentence) VALUES ( {}, '{}');"""
get_article_id="""SELECT article_id FROM "Articles" WHERE "article_link"='{}';"""