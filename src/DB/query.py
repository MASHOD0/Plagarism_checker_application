add_new_user="""
            INSERT INTO Users (username, password) VALUES ('{}', '{}');
            """
get__pw="""
        SELECT password FROM Users WHERE name = '{}';
        """
get_history="""
            SELECT Sentence_history.sentence_id, Sentence_history.sentence, History.search_id, History.time
            FROM History
            JOIN Sentence_history ON History.search_id=Sentence.search_id
            WHERE username = '{}';
            """