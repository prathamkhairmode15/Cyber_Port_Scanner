import sqlite3

def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS scans(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            osguess TEXT,
            ports TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_scan(target, osguess, ports, date):
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO scans(target,osguess,ports,date) VALUES(?,?,?,?)",
        (target, osguess, ports, date)
    )
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("SELECT * FROM scans ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data
