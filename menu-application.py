import mysql.connector
import os
import sys
import re
from dotenv import load_dotenv

# Import password
load_dotenv()
MY_PASSWORD = os.getenv("DB_PASSWORD")
MY_DATABASE = "researchlabmanager"

# Title names for functions
TABLE_TITLES = ["COLLABORATOR",
                "DEVICE",
                "EQUIPMENT",
                "FACULTY",
                "GRANT",
                "LAB_MEMBER",
                "PROJECT",
                "PUBLICATION",
                "PUBLISHES",
                "STUDENT",
                "USES",
                "WORKS"]
TABLE_SHORTHAND = ["C",
                "D",
                "E",
                "F",
                "G",
                "L",
                "P",
                "PC",
                "PS",
                "S",
                "U",
                "W"]

# Connect to the Database with relevant info
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=MY_PASSWORD,
        database=MY_DATABASE
    )

# Function for work in progress choices
def choice_wip():
    print("\nSorry, this feature is a Work In Progress.")

# Helper function to evaluate if the value for an attribute is the correct format
def check_attribute_value_format(data_type, value):
    if data_type == "int":
        try:
            int(value)
            return (1, value)
        except ValueError:
            print(f"Error: {value} is an invalid {data_type}")
    elif data_type == "date":
        return (1, value)
    elif re.fullmatch(r"varchar\(\d+\)", data_type):
        string_len = int(re.search(r"(\d+)", data_type).group())
        if len(value) <= string_len:
            return (1, f"\"{value}\"")
        else:
            print(f"Error: {value} is an invalid {data_type}, too long")
    return (0, None)

# Query the Database with parameter "query"
def query_db(query):
    try:
        # Connect to the Database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query);

        # Process Query
        query_result = cursor.fetchall()

        # Close Connection and return results
        conn.close()
        return query_result

    # Error handling
    except Exception as e:
        print("Error:", e)
        conn.close()

# Manipulate the Database with parameter "sql" and "val
def manipulate_db(sql, val):
    try:
        # Connect to the Database
        conn = connect_db()
        cursor = conn.cursor()

        # Process Manipulation
        print(sql)
        print(val)
        cursor.execute(sql, val);
        conn.commit()

        print(cursor.rowcount, "record(s) affected")

    # Error handling
    except Exception as e:
        print("Error:", e)

    # Close Connection
    conn.close()

# Read Function for all tables
def read_table(table_title):
    # Ensure table_title is a valid title
    if table_title is None or table_title.upper() not in TABLE_TITLES :
        print("Error: Invalid selection \"" + table_title + "\" for table title")
        return
    table_structure = query_db("DESCRIBE " + table_title)
    # Select: Which attributes wanted returned?
    # Where: Filter by condition
    # Order By: Sort by attribute
    # Group By:
    # Having: Filter Group By (Seems complicated)
    # Aggregate Functions: Count, Sum, Avg, min, max
    for row in query_db(
        """
        SELECT *
        FROM """ + table_title + """
        """
    ):
        print(row)

# Update Function for all tables
def update_table(table_title):
    # Ensure table_title is a valid title
    if table_title is None or table_title.upper() not in TABLE_TITLES :
        print("\nError: Invalid selection \"" + table_title + "\" for table title")
        return

    # Declare variables
    filter_attr = None
    filter_value = None
    update_attr = None
    update_value = None

    # Get Table Structure
    table_structure = query_db("DESCRIBE " + table_title)
    table_attributes = [inner[0] for inner in table_structure]

    # Loop through input options
    while True:
        # Text
        print("\nWhich attribute do you want to filter by?")
        print(table_attributes[0], end="")
        for attribute in table_attributes[1:]:
            print(", " + attribute, end="")
        print(" ")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            return
        elif choice == "EXIT":
            sys.exit()
        elif choice.upper() in table_attributes:
            filter_attr = choice.upper()
            break

    # Store the filter attribute data type
    data_type = table_structure[table_attributes.index(filter_attr)][1]

    # Loop through input options
    while True:
        # Text
        print(f"\nWhat value do you want to filter {filter_attr} by?")
        print(filter_attr + ": " + data_type)

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        check_results = check_attribute_value_format(data_type, choice)
        if (check_results[0] == 1):
            filter_value = check_results[1]
            break

                
    # Loop through input options
    while True:
        # Text
        print("\nWhich attribute do you want to update?")
        print(table_attributes[0], end="")
        for attribute in table_attributes[1:]:
            print(", " + attribute, end="")
        print(" ")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            return
        elif choice == "EXIT":
            sys.exit()
        elif choice.upper() in table_attributes:
            update_attr = choice.upper()
            break

    # Store the update attribute data type
    data_type = table_structure[table_attributes.index(update_attr)][1]

    # Loop through input options
    while True:
        # Text
        print(f"\nWhat value do you want to update {update_attr} to?")
        print(update_attr + ": " + data_type)

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        check_results = check_attribute_value_format(data_type, choice)
        if (check_results[0] == 1):
            update_value = check_results[1]
            break

    sql = f"UPDATE {table_title} SET {update_attr} = %s WHERE {filter_attr} = %s"
    val = (update_value, filter_value)
    manipulate_db(sql, val)

# WIP
# Insert into Database with parameter "query"
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

# TEMP
# Get the table for a specific format for creation
def create_table_format(query):
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
def create_member(tn):
    query_result = [None] * len(tables)
    for i in range(len(tables)):
        query_result[i] = create_table_format(
            """
                SELECT COLUMN_NAME
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
        elif choice == "t":
            update_table("PROJECT")
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
            read_table("LAB_MEMBER")
        elif choice == "UM":
            choice_wip()
        elif choice == "DM":
            choice_wip()
        elif choice == "CP":
            choice_wip()
        elif choice == "RP":
            read_table("PROJECT")
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