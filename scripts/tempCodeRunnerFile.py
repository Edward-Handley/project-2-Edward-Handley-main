            CREATE TABLE IF NOT EXISTS Sponsors (
                sponsor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                contribution_amount REAL NOT NULL
            );
            '''