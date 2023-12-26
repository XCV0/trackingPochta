import sqlite3

connection = sqlite3.connect("db.db")
cursor = connection.cursor()


def check_is_user_exists(tg_id):
    info = cursor.execute('SELECT * FROM users WHERE tg_id=?', (tg_id,))
    if info.fetchone() is None:
        print("User does not exists!")
        cursor.execute('INSERT INTO users VALUES(?)', (tg_id,))
        connection.commit()
        return False
    else:
        print("User exists!")
        return True


def add_schedule_check(tg_id, track_number, name):
    cursor.execute('INSERT INTO parcels_for_tracking VALUES(?,?,?)', (tg_id, track_number, name,))
    connection.commit()


def get_all_parcels():
    data = cursor.execute('SELECT track FROM parcels_for_tracking').fetchall()
    return data


def get_last_package_date(package):
    return cursor.execute('SELECT last_time_status FROM parcels_for_tracking WHERE track=?', (package,)).fetchone()


def get_tg_id(package):
    return cursor.execute('SELECT tg_id FROM parcels_from_tracking WHERE track=?', (package,)).fetchone()


def get_name_package(package):
    return cursor.execute('SELECT name FROM parcels_from_tracking WHERE track=?', (package,)).fetchone()
