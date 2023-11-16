steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            score INTEGER
        )
        """,
        # "Down" SQL statement
        """
        DROP TABLE question;
        """
    ]]
