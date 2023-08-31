
<!DOCTYPE html>
<html>
<head>
    <title>Members Page</title>
    <link rel="stylesheet" href="/static/members_page.css">
    <link rel="stylesheet"  href="/static/navbar.css">
</head>
<body>

    <!-- Header -->
    <header>
        <h1>Members Page</h1>
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
    

    <!-- Main Content -->
    <main>

    <!-- Search Section -->
        <!-- Search Card -->
        <div class="search-card">
            <h2>Search Members</h2>
            <form action="/search_members" method="post">
                <input type="text" name="member_name" placeholder="Enter the name to search..." />
                <button type="submit">Search</button>
            </form>
        </div>



        <!-- Section 2: Add New Members -->
        <div class="add-member-section">
            <h1>Add New Member</h1>
            <form action="/add_member" method="post" id="add-member-form">
                <input type="text" name="first_name" id="first_name" placeholder="First Name" required>
                <input type="text" name="last_name" id="last_name" placeholder="Last Name" required>
                <input type="date" name="dob" id="dob" placeholder="DOB" required>
                <input type="email" name="email" id="Email" placeholder="Email" required>
                <input type="tel" name="phone" id="phone" placeholder="Phone" required>
                <button type="submit" id="add-button">Add Member</button>
            </form>
        </div>

    </main>

    <!-- Footer -->
    <footer>
        <!-- Footer content can go here -->
    </footer>

</body>
</html>
