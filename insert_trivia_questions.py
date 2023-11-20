import csv
from sqlalchem import create_engine

# Set your database connection parameters
DB_USERNAME = 'example_user'
DB_PASSWORD = 'secret'
DB_HOST = 'localhost'  # Use the host where your Docker is running
DB_PORT = '15432'      # The mapped port from your docker-compose.yaml
DB_NAME = 'postgres-trivia-data'

# Create a database connection using SQLAlchemy
db_url = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# Read the CSV file and insert data into the existing table
csv_file_path = 'trivia_questions.csv'
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row
    for row in csvreader:
        values = ", ".join([f"'{value}'" for value in row])
        query = f"INSERT INTO questions (id, category, type, difficulty, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3) VALUES ({values});"
        engine.execute(query)

# Close the database connection
engine.dispose()

print(f"Data from {csv_file_path} has been successfully inserted into your_existing_table_name.")
