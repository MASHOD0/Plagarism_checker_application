from DB import db, query as q

def create_history(conn, username, timestamp, sentences, language):
    db.execute(conn, q.add_history.format(username, timestamp, language))
    search_id=db.fetch(conn, q.get_search_id.format(timestamp, username))[0][0]
    for sentence in sentences:
        db.execute(conn, q.add_sentence_history.format(sentence, search_id))


def get_history(conn, username):
    history = db.fetch(conn, q.get_history.format(username))
    return history