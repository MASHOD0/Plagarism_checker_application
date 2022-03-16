add_new_user="""
            INSERT INTO "Users" (username, password) VALUES ('{}', '{}');
            """
get_pw="""
        SELECT password FROM "Users" WHERE username = '{}';
        """
get_history="""
            SELECT "Sentence_history".sentence_id, "Sentence_history".sentence, "History".search_id, "History".time
                FROM "History"
                JOIN "Sentence_history" ON "History".search_id="Sentence_history".search_id
                WHERE id = (SELECT id FROM "Users" WHERE username='{}');
            """
get_all_data="""
                SELECT Articles.article_id, Articles.link, Articles.metadata, Article_sentence.sentence_id, Article_sentence.sentence
                FROM Articles
                JOIN Article_sentence ON Articles.article_id=Article_sentence.article_id
                WHERE Articles.language = (SELECT language_id FROM Languages WHERE language = '{}');
                """
