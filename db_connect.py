import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       # leave blank for XAMPP
        database="cafeteria_db"
    )