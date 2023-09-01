
<!DOCTYPE html>
<html>
<head>
    <title>Training Page</title>
    <link rel="stylesheet" href="/static/training_page.css">
    <link rel="stylesheet" href="/static/navbar.css">
</head>
<body>

    <!-- Header -->
    <header>
        <h1>Training Page</h1>
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
    <div class="training-card">
    <h2>Upcoming Training Sessions</h2>
    <!-- Table for displaying the training sessions -->
        <table>
            <tr>
                <th>Training ID</th>
                <th>Date</th>
                <th>Time</th>
                <th>Coach</th>
                <th>Venue ID</th>
            </tr>
            % for training in training_sessions:
            <tr>
                <td>{{ training[0] }}</td>
                <td>{{ training[1] }}</td>
                <td>{{ training[2] }}</td>
                <td>{{ training[3] }}</td>
                <td>{{ training[4] }}</td>
            </tr>
            % end
        </table>
    </div>
    <div class="add-training-section">
    <h1>Add New Training</h1>
    <form action="/add_training" method="post" id="add-training-form">
        <input type="date" name="date" id="date" placeholder="Training Date" required>
        <input type="time" name="time" id="time" placeholder="Training Time" required>
        <label for="coach">Choose a coach:</label>
        <select name="coach" id="coach">
            <option value="Kovalenko">Kovalenko</option>
            <option value="Kelly">Kelly</option>
        </select>
        <!-- Drop-down for selecting venue -->
        <label for="venue_id">Choose a venue:</label>
        <select name="venue_id" id="venue_id">
            % for venue in venues:
                <option value="{{venue[0]}}">{{venue[1]}}</option>
            % end
        </select>
        <button type="submit" id="add-button">Add Training</button>
    </form>
</div>

    <!-- Footer -->
    <footer>
        <!-- Footer content can go here -->
    </footer>

</body>
</html>
