<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1em;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
    <h1>{{title}}</h1>
</header>

<div class="container">
    <h2>{{description}}</h2>
    <table>
        <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Team Name</th>
        </tr>
        % for record in records:
        <tr>
            <td>{{record['first_name']}}</td>
            <td>{{record['last_name']}}</td>
            <td>{{record['team_name']}}</td>
        </tr>
        % end
    </table>
</div>

</body>
</html>
