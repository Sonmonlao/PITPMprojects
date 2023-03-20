import sqlite3

from sqlite3 import Error


def sql_connection():
    try:

        con = sqlite3.connect('city.db')

        return con

    except Error:

        print(Error)


def sql_table(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE if not exists streets(id integer PRIMARY KEY NOT NULL, name text)")

    con.commit()


def sql_insert(con):
    cursorObj = con.cursor()

    data = [(1, 'Республиканская'), (2, "Гончарная"), (3, "Петина"), (4, "Ленинградская"), (5, "Засимовская")]

    cursorObj.executemany("INSERT INTO streets VALUES(?,?)", data)


def sql_select(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM streets')

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


con = sql_connection()
sql_table(con)
sql_insert(con)
sql_select(con)
con.close()
