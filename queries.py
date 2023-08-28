
# Import the get_db_connection function from your main application file
from project2_app import get_db_connection
import sqlite3

# Function to query Members table and fetch all members
def get_all_members():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM Members")
    return c.fetchall()

# Other query functions go here...

# Function to search Members table based on the search query
def search_members(search_query):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM Members WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR phone LIKE ?", ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
    results = c.fetchall()
    conn.close()
    return results

# Function to add a new member
def add_new_member(first_name, last_name, dob, email, phone):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO Members (first_name, last_name, dob, email, phone) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, dob, email, phone))
    conn.commit()
    conn.close()

# Updated function to search members by a specific field
from project2_app import DB_FILENAME


def search_members(search_field, search_query):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute(f"SELECT * FROM Members WHERE {search_field} LIKE ?", ('%' + search_query + '%',))
    results = c.fetchall()
    conn.close()
    return results
