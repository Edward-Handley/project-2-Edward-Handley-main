<h1>{{title}}</h1>
<p>{{description}}</p>
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
