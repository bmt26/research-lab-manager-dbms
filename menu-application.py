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

def choice_wip():
    print("\nSorry, this feature is a Work In Progress.")

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
        print("\n--- Research Lab Manager DBMS")
        print("1. Project and Member Management")
        print("2. Equipment Usage Tracking")
        print("3. Grant and Publication Reporting")
        print("Or type EXIT to exit.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "1":
            project_member_management()
        elif choice == "2":
            equipment_usage_tracking()
        elif choice == "3":
            grant_publication_reporting()
        elif choice == "EXIT":
            sys.exit()

# Project and Member Management sub menu
def project_member_management():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Project and Member Management")
        print("0. Back")
        print("1. Create/Read/Update/Delete Members or Projects")
        print("2. Display the status of a project")
        print("3. Show members who have worked on project funded by a given grant")
        print("4. Show mentorship relations among members who have worked on the same project")
        print("Or type EXIT to exit.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            break
        elif choice == "1":
            crud_member_projects()
        elif choice == "2":
            choice_wip()
        elif choice == "2":
            choice_wip()
        elif choice == "3":
            choice_wip()
        elif choice == "4":
            choice_wip()
        elif choice == "EXIT":
            sys.exit()

# Project and Member Management sub menu
def crud_member_projects():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Project and Member Management")
        print("    --- CRUD Members/Projects")
        print("0. Back")
        print("CM. Create Member")
        print("RM. Read Member")
        print("UM. Update Member")
        print("DM. Delete Member")
        print("CP. Create Project")
        print("RP. Read Project")
        print("UP. Update Project")
        print("DP. Delete Project")
        print("Or type EXIT to exit.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            break
        elif choice == "CM":
            choice_wip()
        elif choice == "RM":
            choice_wip()
        elif choice == "UM":
            choice_wip()
        elif choice == "DM":
            choice_wip()
        elif choice == "CP":
            choice_wip()
        elif choice == "RP":
            choice_wip()
        elif choice == "UP":
            choice_wip()
        elif choice == "DP":
            choice_wip()
        elif choice == "EXIT":
            sys.exit()

# Equipment Usage Tracking sub menu
def equipment_usage_tracking():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Equipment Usage Tracking")
        print("0. Back")
        print("1. Option 1")
        print("2. Option 2")
        print("Or type EXIT to exit.")

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

# Grant and Publication Reporting sub menu
def grant_publication_reporting():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Grant and Publication Reporting")
        print("0. Back")
        print("1. Option 1")
        print("2. Option 2")
        print("Or type EXIT to exit.")

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