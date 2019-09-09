import random
from sql_conn import set_cur

# TODO: set up function to create new account numbers when neccessary
# # check them against all in-use acct nums
# # save a batch(100? 1000?) to pull from 

accts_100 = random.sample(range(100000000, 999999999), 100)
print(accts_100)

conn, cur = set_cur("loaf_0.db")

# for acct in accts_100:
#     cur.execute("INSERT INTO acct_nums (acct_num, active) VALUES      (?, ?)", (acct, 0))
#     conn.commit()

cur.execute("SELECT * FROM acct_nums")
x = cur.fetchall()
print(x)