steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE question (
            id SERIAL PRIMARY KEY NOT NULL,
            category VARCHAR(1000) NOT NULL,
            type VARCHAR(1000) NOT NULL,
            difficulty VARCHAR(1000) NOT NULL,
            question VARCHAR(1000) NOT NULL,
            correct_answer VARCHAR(1000) NOT NULL,
            incorrect_answers VARCHAR(1000) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE question;
        """
    ]]
