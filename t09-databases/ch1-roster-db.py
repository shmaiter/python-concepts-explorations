import sqlite3


# 1. Create a new database with a table named Roster that has three
# fields: Name, Species and IQ. The Name and Species columns should
# be text fields, and the IQ column should be an integer field.
# 2. Populate your new table with the following values

character_values = (
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5),
)

with sqlite3.connect("sci_fi.db") as conn:
    cursor = conn.cursor()

    # cursor.execute("DROP TABLE IF EXISTS Roster;")
    # cursor.executescript(
    #     """CREATE TABLE Roster(
    #     Name TEXT,
    #     Species TEXT,
    #     IQ INT
    # );
    # """
    # )

    # cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?)", character_values)

    # 3. Update the Species of Korben Dallas to be Human.
    # cursor.execute(
    #     """
    #     UPDATE Roster
    #     SET Species=?
    #     WHERE Name=?;
    #     """,
    #     ("Human", "Korben Dallas"),
    # )
    
    # 4. Display the names and IQs of everyone in the table classified as Human.
    response = cursor.execute(
        """
        SELECT Name, IQ FROM Roster
        WHERE Species LIKE "Human"
        """
    )
    
    for row in response.fetchall():
        print(row)

# There are many SQL variants and corresponding Python packages
# available. A few of the most commonly used and reliable open-source
# alternatives to SQLite are:
# • pyodbc, which connects to ODBC (Open Database Connection)
#   databases, such as Microsoft SQL Server
# • psycopg2, which connects to the PostgreSQL database
# • PyMySQL, which connects to MySQL databases
