from DB import db, query as q

def create_history(conn, username, timestamp, sentences, language):
    print(f"username:{username}")
    print(f"timestamp:{timestamp}")
    print(f"sentences:{sentences}")
    print(f"language:{language}")
    db.execute(conn, q.add_history.format(username, timestamp, language))
    search_id=db.fetch(conn, q.get_search_id.format(timestamp, username))[0][0]
    for sentence in sentences:
        print(sentence)
        db.execute(conn, q.add_sentence_history.format(sentence, search_id))


def get_history(conn, username):
    history_articles = []
    history = db.fetch(conn, q.get_history.format(username))
    return history