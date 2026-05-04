import mysql.connector
import os
import sys
from dotenv import load_dotenv

# Import password
load_dotenv()
my_password = os.getenv("DB_PASSWORD")
my_database = "researchlabmanager"

table_titles = ["GRANT",
                "PROJECT",
                "WORKS",
                "LAB_MEMBER",
                "STUDENT",
                "COLLABORATOR",
                "FACULTY",
                "USES",
                "DEVICE",
                "EQUIPMENT",
                "PUBLISHES",
                "PUBLICATION"]
"""(lab members, students, collaborator, faculty
     , projects,
    equipment, device
 grant
 publication
 publishes)*/"""

# Connect to the Database with relevant info
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=my_password,
        database=my_database
    )

def choice_wip():
    print("\nSorry, this feature is a Work In Progress.")

# Test function to view all Lab Members
def query_db(query):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query);

        for row in cursor.fetchall():
            print(row)

        conn.close()
    except Exception as e:
        print("Error:", e)

# Test function to view all Lab Members
def insert_db(query):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query);

        for row in cursor.fetchall():
            print(row)

        db.commit()
        print(cursor.rowcount, "record inserted.")

        conn.close()
    except Exception as e:
        print("Error:", e)

def query_table_format(query):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query);

        query_result = [item[0] for item in cursor.fetchall()]

        conn.close()
        return query_result

        conn.close()
    except Exception as e:
        print("Error:", e)

# WIP
def create_test():
    tables = ['Student', 'Faculty', 'Collaborator']
    query_result = [None] * len(tables)
    for i in range(len(tables)):
        query_result[i] = query_table_format(
            """SELECT COLUMN_NAME
               FROM (SELECT COLUMN_NAME,
                            MIN(CASE WHEN TABLE_NAME = 'lab_member' THEN 1 ELSE 2 END) AS table_priority,
                            MIN(ORDINAL_POSITION)                                      AS position_priority
                     FROM INFORMATION_SCHEMA.COLUMNS
                     WHERE TABLE_NAME IN ('lab_member', '""" + tables[i] + """')
                     GROUP BY COLUMN_NAME) AS C
               ORDER BY table_priority, position_priority;
            """
        )

    while True:
        print("Following the format to create a student, faculty, or collaborator entry:")
        for i in range(len(query_result)):
            print(tables[i], end=": ")
            print("(" + query_result[i][0], end="")
            for j in query_result[i][1:]:
                print(", " + j, end="")
            print(")")
        print("Or type EXIT to exit.")

        choice = input("Enter: ")
        choice_split = choice.split(", ")
        if choice == "EXIT":
            sys.exit()
        elif choice_split[3] == "\"Student\"":
            print("working")
            lab_member_values= choice_split[0]
            for i in range(6):
                lab_member_values += ", " +choice_split[i+1]
            lab_member_values += ")"
            student_values=choice_split[0]
            for i in range(3):
                student_values += ", " +choice_split[i+7]

            query = "INSERT INTO lab_member VALUES" + lab_member_values + ";"
            print(query)
            query_db(query)
            query = "INSERT INTO student VALUES" + student_values + ";"
            print(query)
            query_db(query)



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
        elif choice == "test":
            create_test()
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
            choice_wip()
        elif choice == "2":
            choice_wip()
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
            choice_wip()
        elif choice == "2":
            choice_wip()
        elif choice == "EXIT":
            sys.exit()

main_menu()