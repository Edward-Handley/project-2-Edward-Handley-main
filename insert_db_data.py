import sqlite3

def insert_Members_data(cursor):
	print('Start inserting data into Members table')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (1, "Sarah", "Johnson", "sarah.johnson@example.com", "20-08-2004", 0461478099)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (2, "Emily", "Jones", "emily.jones@example.com", "31-03-2002", 0432492546)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (3, "Sarah", "Williams", "sarah.williams@example.com", "01-04-1975", 0440481346)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (4, "Sarah", "Smith", "sarah.smith@example.com", "15-06-2006", 0423452404)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (5, "Sarah", "Brown", "sarah.brown@example.com", "08-08-2000", 0445909622)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (6, "John", "Brown", "john.brown@example.com", "11-12-2002", 0423958565)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (7, "John", "Johnson", "john.johnson@example.com", "31-01-2006", 0496713871)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (8, "Michael", "Brown", "michael.brown@example.com", "17-05-1980", 0485230309)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (9, "Michael", "Smithy", "michael.smithy@example.com", "06-03-2000", 0495651549)''')
	cursor.execute('''INSERT INTO Members (member_id, first_name, last_name, email, dob, phone) VALUES (10, "Sarah", "Williams", "sarah.williams@example.com", "25-04-2010", 0434782260)''')
	print('Finish inserting data into Members table')

def insert_Players_data(cursor):
	print('Start inserting data into Players table')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (1, 1, 2)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (2, 2, 4)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (3, 3, 4)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (4, 4, 2)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (5, 5, 2)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (6, 6, 2)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (7, 7, 1)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (8, 8, 3)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (9, 9, 1)''')
	cursor.execute('''INSERT INTO Players (player_id, member_id, team_id) VALUES (10, 10, 2)''')
	print('Finish inserting data into Players table')

def insert_Teams_data(cursor):
	print('Start inserting data into Teams table')
	cursor.execute('''INSERT INTO Teams (team_id, name, age_group, division) VALUES (1, "UWA Bears", "U21", "Division 1")''')
	cursor.execute('''INSERT INTO Teams (team_id, name, age_group, division) VALUES (2, "UWA Golds", "U21", "Division 2")''')
	cursor.execute('''INSERT INTO Teams (team_id, name, age_group, division) VALUES (3, "UWA Blues", "Senior", "Division 1")''')
	cursor.execute('''INSERT INTO Teams (team_id, name, age_group, division) VALUES (4, "UWA Greens", "U18", "Division 2")''')
	print('Finish inserting data into Teams table')

def insert_Trainings_data(cursor):
	print('Start inserting data into Trainings table')
	cursor.execute('''INSERT INTO Trainings (training_id, date, time, venue_id, coach) VALUES (1, "2023-2-11", "5:30", 1, "Kovalenko")''')
	cursor.execute('''INSERT INTO Trainings (training_id, date, time, venue_id, coach) VALUES (2, "2023-5-25", "6:30", 1, "Kelly")''')
	cursor.execute('''INSERT INTO Trainings (training_id, date, time, venue_id, coach) VALUES (3, "2023-9-16", "12:30", 1, "Kovalenko")''')
	print('Finish inserting data into Trainings table')

def insert_Venues_data(cursor):
	print('Start inserting data into Venues table')
	cursor.execute('''INSERT INTO Venues (venue_id, name, location, address, entrance_fee) VALUES (1, "UWA Pool", "Perth", "Parkway Crawley WA 6009", "False")''')
	cursor.execute('''INSERT INTO Venues (venue_id, name, location, address, entrance_fee) VALUES (2, "HBF Stadium", "Perth", "100 Stephenson Ave Mount Claremont WA 6010", "True")''')
	print('Finish inserting data into Venues table')

def insert_table_data(database_name):
	try:
		connection = sqlite3.connect(database_name)
		cursor = connection.cursor()

		insert_Members_data(cursor)
		insert_Players_data(cursor)
		insert_Teams_data(cursor)
		insert_Trainings_data(cursor)
		insert_Venues_data(cursor)

		connection.commit()
		connection.close()

		return "Data inserted successfully"
	except Exception as e:
		print("Error: ", e)
		connection.rollback()
		connection.close()
		return "Error inserting data into database"