import mysql.connector
import os
import sys
import re
from datetime import datetime
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
                "`GRANT`",
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
    # Check which data type is used
    # Integer
    if data_type == "int":
        # Try to convert to int, if successful, return value, else error
        try:
            int(value)
            return (1, value)
        except ValueError:
            print(f"Error: {value} is an invalid {data_type}")

    # Date
    elif data_type == "date":
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return (1, value)
        except ValueError:
            print(f"Error: {value} is an invalid {data_type}, date formatted as YYYY-MM-DD")
        #if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        #
        #else:
       #

    # Varchar(#) (String)
    elif re.fullmatch(r"varchar\(\d+\)", data_type):
        # Get varchar length
        string_len = int(re.search(r"(\d+)", data_type).group())

        # Ensure string is short enough, else return error
        if len(value) <= string_len:
            return (1, value)
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
    # Reformat to allow any case
    table_title = table_title.upper()

    # Ensure table_title is a valid title
    if table_title is None or table_title not in TABLE_TITLES :
        print("Error: Invalid selection \"" + table_title + "\" for table title")
        return

    # Text
    if table_title in ["COLLABORATOR", "FACULTY", "LAB_MEMBER", "PROJECT", "STUDENT", "WORKS"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Project and Member Management")
        print("    --- CRUD Members/Projects")
    elif table_title in ["DEVICE", "EQUIPMENT", "USES"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Equipment Usage Tracking")
        print("    --- CRUD Equipment/Equipment Usage")
    elif table_title in ["`GRANT`", "PUBLICATION", "PUBLISHES"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Grant and Publication Reporting")
        print("    --- CRUD Grants/Publications")
    print(f"      --- Read {table_title}")

    # Get Table Structure
    table_structure = query_db("DESCRIBE " + table_title)
    table_attributes = [inner[0] for inner in table_structure]

    # Query and Display Results
    for row in query_db(
        """
        SELECT *
        FROM """ + table_title + """
        """
    ):
        print(row)

# Update Function for all tables
def update_table(table_title):
    # Reformat to allow any case
    table_title = table_title.upper()
    
    # Ensure table_title is a valid title
    if table_title is None or table_title.upper() not in TABLE_TITLES :
        print("\nError: Invalid selection \"" + table_title + "\" for table title")
        return

    # Text
    if table_title in ["COLLABORATOR", "FACULTY", "LAB_MEMBER", "PROJECT", "STUDENT", "WORKS"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Project and Member Management")
        print("    --- CRUD Members/Projects")
    elif table_title in ["DEVICE", "EQUIPMENT", "USES"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Equipment Usage Tracking")
        print("    --- CRUD Equipment/Equipment Usage")
    elif table_title in ["`GRANT`", "PUBLICATION", "PUBLISHES"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Grant and Publication Reporting")
        print("    --- CRUD Grants/Publications")
    print(f"      --- Update {table_title}")

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
        print("Or type 0 to go back.")
        print("Or type EXIT to exit.")

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
        print("Or type 0 to go back.")
        print("Or type EXIT to exit.")

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

    # Prepare Data Manipulation SQL and Val parameters
    sql = f"UPDATE {table_title} SET {update_attr} = %s WHERE {filter_attr} = %s"
    val = (update_value, filter_value)

    # Loop through input options
    while True:
        # Text
        print(f"\nIs this correct?")
        print(f"sql = {sql}")
        print(f"fal = {val}")
        print("y. Yes (Apply Update)")
        print("n. No (Go back WITHOUT SAVING)")
        print("Or type EXIT to exit WITHOUT SAVING.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "n":
            return
        elif choice.upper() == "EXIT":
            sys.exit()
        elif choice.upper() == "Y":
            break
        else:
            continue

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        check_results = check_attribute_value_format(data_type, choice)
        if (check_results[0] == 1):
            update_value = check_results[1]
            break

    # Send Data Manipulation
    manipulate_db(sql, val)

# Delete Function for all tables
def delete_table(table_title):
    # Reformat to allow any case
    table_title = table_title.upper()

    # Ensure table_title is a valid title
    if table_title is None or table_title.upper() not in TABLE_TITLES:
        print("\nError: Invalid selection \"" + table_title + "\" for table title")
        return

    # Text
    if table_title in ["COLLABORATOR", "FACULTY", "LAB_MEMBER", "PROJECT", "STUDENT", "WORKS"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Project and Member Management")
        print("    --- CRUD Members/Projects")
    elif table_title in ["DEVICE", "EQUIPMENT", "USES"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Equipment Usage Tracking")
        print("    --- CRUD Equipment/Equipment Usage")
    elif table_title in ["`GRANT`", "PUBLICATION", "PUBLISHES"]:
        print("\n--- Research Lab Manager DBMS")
        print("  --- Grant and Publication Reporting")
        print("    --- CRUD Grants/Publications")
    print(f"      --- Delete {table_title}")

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
        print("Or type 0 to go back.")
        print("Or type EXIT to exit.")

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

    # Prepare Data Manipulation SQL and Val parameters
    sql = f"DELETE FROM {table_title} WHERE {filter_attr} = %s"
    val = [filter_value]

    # Loop through input options
    while True:
        # Text
        print(f"\nIs this correct?")
        print(f"sql = {sql}")
        print(f"fal = {val}")
        print("y. Yes (Apply Delete)")
        print("n. No (Go back WITHOUT SAVING)")
        print("Or type EXIT to exit WITHOUT SAVING.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "n":
            return
        elif choice.upper() == "EXIT":
            sys.exit()
        elif choice.upper() == "Y":
            break
        else:
            continue

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        check_results = check_attribute_value_format(data_type, choice)
        if (check_results[0] == 1):
            update_value = check_results[1]
            break

    # Send Data Manipulation
    manipulate_db(sql, val)

# Display the status of a project
def display_project_status():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Project and Member Management")
        print("    --- Project Status")
        print("Enter a Project ID number to view its status")
        print("Or type ALL to view project status")
        print("Or type B to go Back")
        print("Or type EXIT to exit.")

        # Declare variables
        pid = None

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice.upper() == "B":
            return
        elif choice.upper() == "EXIT":
            sys.exit()
        elif choice.upper() == "ALL":
            pid = "pid"
        else:
            check = check_attribute_value_format("int", choice)
            if (check[0]==1):
                pid = choice
            else:
                continue

        # Query and Display Results
        print("(PID, TITLE, STATUS)")
        for row in query_db(
            f"""
            SELECT pid, title, status
            FROM project
            WHERE pid = {pid}
            """
        ):
            print(row)

# Show members who have worked on projects funded by a given grant.
def display_grant_members():
    # Text
    print("\n--- Research Lab Manager DBMS")
    print("  --- Project and Member Management")
    print("    --- Display Grant Members")

    # Query and Display Results
    print("(MEMBER NAME, PID, GID)")
    for row in query_db(
        """
        SELECT m.NAME, w.PID, g.GID
        FROM lab_member AS m, works AS w, `grant` AS g
        WHERE m.MID = w.MID AND w.PID = g.PID
        """
    ):
        print(row)

# Show all mentor mentee pairs that work on the same project
def display_mentor_mentee_collaboration():
    # Text
    print("\n--- Research Lab Manager DBMS")
    print("  --- Project and Member Management")
    print("    --- Display Mentor-Mentee Collaboration")

    # Query and Display Results
    print("(MENTOR NAME, MENTEE NAME, PID)")
    for row in query_db(
        """
        SELECT mentor.NAME, mentee.NAME, w1.PID
        FROM lab_member AS mentor, lab_member AS mentee, works AS w1, works AS w2
        WHERE mentor.MID = mentee.MENTOR AND w1.MID = mentor.MID AND w2.MID = mentee.MID AND w1.PID = w2.PID
        """
    ):
        print(row)


# Show status of a piece of equipment
def display_equipment_status():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Equipment Usage Tracking")
        print("    --- Display Equipment Status")
        print("Enter a Equipment ID number to view its status")
        print("Or type ALL to view Equipment status")
        print("Or type B to go Back")
        print("Or type EXIT to exit.")

        # Declare variables
        eid = None

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice.upper() == "B":
            return
        elif choice.upper() == "EXIT":
            sys.exit()
        elif choice.upper() == "ALL":
            eid = "eid"
        else:
            check = check_attribute_value_format("int", choice)
            if (check[0]==1):
                eid = choice
            else:
                continue

        # Query and Display Results
        print("(EID, EQUIPMENT NAME, DEVICE ID, STATUS)")
        for row in query_db(
            f"""
            SELECT eid, e_name, did, status
            FROM equipment
            NATURAL JOIN device
            WHERE eid = {eid}
            """
        ):
            print(row)

# Show members currently using a given piece of equipment and the projects they
# are working on.
def display_equipment_usage():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Equipment Usage Tracking")
        print("    --- Display Equipment Usage")
        print("Enter a Equipment ID number to view its status")
        print("Or type ALL to view project status")
        print("Or type B to go Back")
        print("Or type EXIT to exit.")

        # Declare variables
        eid = None

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice.upper() == "B":
            return
        elif choice.upper() == "EXIT":
            sys.exit()
        elif choice.upper() == "ALL":
            eid = "e.eid"
        else:
            print("hello")
            check = check_attribute_value_format("int", choice)
            if (check[0] == 1):
                print("hello again")
                eid = choice
            else:
                continue

        # Query and Display Results
        print("(MID, MEMBER NAME, EQUIPMENT NAME, TITLE, PURPOSE)")
        for row in query_db(
            f"""
            SELECT
                lm.MID,
                lm.NAME AS member_name,
                e.E_NAME AS equipment_name,
                p.TITLE AS project_title,
                u.PURPOSE AS usage_purpose
            FROM USES u
            JOIN LAB_MEMBER lm ON u.MID = lm.MID
            JOIN DEVICE d ON u.DID = d.DID AND u.EID = d.EID
            JOIN EQUIPMENT e ON d.EID = e.EID
            JOIN WORKS w ON lm.MID = w.MID
            JOIN PROJECT p ON w.PID = p.PID
            WHERE e.EID = {eid}
                AND u.E_DATE IS NULL;
            """
        ):
            print(row)

# List the top 5 projects ranked by their total grant funding, and show the total
# amount each project received, in decreasing order of total funding (assume
# Budget is the dollar amount of each grant).
def display_top_five_projects():
    # Text
    print("\n--- Research Lab Manager DBMS")
    print("  --- Grant and Publication Reporting")
    print("    --- Top Five Projects")

    # Query and Display Results
    print("(WIP)")
    for row in query_db(
        """
        SELECT true
        FROM dual
        WHERE false;
        """
    ):
        print(row)

# Find the mentor(s) whose mentees collectively produced the largest number of
# publications.
def display_top_mentor():
    # Text
    print("\n--- Research Lab Manager DBMS")
    print("  --- Grant and Publication Reporting")
    print("    --- Display Top Mentors")

    # Query and Display Results
    print("(WIP)")
    for row in query_db(
        """
        SELECT true
        FROM dual
        WHERE false;
        """
    ):
        print(row)

# Calculate the total number of student publications per major and per publication
# year.
def display_student_publications():
    # Text
    print("\n--- Research Lab Manager DBMS")
    print("  --- Grant and Publication Reporting")
    print("    --- Display Student Publications")

    # Query and Display Results
    print("(WIP)")
    for row in query_db(
        """
        SELECT true
        FROM dual
        WHERE false;
        """
    ):
        print(row)

# Given a date X, find the projects that ended before X and the number of grants
# that funded each project.
def display_completed_projects():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Grant and Publication Reporting")
        print("    --- Display Completed Projects")
        print("0. Back")
        print("1. Sample Query")
        print("Or type EXIT to exit.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            break
        elif choice == "EXIT":
            sys.exit()
        elif choice == "1":
            pass
        else:
            continue

        # Query and Display Results
        print("(WIP)")
        for row in query_db(
            """
            SELECT true
            FROM dual
            WHERE false;
            """
        ):
            print(row)

# Find the three most productive years in terms of publications produced by
# students.
def display_productive_years():
    # Text
    print("\n--- Research Lab Manager DBMS")
    print("  --- Grant and Publication Reporting")
    print("    --- Display Productive Years")

    # Query and Display Results
    print("(WIP)")
    for row in query_db(
        """
        SELECT true
        FROM dual
        WHERE false;
        """
    ):
        print(row)

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
        elif choice.upper() == "T":
            #print(TABLE_TITLES)
            #function(input("Text: ").upper())
            display_equipment_status()
        elif choice.upper() == "EXIT":
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
            display_project_status()
        elif choice == "3":
            display_grant_members()
        elif choice == "4":
            display_mentor_mentee_collaboration()
        elif choice.upper() == "EXIT":
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
        elif choice.upper() == "CM":
            choice_wip()
        elif choice.upper() == "RM":
            read_table("LAB_MEMBER")
        elif choice.upper() == "UM":
            update_table("LAB_MEMBER")
        elif choice.upper() == "DM":
            choice_wip()
        elif choice.upper() == "CP":
            choice_wip()
        elif choice.upper() == "RP":
            read_table("PROJECT")
        elif choice.upper() == "UP":
            update_table("PROJECT")
        elif choice.upper() == "DP":
            choice_wip()
        elif choice.upper() == "EXIT":
            sys.exit()

# Equipment Usage Tracking sub menu
def equipment_usage_tracking():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Equipment Usage Tracking")
        print("0. Back")
        print("1. Create/Read/Update/Delete Equipment and Equipment Usage")
        print("2. Show status of a piece of equipment")
        print("3. Show members currently using a given piece of equipment and the projects they are working on.")
        print("Or type EXIT to exit.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            break
        elif choice == "1":
            crud_equipment()
        elif choice == "2":
            display_equipment_status()
        elif choice == "3":
            display_equipment_usage()
        elif choice == "EXIT":
            sys.exit()

# Equipment and Equipment Usage sub menu
def crud_equipment():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Equipment Usage Tracking")
        print("    --- CRUD Equipment/Equipment Usage")
        print("0. Back")
        print("CE. Create Equipment")
        print("RE. Read Equipment")
        print("UE. Update Equipment")
        print("DE. Delete Equipment")
        print("CD. Create Device")
        print("RD. Read Device")
        print("UD. Update Device")
        print("DD. Delete Device")
        print("CU. Create Uses")
        print("RU. Read Uses")
        print("UU. Update Uses")
        print("DU. Delete Uses")
        print("Or type EXIT to exit.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            break
        elif choice.upper() == "CE":
            choice_wip()
        elif choice.upper() == "RE":
            read_table("EQUIPMENT")
        elif choice.upper() == "UE":
            update_table("EQUIPMENT")
        elif choice.upper() == "DE":
            choice_wip()
        elif choice.upper() == "CD":
            choice_wip()
        elif choice.upper() == "RD":
            read_table("DEVICE")
        elif choice.upper() == "UD":
            update_table("DEVICE")
        elif choice.upper() == "DD":
            choice_wip()
        elif choice.upper() == "CU":
            choice_wip()
        elif choice.upper() == "RU":
            read_table("USES")
        elif choice.upper() == "UU":
            update_table("USES")
        elif choice.upper() == "DU":
            choice_wip()
        elif choice.upper() == "EXIT":
            sys.exit()

# Grant and Publication Reporting sub menu
def grant_publication_reporting():
    # Loop display message waiting on user input
    while True:
        # Text
        print("\n--- Research Lab Manager DBMS")
        print("  --- Grant and Publication Reporting")
        print("0. Back")
        print("""1. List the top 5 projects ranked by their total grant funding, and show the total
amount each project received, in decreasing order of total funding (assume
Budget is the dollar amount of each grant).""")
        print("""2. Find the mentor(s) whose mentees collectively produced the largest number of
publications.""")
        print("""3. Calculate the total number of student publications per major and per publication
year.""")
        print("""4. Given a date X, find the projects that ended before X and the number of grants
that funded each project.""")
        print("""5. Find the three most productive years in terms of publications produced by
students.""")
        print("Or type EXIT to exit.")

        # Get Input
        choice = input("Choose an option: ")

        # Evaluate Input
        if choice == "0":
            break
        elif choice == "1":
            display_top_five_projects()
        elif choice == "2":
            display_top_mentor()
        elif choice == "3":
            display_student_publications()
        elif choice == "4":
            display_completed_projects()
        elif choice == "5":
            display_productive_years()
        elif choice.upper() == "EXIT":
            sys.exit()

main_menu()