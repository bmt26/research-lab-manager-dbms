# research-lab-manager-dbms

## ToDo:

* Fix Read

  * Read Table Customization

    * Select: Which attributes wanted returned?
    * Where: Filter by condition
    * Order By: Sort by attribute
    * Group By:
    * Having: Filter Group By (Seems complicated)
    * Aggregate Functions: Count, Sum, Avg, min, max
* Cascading Update/Delete
* Special Case for Labmember CRUD
* Custom CRUD?
* Allow for NULL inserts and updates
* Double Check CRUD still Works



Core setup + Project \& Member Management

Tables primarily under your ownership

\[x] LAB\_MEMBER

\[x] STUDENT

\[x] FACULTY

\[x] COLLABORATOR

\[x] PROJECT

\[x] WORKS

TODO:

\[\~] Implement Lab Member disjoint subclass, must pick one and only one (type attribute NOT NULL),

\[-] Each lab member works on at least one project

\[x] Each project has exactly one leader (NOT NULL)

\[x] A student cannot mentor faculty members

(341, "Stacy Gwen", "1972-12-23", "Student", null, null, null, 234, "Freshman", "Computer Science")

Menu

> pip install mysql-connector-python

> python menu-application.py



