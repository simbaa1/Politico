


tables = [
    """
    CREATE TABLE IF NOT EXISTS user(
            id INT NOT NULL SERIAL PRIMARY KEY,
            firstname VARCHAR(200) NOT NULL,
            lastname VARCHAR(200) NOT NULL,
            othername VARCHAR(200),
            email VARCHAR(50) NOT NULL,
            phonenumber VARCHAR(15),
            idnumber VARCHAR(15),
            passportUrl VARCHAR(100),
            isAdmin BOOLEAN DEFAULT FALSE,
            UNIQUE(email, phonenumber)
           );
        """,

        """
           CREATE TABLE IF NOT EXISTS party(
            id INT NOT NULL SERIAL PRIMARY KEY,
            name VARCHAR(200),
            hqAddress VARCHAR(100),
            logoUrl VARCHAR(100),
            UNIQUE(name)
           );
        """,

        """
           CREATE TABLE IF NOT EXISTS office(
            id INT NOT NULL SERIAL PRIMARY KEY,
            type VARCHAR(100) NOT NULL,
            name VARCHAR(100) NOT NULL,
            UNIQUE(name)
           );
        """,

        """
           CREATE TABLE IF NOT EXISTS candidates(
            id SERIAL PRIMARY KEY,
            office INT NOT NULL,
            party  INT NOT NULL,
            candidate INT NOT NULL,
            PRIMARY KEY(id, candidate, office),
            FOREIGN KEY (candidate) REFERENCES user(id) ON DELETE CASCADE,
            FOREIGN KEY (party) REFERENCES party(id) ON DELETE CASCADE,
            FOREIGN KEY (office) REFERENCES office(id) ON DELETE CASCADE            
           );
        """,
        """
           CREATE TABLE IF NOT EXISTS vote(
            id SERIAL INT NOT NULL,
            createdOn DEFAULT CURRENT_TIMESTAMP,
            createdBy VARCHAR(200),
            office INT NOT NULL REFERENCES office(id),
            candidate INT NOT NULL REFERENCES candidate(id)
            voter  INT NOT NULL,
            PRIMARY KEY(id, voter, office),
            FOREIGN KEY (voter) REFERENCES user(id) ON DELETE CASCADE,
            FOREIGN KEY (office) REFERENCES office(id) ON DELETE CASCADE
            FOREIGN KEY (candidate) REFERENCES candidate(id) ON DELETE CASCADE
           );
        """
]


table_names = [
   'user',
   'party',
   'office',
   'candidates',
   'vote'
]