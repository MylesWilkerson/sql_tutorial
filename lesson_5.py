'''****************************************************************************
*  Program  lessson_5.py                                                   *
*  Author   Myles Wilkerson                                                 *
*  Date     March 31, 2021                                                 *
*  Source   Realpython https://realpython.com/python-sql-libraries/#sqlite *
*  Description:                                                            *
*  This program is used to introduce Geniuses to using a                   *
*  database Structured Query Language (SQL).  The program                  *
*  imports the sqlite3 module which allows you to create                   *
*  and interact with an SQL Database                                       *
*                                                                          *
*  - The create_connection function is passed the                          *
*    path of the SQLite database file then it connects                     *
*    the app to an exixting SQLite3 database named hgp_pods                *
*    or if it;s not present it creates the database file                   *
*                                                                          *
*  - The execute_query function is passed the path and the                 *
*    query to implement; create_staff_member_table query and               *
*    add_staff_member query                                                *
*                                                                          *
*  - The execute_read function is passed the path and                      *
*    the display_staff_member query                                        *
****************************************************************************
'''
import sqlite3
from sqlite3 import Error
############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
def execute_query(connection, query): #Input Query, only inputs database
    cursor = connection.cursor()
    try: #Tries cursor
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully") #If try is successful, green text is printed
    except Error as e: #If try is unseccessful, error is run and green text is pritned
        print(f"The error '{e}' occurred")
def execute_read_query(connection, query): #Telling database to do soemthing but is excepting somethingin return
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
###################  Connect/Create to the Sqlite3 Database File *********************
connection = create_connection("oak8_pods.sqlite5")
##########################  Create staff table variable query ################
create_staff_member_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
#lines above creates table
#################### Executive query to create staff table #################
execute_query(connection, create_staff_member_table_query) #inputs soemthing into databse and doesn't expect return result
create_pod_leader_table_query = """
CREATE TABLE IF NOT EXISTS leader (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_pod_leader_table_query)
create_pod_member_table_query = """
CREATE TABLE IF NOT EXISTS member (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_pod_member_table_query)
################# Create insert query to add staff members to staff table #######
add_staff_members_query = """
INSERT INTO
  staff (name,cell,position)
VALUES
  ('Baba','510.205.0980','Senior Innovation Educator'),
  ('Brandon','111.111.1111', 'Executive Director'),
  ('Hodari','(510) 435-2594','Curriculum Lead'),
  ('Akeeem','(415) 684-0505','Programs Director');
"""
#lines above adds more things to table
####################  Execute insert staff members query ##################
execute_query(connection, add_staff_members_query)
add_pod_leader_query = """
INSERT INTO
    leader (name, cell, position)
VALUES
    ('Richard','111.111.1111','Pod Leader'),
    ('Andrew','111.111.1111','Pod Leader'),
    ('Jacore','111.111.1111','Pod Leader'),
    ('Aris','111.111.1111','Pod Leader'),
    ('Gabriel','111.111.1111','Pod Leader');
"""
execute_query(connection, add_pod_leader_query)
add_pod_member_query = """
INSERT INTO
    member (name, cell, position)
VALUES
    ('Myles','111.111.1111','Pod Member'),
    ('Kymari','111.111.1111','Pod Member'),
    ('Gaelan','111.111.1111','Pod Member'),
    ('David','111.111.1111','Pod Member'),
    ('Emmanuel','111.111.1111','Pod Member'),
    ('Josiah','111.111.1111','Pod Member'),
    ('Glenn','111.111.1111','Pod Member'),
    ('Hyab','111.111.1111','Pod Member'),
    ('Maurice','111.111.1111','Pod Member'),
    ('Milan','111.111.1111','Pod Member'),
    ('Morris','111.111.1111','Pod Member'),
    ('Moussa','111.111.1111','Pod Member'),
    ('Malick','111.111.1111','Pod Member'),
    ('Prince','111.111.1111','Pod Member'),
    ('Ronin','111.111.1111','Pod Member');
"""
execute_query(connection, add_pod_member_query)
########################### Display staff_member Query #####################
display_staff_query = "SELECT * from staff" #This line and next line is returning list as tuple, or unchanging list
staff = execute_read_query(connection, display_staff_query) #executes read query is given by a list,
                                                            #and it is being looped and printing out each
                                                            #row, or string
display_leader_query = "SELECT * from leader"
leader = execute_read_query(connection, display_leader_query)
display_member_query = "SELECT * from member"
member = execute_read_query(connection, display_member_query)
for user in staff: #looping through results and returns in row as print statement/prints each row
  print(user)
print("\n")
for user in leader:
  print(user)
print("\n")
for user in member:
  print(user)
print("\n")
execute_query(connection,'drop table staff') #drops all of the rows from table, essentially deleting the table
execute_query(connection,'drop table leader')
execute_query(connection,'drop table member')
