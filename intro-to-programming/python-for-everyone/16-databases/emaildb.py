import sqlite3

connection = sqlite3.connect("emaildb.sqlite")
cur = connection.cursor()

cur.execute(
    """
DROP TABLE IF EXISTS Counts"""
)

cur.execute(
    """
CREATE TABLE Counts (email TEXT, count INTEGER)"""
)

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "/home/sunil/OpenSource/Learning/computer-science/\
    intro-to-programming/python-for-everyone/8-files/mbox-short.txt"
fh = open(fname)
for line in fh:
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute("SELECT count FROM Counts WHERE email = ? ", (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute(
            """
        INSERT INTO Counts (email, count)
        VALUES (?, 1)""",
            (email,),
        )
    else:
        cur.execute(
            """
        UPDATE Counts SET count = count + 1 WHERE email = ?""",
            (email,),
        )
    connection.commit()

sqlstr = """SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"""

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
