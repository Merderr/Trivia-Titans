query = [
    """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            name TEXT,
            score INTEGER
        )
    """
]
