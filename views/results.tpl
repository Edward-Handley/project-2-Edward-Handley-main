DOCTYPE html>
<html>
    <head>
        <title>Fuel Watch Database</title>
        <link type="text/css" href="/static/results_style.css" rel="stylesheet">
    </head>

    <body>
        <header>
            <p><a href="/">Return to Home Page</a></p>
        </header>

        <h1>{{ title }}</h1>
        <p>{{ description }}</p>

        <table>
            <tr>
                % for field in records[0].keys():
                <th> {{ field }} </th>
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

        <footer>
            <p><a href="/">Return to Home Page</a></p>
        </footer>
    </body>
</html>