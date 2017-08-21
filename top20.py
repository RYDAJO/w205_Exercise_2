import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

#Select wods in top 20 for count
cur.execute("SELECT word, count from tweetwordcount ORDER BY count DESC LIMIT 20")
records = cur.fetchall()
for rec in records:
    print rec[0], ": ", rec[1], "\n"
    conn.commit()

conn.close()
