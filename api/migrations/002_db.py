steps = [
    [
        # "Up" SQL statement
        """
        DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'users') THEN
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            score INTEGER
        );
    END IF;
END $$;
        """,
        # "Down" SQL statement
        """
        DROP TABLE IF EXISTS users;
        """,
    ],
    [
        # "Up" SQL statement
        """
        DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'questions') THEN
        CREATE TABLE questions (
          id SERIAL PRIMARY KEY,
          category VARCHAR(1000) NOT NULL,
          type VARCHAR(1000) NOT NULL,
          difficulty VARCHAR(1000) NOT NULL,
          question VARCHAR(1000) NOT NULL,
          correct_answer VARCHAR(1000) NOT NULL,
          incorrect_answer_1 VARCHAR(1000) NOT NULL,
          incorrect_answer_2 VARCHAR(1000) NOT NULL,
          incorrect_answer_3 VARCHAR(1000) NOT NULL
        );
            END IF;
END $$;
        """,
        # "Down" SQL statement
        """
        DROP TABLE IF EXISTS questions;
        """,
    ],
]
