<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sponsors Page</title>
    <link rel="stylesheet" href="/static/sponsor.css">
    <link rel="stylesheet"  href="/static/navbar.css">
</head>
<body>

    <header>
        <h1>Sponsors Page</h1>
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
        <div class="feature-box">
            <h2>Our Sponsors</h2>
            <p><a href="/all_sponsors">View the list of our respected sponsors.</a></p>
        </div>
    </div>

    <div class="add-sponsor-section">
        <h1>Add New Sponsor</h1>
        <form action="/add_sponsor" method="post" id="add-sponsor-form">
            <input type="text" name="name" id="name" placeholder="Sponsor Name" required>
            <input type="email" name="email" id="email" placeholder="Sponsor Email" required>
            <input type="number" name="contribution_amount" id="contribution_amount" placeholder="Contribution Amount" required>
            <button type="submit" id="add-button">Add Sponsor</button>
        </form>
    </div>

</body>
</html>
