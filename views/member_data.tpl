
<!DOCTYPE html>
<html>
<head>
    <title>Members Page</title>
    <link rel="stylesheet" href="/static/members_page.css">
</head>
<body>

    <!-- Header -->
    <header>
        <h1>Club Waterpolo Management</h1>
    </header>

    <!-- Navigation -->
    <nav>
      
        <a href="/">Home</a>   
    </nav>

    <!-- Main Content -->
    <main>

    <form action="/search_members" method="post">
        Enter the name: <input type="text" name="member_name" /><br />
        <input type="submit">
    </form> 

        <!-- Section 2: Add New Members -->
        <div class="add-member-section">
            <h1>Add New Member</h1>
            <form action="/add_member" method="post" id="add-member-form">
                <input type="text" name="first_name" placeholder="First Name" required>
                <input type="text" name="last_name" placeholder="Last Name" required>
                <input type="date" name="dob" placeholder="DOB" required>
                <input type="email" name="email" placeholder="Email" required>
                <input type="tel" name="phone" placeholder="Phone" required>
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
