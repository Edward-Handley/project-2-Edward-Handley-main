
# Import the get_db_connection function from your main application file
from project2_app import get_db_connection

# Function to query Members table and fetch all members
def get_all_members():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM Members")
    return c.fetchall()

# Other query functions go here...
