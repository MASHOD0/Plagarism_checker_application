from DB import db, query as q

def create_history(conn, username, timestamp, sentences):
    db.execute(conn, q.add_history.format(username, timestamp))
    search_id=db.fetch(conn, q.get_search_id.format(username, timestamp))[0]
    for sentence in sentences:
        db.execute(conn, q.add_sentence_history.format(search_id, sentence))