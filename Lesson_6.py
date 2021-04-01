'''
****************************************************************************
*  Program  lessson_6.py                                                   *
*  Author   Myles                                                          *
*  Date     March 23, 2021                                                 *
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
        print("\nConnection to SQLite DB successful\n")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
###################  Connect to The Database File *********************
connection = create_connection("oak8_pods.sqlite6")
##########################  Create And Execute Queries ################
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""
execute_query(connection, create_users_table)
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""
execute_query(connection, create_posts_table)
create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""
execute_query(connection, create_comments_table)
create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  post_id integer NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""
execute_query(connection, create_likes_table)
create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""
execute_query(connection, create_users)
create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""
execute_query(connection, create_posts)
create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""
execute_query(connection, create_comments)
create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""
execute_query(connection, create_likes)
print('\n')
########################### Display staff_member Query #####################
display_user_query = "SELECT * from users"
users = execute_read_query(connection, display_user_query)
for user in users:
	print(user)
print('\n')
select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""
users_posts = execute_read_query(connection, select_users_posts)
print('\n')
for users_post in users_posts:
    print(users_post)
print('\n')
select_posts_comments_users = """
SELECT
  posts.description as post,
  text as comment,
  name
FROM
  posts
  INNER JOIN comments ON posts.id = comments.post_id
  INNER JOIN users ON users.id = comments.user_id
"""
posts_comments_users = execute_read_query(
    connection, select_posts_comments_users
)
cursor = connection.cursor()
cursor.execute(select_posts_comments_users)
cursor.fetchall()
column_names = [description[0] for description in cursor.description]
print('\n',column_names)
for posts_comments_user in posts_comments_users:
    print(posts_comments_user)
print('\n')
execute_query(connection,'Drop table users')
execute_query(connection,'Drop table posts')
execute_query(connection,'Drop table comments')
execute_query(connection,'Drop table likes')
print('\n')