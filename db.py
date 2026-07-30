import sqlite3

DB_NAME = "laptops.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS laptops(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ebay_item_id TEXT UNIQUE,
        brand TEXT,
        model TEXT,
        price REAL
    )
    """
    )

    conn.commit()
    conn.close()


def is_db_empty():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM laptops")

    count = cursor.fetchone()[0]

    conn.close()

    return count == 0


def insert_laptops(laptops):

    conn = get_connection()

    cursor = conn.cursor()

    for laptop in laptops:

        cursor.execute(
            """
        INSERT OR IGNORE INTO laptops(
            ebay_item_id,
            brand,
            model,
            price
        )
        VALUES(?,?,?,?)
        """,
            (laptop["item_id"], laptop["brand"], laptop["model"], laptop["price"]),
        )

    conn.commit()
    conn.close()


def search_by_budget(max_price):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT brand,model,price
        FROM laptops
        WHERE price<=?
        ORDER BY price
    """,
        (max_price,),
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
