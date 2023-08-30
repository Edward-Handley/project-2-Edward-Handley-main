<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fuel Watch Database</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header, footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1em;
        }
        header a, footer a {
            color: white;
            text-decoration: none;
        }
        .container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, p {
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<header>
    <p><a href="/">Return to Home Page</a></p>
</header>

<div class="container">
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
    <table>
        <tr>
            % for field in records[0].keys():
            <th>{{ field }}</th>
            % end
        </tr>
        % for record in records:
        <tr>
            % for field in record:
            <td>{{ field }}</td>
            % end
        </tr>
        % end
    </table>
</div>

<footer>
    <p><a href="/">Return to Home Page</a></p>
</footer>

</body>
</html>
