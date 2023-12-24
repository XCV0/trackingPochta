import sqlite3

connection = sqlite3.connect("db.db")
cursor = connection.cursor()


def check_is_user_exists(tg_id):
    info = cursor.execute('SELECT * FROM users WHERE id_telegram=?', (tg_id,))
    if info.fetchone() is None:
        print("User exists!")
        return True
    else:
        print("User does not exists")
        return False
