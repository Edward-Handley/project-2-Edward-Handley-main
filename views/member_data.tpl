
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
        <!-- Navigation links can go here -->
    </nav>

    <!-- Main Content -->
    <main>

    <form action="/search_members" method="get">
      <label for="search_field">Search By:</label>
        <select name="search_field" id="search_field">
          <option value="first_name">First Name</option>
          <option value="last_name">Last Name</option>
          <option value="email">Email</option>
          <option value="phone">Phone</option>
        </select>
        <input type="text" name="search_query" placeholder="Search for a member...">
      <button type="submit">Search</button>
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
