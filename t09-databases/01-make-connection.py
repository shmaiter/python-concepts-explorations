import sqlite3
from icecream import ic


# ************************************************** Method #2 **************************************************


with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    response = cursor.execute(query)
    datetime = response.fetchone()[0]

    ic(datetime)


# ************************************************** Method #1 **************************************************
# connection = sqlite3.connect("test_database.db")
# cursor = connection.cursor()

# query = "SELECT datetime('now', 'localtime');"
# response = cursor.execute(query)
# datetime = response.fetchone()[0]

# ic(datetime)

# connection.close()
