from bottle import route, run, template, request, static_file
import sqlite3
import scripts.create_database as create_database
import insert_db_data as insert_db_data
import queries


##################################################
#
# Constants
#
DATABASE_FILE = 'Database.db'
create_database.create_db(DATABASE_FILE)
insert_db_data.insert_table_data(DATABASE_FILE)


##################################################


# Homepage
@route('/')
def index():
    return template('index')

# Team Data
@route('/team')
def team_data():
    return template('team_data')

# Members Data
@route('/members')
def members_data():
    return template('member_data')

# Player Data
@route('/venue')
def player_data():
    return template('venue_data')

# Team Data
@route('/trainings')
def player_data():
    return template('training_data')

###Hard Coded Queries###
@route('/members_and_teams')
def members_and_teams():
    query = queries.SELECT_MEMBERS_AND_TEAMS
    title = 'Members and Their Teams'
    description = 'This page shows all members and their respective teams.'
    return get_template(query, title, description)

@route('/venues_summary')
def venues_and_info():
    query = queries.ALL_VENUES
    title = 'Venues and Their Info'
    description = 'This page shows the Venues and their info.'
    return get_template(query, title, description)


###Dyanmic Queries###
@route('/search_members')
def search_members():
    return template('member_data')

@route('/search_members', method="POST")
def search_members_post():
    member_name = request.forms.get('member_name')
    values = {'first_name': member_name}

    title = f'Search Results for {member_name}'
    description = f'This page shows the results of a search for {member_name}'
    query = queries.SEARCH_MEMBERS
    try:
        return get_template_with_parameters(query, values, title, description)
    except Exception as e:
        return f"An error occurred: {str(e)}"

###Add new to DB###
@route('/add_venue', method='POST')
def add_venue():
    name = request.forms.get('name')
    location = request.forms.get('location')
    address = request.forms.get('address')
    entrance_fee = int(request.forms.get('entrance_fee'))

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Venues (name, location, address, entrance_fee) VALUES (?, ?, ?, ?)",
                   (name, location, address, entrance_fee))

    conn.commit()
    conn.close()

    return template('conformation', title="Venue Added Successfully", message="Your new venue has been added to the database.", return_url="/venue")



########################################################
# Constant for the database file name
def run_query(query):
    return run_query_with_parameters(query, {})

def run_query_with_parameters(query, values):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(query, values)
    result = cursor.fetchall()

    connection.close()

    return result

def get_template(query, title='Query Results', description='This page shows the results of a query'):
    return get_template_with_parameters(query, {}, title, description)

def get_template_with_parameters(query, values, title='Query Results', description='This page shows the results of a query'):
    result = run_query_with_parameters(query, values)
    if len(result) > 0:
        page = template('results', title=title, description=description, records=result)
    else:
        page = template('no_results', title=title, description=description)
    return page



# Function to get the database connection
def get_db_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection


@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)

