import sqlite3


def conn_and_set_cur(dbName):
    conn = sqlite3.connect(dbName)
    cur = conn.cursor()
    return conn, cur


def close_conn(conn, cur):
    cur.close()
    conn.close()


user_table_schema = "user_id TEXT NOT NULL PRIMARY KEY, user_name TEXT NOT NULL, join_date BLOB"
expense_table_schema = "exp_id TEXT NOT NULL PRIMARY KEY, amount REAL NOT NULL, desc TEXT NOT NULL, exp_date BLOB NOT NULl, user_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES user (user_id)"


def create_table(db_name, table_name, table_schema):
    conn, cur = conn_and_set_cur(db_name)
    cur.execute('CREATE TABLE IF NOT EXISTS {} ({})'.format(table_name, table_schema))
    close_conn(conn, cur)

if __name__ == "__main__":
    create_table('loaf_1.db', 'user', user_table_schema)
    create_table('loaf_1.db', 'expense', expense_table_schema)


# check table exists:
## SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
