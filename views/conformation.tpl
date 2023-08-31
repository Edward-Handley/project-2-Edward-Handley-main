<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Confirmation</title>
    <link rel="stylesheet" href="/static/confirm.css">
</head>
<body>

<header>
    <p><a href="/">Return to Home Page</a></p>
</header>

<div class="container">
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>

    <!-- Tick Animation -->
    <div class="confirmation-container">
        <div class="tick stop"></div>
    </div>

    <a href="{{ return_url }}">Go Back</a>
</div>

<footer>
    <p><a href="/">Return to Home Page</a></p>
</footer>

</body>
</html>