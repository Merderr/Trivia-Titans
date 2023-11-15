steps = [
    """
    CREATE TABLE users (
    id SERIAL PRIMARY KEY NOT NULL
    name VARCHAR(1000) NOT NULL
    username VARCHAR(20) NOT NULL
    password VARCHAR(20) NOT NULL
    score INTEGER
    );
    """
    """
    DROP TABLE users;
    """
]
