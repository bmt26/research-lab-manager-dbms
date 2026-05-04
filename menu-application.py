import mysql.connector
import os
import sys
from dotenv import load_dotenv

# Import password
load_dotenv()
my_password = os.getenv("DB_PASSWORD")

# Connect to the Database with relevant info
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=my_password,
        database="researchlabmanager"
    )

# Test function to view all Lab Members
def view_members():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LAB_MEMBER");

        for row in cursor.fetchall():
            print(row)

        conn.close()
    except Exception as e:
        print("Error, could not connect to database:", e)

# Text Menu
def main_menu():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS ---")
        print("1. Print Lab Members")
        print("2. Sub Menu")
        print("Or type EXIT to exit.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "1":
            view_members()
        elif choice == "2":
            other_menu()
        elif choice == "EXIT":
            sys.exit()

# Example Function for sub menus
def other_menu():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Sub Menu ---")
        print("0. Back")
        print("1. Option 1")
        print("2. Option 2")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            break
        elif choice == "1":
            view_members()
        elif choice == "2":
            other_menu()
        elif choice == "EXIT":
            sys.exit()

main_menu()