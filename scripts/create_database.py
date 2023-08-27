
import sqlite3

###############################
# SET UP EMPTY DATABASE
#
# Drop the tables from the database if they exist so we can run the CREATE statements
# NOTE: If there is data in the database, tables need to be dropped in the correct order 
# to maintain referential integrity
#
def drop_tables(cursor):
    print('Drop tables if they exist')
    query = """
            DROP TABLE IF EXISTS Members;
            DROP TABLE IF EXISTS Players;
            DROP TABLE IF EXISTS Teams;
            DROP TABLE IF EXISTS Trainings;
            DROP TABLE IF EXISTS Venues;
            """
    # Use executescript as there are multiple queries in the same string
    cursor.executescript(query)

def update_pragma(cursor):
    # Update the database to allow foreign keys to enforce referential integrity
    print("Update PRAGMA to support foreign keys")
    query = "PRAGMA foreign_keys = ON"
    cursor.execute(query)



# Create the database tables
def create_members_table(cursor):
    print("Create Members Table")
    query = """CREATE TABLE Members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        dob TEXT NOT NULL,
        phone TEXT
        )"""
    cursor.execute(query)

def create_players_table(cursor):
    print("Create Players Table")
    query = """CREATE TABLE Players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        team_id INTEGER,
        FOREIGN KEY(member_id) REFERENCES Members(member_id),
        FOREIGN KEY(team_id) REFERENCES Teams(team_id)
        )"""
    cursor.execute(query)

def create_teams_table(cursor):
    print("Create Teams Table")
    query = """CREATE TABLE Teams (
        team_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age_group TEXT NOT NULL,
        division TEXT NOT NULL
        )"""
    cursor.execute(query)

def create_trainings_table(cursor):
    print("Create Trainings Table")
    query = """CREATE TABLE Trainings (
        training_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        venue_id INTEGER,
        coach TEXT NOT NULL,
        FOREIGN KEY(venue_id) REFERENCES Venues(venue_id)
        )"""
    cursor.execute(query)

def create_venues_table(cursor):
    print("Create Venues Table")
    query = """CREATE TABLE Venues (
        venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        address TEXT NOT NULL,
        entrance_fee BOOLEAN NOT NULL
        )"""
    cursor.execute(query)
####Creat DB####
def create_db(database_name):
    try:
        # Create connection to database
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()

        # Drop and create tables
        create_members_table(cursor)
        create_players_table(cursor)
        create_teams_table(cursor)
        create_trainings_table(cursor)
        create_venues_table(cursor)

        # Commit changes to the database and close connection
        connection.commit()
        connection.close()

        return "success"

    except Exception as e:
        print("Error: ", e)
        connection.rollback()
        connection.close()
        return "error"


# Main function to set up the database
# def main():
#     conn = sqlite3.connect('uwa_waterpolo_club.db')
#     cursor = conn.cursor()
    
#     drop_tables(cursor)
#     create_tables(cursor)
    
#     conn.commit()
#     conn.close()

# if __name__ == '__main__':
#     main()



























# import sqlite3

# #
# def drop_tables(cursor):
#     print('Drop tables if they exist')
#     query = """
#             DROP TABLE IF EXISTS Price;
#             DROP TABLE IF EXISTS Station;
#             DROP TABLE IF EXISTS Area;
#             DROP TABLE IF EXISTS Product;
#             DROP TABLE IF EXISTS Region;
#             DROP TABLE IF EXISTS Brand;
#             """
#     # Use executescript as there are multiple queries in the same string
#     cursor.executescript(query)

# def update_pragma(cursor):
#     # Update the database to allow foreign keys to enforce referential integrity
#     print("Update PRAGMA to support foreign keys")
#     query = "PRAGMA foreign_keys = ON"
#     cursor.execute(query)


# # Establish a connection to the database
# conn = sqlite3.connect('project2.db')
# cursor = conn.cursor()

# # SQL queries to create the tables
# create_members_table = '''
# CREATE TABLE IF NOT EXISTS Members (
#     MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
#     FirstName TEXT NOT NULL,
#     LastName TEXT NOT NULL,
#     Age INTEGER,
#     DateOfBirth TEXT,
#     PhoneNumber TEXT,
#     Email TEXT
# );
# '''

# create_players_table = '''
# CREATE TABLE IF NOT EXISTS Players (
#     PlayerID INTEGER PRIMARY KEY AUTOINCREMENT,
#     MemberID INTEGER,
#     TeamID INTEGER,
#     FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
# );
# '''

# create_team_table = '''
# CREATE TABLE IF NOT EXISTS Team (
#     TeamID INTEGER PRIMARY KEY AUTOINCREMENT,
#     AgeGroup TEXT,
#     Division TEXT
# );
# '''

# create_trainings_table = '''
# CREATE TABLE IF NOT EXISTS Trainings (
#     TrainingID INTEGER PRIMARY KEY AUTOINCREMENT,
#     DateTime TEXT,
#     Venue TEXT,
#     Coach TEXT
# );
# '''

# create_venue_table = '''
# CREATE TABLE IF NOT EXISTS Venue (
#     VenueID INTEGER PRIMARY KEY AUTOINCREMENT,
#     Address TEXT,
#     EntranceFee BOOLEAN
# );
# '''

# # Execute the SQL queries to create the tables
# cursor.execute(create_members_table)
# cursor.execute(create_players_table)
# cursor.execute(create_team_table)
# cursor.execute(create_trainings_table)
# cursor.execute(create_venue_table)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

# # Confirmation that the tables have been created
# "Database tables created successfully."