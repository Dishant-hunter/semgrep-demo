import sqlite3
import hashlib
import requests

# 1. SQL Injection (OWASP A03: Injection)
# Passing raw formatted user input directly into an SQL execution
def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchone()

# 2. Remote Code Execution (RCE)
# Using python's eval() on dynamic user input lets an attacker run shell commands
def calculate_discount(user_input):
    return eval(user_input)

# 3. Weak Cryptographic Password Hashing (OWASP A02: Broken Crypto)
# Using MD5 for passwords can be cracked in seconds via rainbow tables
def hash_user_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# 4. Disabling SSL Certificate Verification (OWASP A07: Insecure Communication)
# Setting verify=False allows Man-In-The-Middle (MITM) attackers to intercept traffic
def download_profile_pic(avatar_url):
    return requests.get(avatar_url, verify=False)
