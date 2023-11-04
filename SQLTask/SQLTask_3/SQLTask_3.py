import sqlite3

conn = sqlite3.connect('SQLTask_3.db')
cursor = conn.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS transfers (
        from_acc INTEGER,
        to_acc INTEGER,
        amount INTEGER,
        tdate DATA
    )
""")
list_data = [
    (1, 2, 500, '23.02.2023'),
    (2, 3, 300, '01.03.2023'),
    (3, 1, 200, '05.03.2023'),
    (1, 3, 400, '05.04.2023')
]
cursor.executemany("""
    INSERT INTO transfers (from_acc, to_acc, amount, tdate)
    VALUES (?, ?, ?, ?)
""", list_data)


cursor.execute("""
    SELECT t1.from_acc AS acc,
           t1.tdate AS dt_from,
           IFNULL(MIN(t2.tdate), '01.01.3000') AS dt_to,
           SUM(t2.amount) AS balance
    FROM transfers t1
    LEFT JOIN transfers t2
    ON t1.from_acc = t2.from_acc
    AND t1.tdate <= t2.tdate
    GROUP BY t1.from_acc, t1.tdate
    ORDER BY t1.from_acc, t1.tdate
""")

for row in cursor.fetchall():
    print(row)

conn.close()
