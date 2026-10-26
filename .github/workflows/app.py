import sqlite3

def get_user_data(user_id):
    # DANGEROUS: String formatting inside SQL query (SQL Injection!)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchone()

# DANGEROUS: Hardcoded cloud secret!
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
