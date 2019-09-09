import sqlite3


def set_cur(dbName):
    conn = sqlite3.connect(dbName)
    cur = conn.cursor()
    return conn, cur


def close_conn(conn, cur):
    cur.close()
    conn.close()
