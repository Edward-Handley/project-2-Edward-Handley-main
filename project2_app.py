
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
@route('/players')
def player_data():
    return template('player_data')

# Team Data
@route('/trainings')
def player_data():
    return template('training_data')

@route('/search_members', method='GET')
def search_members():
    import queries  # Lazy import to avoid circular dependency
    search_field = request.query.get('search_field')
    search_query = request.query.get('search_query')
    results = queries.search_members(search_field, search_query)
    return template('member_data.tpl', members=results)



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
# Updated route to handle the new search form

# Route to handle search queries for members




# from bottle import route, run, template, request, static_file
# import sqlite3
# import scripts.create_database as create_database
# import insert_db_data as insert_db_data
# import queries


# ##################################################
# #
# # Constants
# #
# DATABASE_FILE = 'Database.db'

# import insert_db_data as insert_db_data  # Replace with the actual module name
# create_database.create_db(DATABASE_FILE)
# insert_db_data.insert_table_data(DATABASE_FILE)


# ##################################################


# # Homepage
# @route('/')
# def index():
#     return template('index')

# # Team Data
# @route('/team')
# def team_data():
#     return template('team_data')

# # Members Data
# @route('/members')
# def members_data():
#     return template('member_data')

# # Player Data
# @route('/players')
# def player_data():
#     return template('player_data')

# # Team Data
# @route('/trainings')
# def player_data():
#     return template('training_data')




# ########################################################
# # Constant for the database file name
# def run_query(query):
#     return run_query_with_parameters(query, {})

# def run_query_with_parameters(query, values):
#     connection = get_db_connection()
#     cursor = connection.cursor()

#     cursor.execute(query, values)
#     result = cursor.fetchall()

#     connection.close()

#     return result

# def get_template(query, title='Query Results', description='This page shows the results of a query'):
#     return get_template_with_parameters(query, {}, title, description)

# def get_template_with_parameters(query, values, title='Query Results', description='This page shows the results of a query'):
#     result = run_query_with_parameters(query, values)
#     if len(result) > 0:
#         page = template('results', title=title, description=description, records=result)
#     else:
#         page = template('no_results', title=title, description=description)
#     return page

# # Function to get the database connection
# def get_db_connection():
#     connection = sqlite3.connect(DATABASE_FILE)
#     connection.row_factory = sqlite3.Row
#     return connection


# @route('/static/<filename>')
# def static(filename):
#     return static_file(filename, root='./static')

# run(host='localhost', port=8080, debug=True, reloader=True)