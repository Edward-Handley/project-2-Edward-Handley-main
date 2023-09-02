<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Teams Page</title>
        <link rel="stylesheet" href="/static/team_page.css">
        <link rel="stylesheet"  href="/static/navbar.css">

    </head>
        <body>

        <header>
            <h1>Teams Page</h1>
        </header>

       <div class="universal-navbar">
         <nav class="navbar">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/members">Members</a></li>
                    <li><a href="/venue">Venues</a></li>
                    <li><a href="/trainings">Trainings</a></li>
                </ul>
         </nav>
        </div>

        <div class="container">
            <div class="feature-box">
                <h2>Players and Teams</h2>
                <p>View the list of players and their respective teams.</p>
                <a href="/members_and_teams">Go to Players and Teams</a>
            </div>

            <!-- Add more feature boxes for additional functionalities -->
            <div class="feature-box">
                <h2>All Teams</h2>
                <p>See all teams.</p>
                <a href="/only_teams">Go to All Teams</a>
            </div>

            
        </div>
        <div class="add-team-section">
        <h1>Add New Team</h1>
        <form action="/add_team" method="post" id="add-team-form">
            <input type="name" name="name" id="name" placeholder="Team name" required>
            <label for="age-group">Choose a age group:</label>
            <select name="age-group" id="age-group">
                <option value="U21">U21</option>
                <option value="U18">U18</option>
                <option value="Senior">Senior</option>
            </select>
            <!-- Drop-down for selecting venue -->
            <label for="division">Choose a division:</label>
            <select name="division" id="division">
                <option value="Division 1">Division 1</option>
                <option value="Division 2">Division 2</option>     
            </select>
            <button type="submit" id="add-button">Add Team</button>
        </form>

        </body>
</html>