<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Teams Page</title>
        <link rel="stylesheet" href="/static/venue_page.css">
        
    </head>
        <body>

        <header>
            <h1>Venues Page</h1>
        </header>

        <nav>
            <a href="/">Home</a>
        </nav>

        <div class="container">
            <div class="feature-box">
                <h2>Venues</h2>
                <p>View the list of venues.</p>
                <a href="/venues_summary">Go to Venue's</a>
            </div>
        </div>
        <!-- Add New Venue Form -->
        <div class="venue-form-container">
            <h2>Add New Venue</h2>
            <form action="/add_venue" method="post" class="venue-form">
                <div class="venue-form-group">
                    <label for="name">Venue Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                
                <div class="venue-form-group">
                    <label for="location">Location:</label>
                    <input type="text" id="location" name="location" required>
                </div>

                <div class="venue-form-group">
                    <label for="address">Address:</label>
                    <input type="text" id="address" name="address" required>
                </div>

                <div class="venue-form-group">
                    <label for="entrance_fee">Entrance Fee (0 for No, 1 for Yes):</label>
                    <input type="number" id="entrance_fee" name="entrance_fee" min="0" max="1" required>
                </div>

                <input type="submit" value="Add Venue" class="venue-form-submit">
            </form>
        </div>


        </body>
</html>