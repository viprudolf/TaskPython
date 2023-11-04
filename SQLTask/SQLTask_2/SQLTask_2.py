import sqlite3

with sqlite3.connect('SQLTask_2.db') as db:
    cursor = db.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    table_employee = """ CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, name VARCHAR) """
    cursor.execute(table_employee)

    employee_data = [
        (1, 'Мария'),
        (2, 'Алексей'),
        (3, 'Никита')
    ]

    cursor.executemany("INSERT INTO employee (id, name) VALUES (?, ?)", employee_data)

    table_sales = """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            price INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employee(id)
        )
        """
    cursor.execute(table_sales)

    sales_data = [
        (1, 1, 100),  # Продажи Марии
        (2, 1, 200),  # Продажи Марии
        (3, 2, 150),  # Продажи Алексея
        (4, 3, 300),  # Продажи Никиты
        (5, 2, 50)  # Продажи Алексея
    ]

    cursor.executemany("INSERT INTO sales (id, employee_id, price) VALUES (?, ?, ?)", sales_data)

    cursor.execute('''
        CREATE TEMP VIEW IF NOT EXISTS SalesSummary AS
        SELECT
            e.id,
            e.name,
            COUNT(s.id) AS sales_c,
            SUM(s.price) AS sales_s
        FROM employee e
        LEFT JOIN sales s ON e.id = s.employee_id
        GROUP BY e.id, e.name
    ''')

    cursor.execute('''
        SELECT
            ss.id,
            ss.name,
            ss.sales_c,
            RANK() OVER (ORDER BY ss.sales_c DESC) AS sales_rank_c,
            ss.sales_s,
            RANK() OVER (ORDER BY ss.sales_s DESC) AS sales_rank_s
        FROM SalesSummary ss
    ''')

    result = cursor.fetchall()

    for row in result:
        print(row)

    db.commit()
