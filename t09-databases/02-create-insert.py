import sqlite3
from icecream import ic


people_values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28),
)

# ************************************************** Method #2 **************************************************
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    # cursor.execute("DROP TABLE IF EXISTS People;")

    # # instead of multiple "cursor.execute()" use instead "cursor.executescript()"
    # cursor.executescript("""
    #     CREATE TABLE People(
    #         FirstName TEXT,
    #         LastName TEXT,
    #         Age INT
    #     );
    # """)

    # # passing values from variables, parameterized statement
    # cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)

    # cursor.execute(
    #     "UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;",
    #     (45, "Luigi", "Vercotti"),
    # )

    # independant executions
    # cursor.execute(
    #     """CREATE TABLE People(
    #     FirstName TEXT,
    #     LastName TEXT,
    #     Age INT
    # );
    # """
    # )

    # cursor.execute(
    #     """INSERT INTO People VALUES(
    #         'Ron',
    #         'Obvious',
    #         49
    #     );
    #     """
    # )

    response = cursor.execute("SELECT FirstName, LastName FROM People WHERE Age > 30;")

    for row in response.fetchall():  # returns a Tuple
        print(row)


# ************************************************** Method #1 **************************************************

# connection = sqlite3.connect("test_database.db")
# cursor = connection.cursor()

# cursor.execute(
#     """CREATE TABLE People(
#         FirstName TEXT,
#         LastName TEXT,
#         Age INT
#     );
#     """
# )

# cursor.execute(
#     """INSERT INTO People VALUES(
#         'Ron',
#         'Obvious',
#         42
#     );
#     """
# )

# connection.commit()
# connection.close()

# connection = sqlite3.connect("test_database.db")
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM People;")  # <sqlite3.Cursor object at 0x000001F739DB6650>
# ic(cursor.fetchone())  # ("Ron", "Obvious", 42)
