add_new_user="""
            INSERT INTO Users (username, password) VALUES ('{}', '{}');
            """
get__pw="""
        SELECT password FROM Users WHERE name = '{}';
        """
