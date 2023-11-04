import sqlite3
from datetime import datetime, timedelta

with sqlite3.connect('SQLTask_1.db') as db:
    cursor = db.cursor()

    query = """ CREATE TABLE IF NOT EXISTS expenses (data TEXT) """

    cursor.execute(query)

    current_date = datetime.now()
    for _ in range(100):
        cursor.execute("INSERT INTO expenses (data) VALUES (?)", (current_date.strftime("%Y-%m-%d"),))
        current_date += timedelta(days=2, seconds=0)

    db.commit()
