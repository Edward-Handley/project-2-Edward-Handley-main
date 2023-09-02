
# Queries stored as constants
SELECT_ALL_MEMBERS = 'SELECT * FROM Members'
SEARCH_MEMBERS = 'SELECT * FROM Members WHERE first_name = :first_name'

SELECT_MEMBERS_AND_TEAMS = '''SELECT Members.first_name, Members.last_name, Teams.name AS team_name 
                              FROM Members 
                              JOIN Players ON Members.member_id = Players.member_id 
                              JOIN Teams ON Players.team_id = Teams.team_id
                              ORDER BY team_name'''

ALL_VENUES = 'SELECT * FROM Venues'

SELECT_ONLY_TEAMS = "SELECT * FROM Teams"

ALL_SPONSORS = "SELECT * FROM Sponsors"