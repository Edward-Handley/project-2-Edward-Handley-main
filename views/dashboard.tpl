<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
    <link rel="stylesheet" href="/static/dashboard.css">
    <link rel="stylesheet" href="/static/navbar.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="/static/dashboard.js"></script>

</head>
<body>

    <header>
        <h1>Dashboard</h1>
    </header>

    <div class="universal-navbar">
        <nav class="navbar">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/members">Members</a></li>
                <li><a href="/team">Teams</a></li>
                <li><a href="/venue">Venues</a></li>
                <li><a href="/trainings">Trainings</a></li>
            </ul>
        </nav>
    </div>

    <div class="container">
        <div class="stat-box">
            <h2>Total Members</h2>
            <p>{{ total_members }}</p>
        </div>

        <div class="stat-box">
            <h2>Total Teams</h2>
            <p>{{ total_teams }}</p>
        </div>

        <div class="stat-box">
            <h2>Total Venues</h2>
            <p>{{ total_venues }}</p>
        </div>

        <div class="stat-box">
            <h2>Total Trainings</h2>
            <p>{{ total_trainings }}</p>
        </div>
    </div>
   


    <footer>
        <!-- Footer content can go here -->
    </footer>

</body>
</html>



