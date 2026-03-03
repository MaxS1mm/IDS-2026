from .db_utils import get_connection
import sqlite3

def usernameExists() -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    user = cursor.fetchone()

    if user == None:
        exists = False
    else:
        exists = True

    conn.commit()
    conn.close()
    return exists

def createUser(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))

    conn.commit()
    conn.close()

def readUsername() -> str:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    user = cursor.fetchone()

    if user == None:
        username = ""
    else:
        username = user[0]

    conn.commit()
    conn.close()

    return username

def readRules():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM rules")
    rules = cursor.fetchall()

    if not rules:
        rules = ""

    conn.commit()
    conn.close()

    return rules

def createRule(protocol: str, srcIP: str, destIP: str, srcP: int, destP: int, action: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO rules (protocol, src_ip, dst_ip, src_port, dst_port, action) VALUES (?,?,?,?,?,?)", (protocol, srcIP, destIP, srcP, destP, action))

    conn.commit()
    conn.close()



# def updateRule():
#     # TODO
# def deleteRule():
#     # TODO



