## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

conn = psycopg2.connect('dbname=dq user=dq')
curr = conn.cursor()
query = '''
    create table notes(
        id integer PRIMARY KEY,
        body text,
        title text
    );
'''
curr.execute(query)
conn.close()

## 5. SQL Transactions ##

conn = psycopg2.connect('dbname=dq user=dq')
curr = conn.cursor()
query = '''
    create table notes(
        id integer PRIMARY KEY,
        body text,
        title text
    );
'''
curr.execute(query)
conn.commit()
conn.close()

## 6. Autocommitting ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
curr = conn.cursor()
query = '''
    create table facts(
        id integer PRIMARY KEY,
        country text,
        value integer
    );
'''
curr.execute(query)
conn.close()

## 7. Executing queries ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('truncate table notes')
query = "insert into notes values (1, 'Do more missions on Dataquest.', 'Dataquest reminder');"
cur.execute(query)
cur.execute("SELECT * FROM notes;")
rows = cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('create database income owner dq')
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('drop database income')
conn.close()