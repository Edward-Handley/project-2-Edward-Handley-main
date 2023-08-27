
<!DOCTYPE html>
<html>
<head>
  <title>Members Page</title>
  <style>
    /* Basic styling */
    body { font-family: Arial, sans-serif; margin: 20px; }
    header, footer { background-color: #f2f2f2; padding: 15px; text-align: center; }
    nav { text-align: center; background-color: #333; color: white; padding: 10px; }

    /* Search and Filter section */
    .search-section { margin-bottom: 20px; }
    .search-bar, .filter { margin: 10px; }

    /* Results Table */
    table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    th { background-color: #f2f2f2; }

    /* Add New Members section */
    .new-member-section input { margin: 5px; }
  </style>
</head>
<body>

  <header>Header</header>
  <nav>Navbar</nav>

  <section class="search-section">
    <h2>Search and Filter Members</h2>
    <input type="text" class="search-bar" placeholder="Search Members">
    <div class="filter">Filters: <select><option>ID</option><option>Name</option><option>DOB</option></select></div>
  </section>

  <section>
    <h2>Results</h2>
    <table>
      <tr>
        <th>ID</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>DOB</th>
        <th>Email</th>
        <th>Phone</th>
      </tr>
      <!-- Data will be inserted here -->
    </table>
  </section>

  <section class="new-member-section">
    <h2>Add New Members</h2>
    <input type="text" placeholder="First Name">
    <input type="text" placeholder="Last Name">
    <input type="date" placeholder="DOB">
    <input type="email" placeholder="Email">
    <input type="tel" placeholder="Phone">
    <button type="submit">Submit</button>
  </section>

  <footer>Footer</footer>

</body>
</html>
