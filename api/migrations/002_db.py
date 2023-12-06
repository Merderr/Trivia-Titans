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
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE IF EXISTS users;
        """,
    ],
    [
        # "Up" SQL statement
        """
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
        """,
        # "Down" SQL statement
        """
        DROP TABLE IF EXISTS question;
        """,
    ],
    [
        """
      INSERT INTO questions (
        category, type, difficulty, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3)
        VALUES
        ('Geography', 'multiple', 'easy', 'Which continent is known as the "Land Down Under"?', 'Australia', 'Africa', 'Asia', 'Europe'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of France?', 'Paris', 'Rome', 'Madrid', 'Berlin'),
        ('Geography', 'multiple', 'easy', 'Which river runs through Egypt?', 'Nile', 'Amazon', 'Yangtze', 'Mississippi'),
        ('Geography', 'multiple', 'easy', 'In which country is the Great Barrier Reef located?', 'Australia', 'Brazil', 'Mexico', 'India'),
        ('Geography', 'multiple', 'easy', 'What is the largest country in the world by land area?', 'Russia', 'China', 'United States', 'Canada'),
        ('Geography', 'multiple', 'easy', 'Which ocean is the largest on Earth?', 'Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is the Statue of Liberty located?', 'New York', 'California', 'Florida', 'Texas'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Japan?', 'Tokyo', 'Seoul', 'Beijing', 'Bangkok'),
        ('Geography', 'multiple', 'easy', 'Which mountain range is located in the western United States?', 'Rocky Mountains', 'Appalachian Mountains', 'Sierra Nevada', 'Cascade Range'),
        ('Geography', 'multiple', 'easy', 'In which continent is the Amazon Rainforest primarily located?', 'South America', 'Africa', 'Asia', 'North America'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Canada?', 'Ottawa', 'Toronto', 'Vancouver', 'Montreal'),
        ('Geography', 'multiple', 'easy', 'What is the longest river in the United States?', 'Mississippi River', 'Missouri River', 'Colorado River', 'Columbia River'),
        ('Geography', 'multiple', 'easy', 'In which European country is the city of Barcelona located?', 'Spain', 'Italy', 'France', 'Portugal'),
        ('Geography', 'multiple', 'easy', 'Which desert is located in North Africa?', 'Sahara Desert', 'Arabian Desert', 'Gobi Desert', 'Karakum Desert'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Mexico?', 'Mexico City', 'Cancun', 'Guadalajara', 'Monterrey'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is Yellowstone National Park located?', 'Wyoming', 'Montana', 'Idaho', 'Colorado'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Australia?', 'Canberra', 'Sydney', 'Melbourne', 'Brisbane'),
        ('Geography', 'multiple', 'easy', 'In which country is the city of Cape Town located?', 'South Africa', 'Kenya', 'Nigeria', 'Ghana'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is the Great Salt Lake located?', 'Utah', 'Nevada', 'Arizona', 'Colorado'),
        ('Geography', 'multiple', 'easy', 'In which Asian country is the city of Hanoi located?', 'Vietnam', 'Thailand', 'Cambodia', 'Malaysia'),
        ('Geography', 'multiple', 'easy', 'What is the largest island in the Caribbean?', 'Cuba', 'Jamaica', 'Hispaniola', 'Puerto Rico'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is the Everglades National Park located?', 'Florida', 'Louisiana', 'Georgia', 'Alabama'),
        ('Geography', 'multiple', 'easy', 'Which river is the longest in China?', 'Yangtze River', 'Yellow River', 'Mekong River', 'Indus River'),
        ('Geography', 'multiple', 'easy', 'In which European country is the city of Amsterdam located?', 'Netherlands', 'Belgium', 'Germany', 'France'),
        ('Geography', 'multiple', 'easy', 'Which mountain range separates Europe and Asia?', 'Ural Mountains', 'Caucasus Mountains', 'Carpathian Mountains', 'Alps'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is the Grand Teton National Park located?', 'Wyoming', 'Montana', 'Idaho', 'Colorado'),
        ('Geography', 'multiple', 'easy', 'Which river flows through Paris?', 'Seine', 'Rhine', 'Thames', 'Danube'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Cambodia?', 'Phnom Penh', 'Hanoi', 'Bangkok', 'Vientiane'),
        ('Geography', 'multiple', 'easy', 'In which African country can you find the Victoria Falls?', 'Zimbabwe', 'Zambia', 'Namibia', 'Botswana'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Colombia?', 'Bogota', 'Medellin', 'Cali', 'Cartagena'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Chile?', 'Santiago', 'Buenos Aires', 'Lima', 'Quito'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is the Zion National Park located?', 'Utah', 'Arizona', 'Nevada', 'Colorado'),
        ('Geography', 'multiple', 'easy', 'Which strait separates Greenland and Iceland?', 'Denmark Strait', 'Baffin Bay', 'Davis Strait', 'Norwegian Sea'),
        ('Geography', 'multiple', 'easy', 'In which continent is the Sahara Desert located?', 'Africa', 'Asia', 'South America', 'Australia'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is Mount Rushmore located?', 'South Dakota', 'North Dakota', 'Wyoming', 'Montana'),
        ('Geography', 'multiple', 'easy', 'Which sea is the largest landlocked body of water in the world?', 'Caspian Sea', 'Aral Sea', 'Dead Sea', 'Black Sea'),
        ('Geography', 'multiple', 'easy', 'In which European country is the city of Vienna located?', 'Austria', 'Switzerland', 'Czech Republic', 'Hungary'),
        ('Geography', 'multiple', 'easy', 'Which mountain range is located between Italy and the Balkans?', 'Dinaric Alps', 'Apennines', 'Carpathians', 'Balkan Mountains'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is the Great Basin Desert located?', 'Nevada', 'Utah', 'Arizona', 'California'),
        ('Geography', 'multiple', 'easy', 'In which continent is the Andes mountain range located?', 'South America', 'North America', 'Asia', 'Africa'),
        ('Geography', 'multiple', 'easy', 'Which island is the largest in the Mediterranean Sea?', 'Sicily', 'Sardinia', 'Corsica', 'Cyprus'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is the Horseshoe Bend located?', 'Arizona', 'Utah', 'Nevada', 'New Mexico'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Nigeria?', 'Abuja', 'Lagos', 'Kano', 'Ibadan'),
        ('Geography', 'multiple', 'easy', 'In which European country is the city of Prague located?', 'Czech Republic', 'Austria', 'Hungary', 'Poland'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Thailand?', 'Bangkok', 'Chiang Mai', 'Phuket', 'Pattaya'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Ireland?', 'Dublin', 'Belfast', 'Cork', 'Galway'),
        ('Geography', 'multiple', 'easy', 'In which African country is the city of Casablanca located?', 'Morocco', 'Algeria', 'Tunisia', 'Libya'),
        ('Geography', 'multiple', 'easy', 'Which strait separates Asia and North America at their closest point?', 'Bering Strait', 'Strait of Gibraltar', 'Strait of Hormuz', 'Davis Strait'),
        ('Geography', 'multiple', 'easy', 'What is the highest mountain in Japan?', 'Mount Fuji', 'Mount Tate', 'Mount Hotaka', 'Mount Norikura'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Malaysia?', 'Kuala Lumpur', 'Penang', 'Johor Bahru', 'Ipoh'),
        ('Geography', 'multiple', 'easy', 'In which European country is the city of Brussels located?', 'Belgium', 'Netherlands', 'France', 'Germany'),
        ('Geography', 'multiple', 'easy', 'Which sea is located between Greece and Turkey?', 'Aegean Sea', 'Mediterranean Sea', 'Ionian Sea', 'Adriatic Sea'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Hungary?', 'Budapest', 'Vienna', 'Prague', 'Bratislava'),
        ('Geography', 'multiple', 'easy', 'Which island group is known for its famous Komodo dragons?', 'Komodo Islands', 'Galápagos Islands', 'Mariana Islands', 'Andaman and Nicobar Islands'),
        ('Geography', 'multiple', 'easy', 'What is the largest lake in North America by surface area?', 'Lake Superior', 'Lake Michigan', 'Lake Huron', 'Lake Erie'),
        ('Geography', 'multiple', 'easy', 'In which African country is the city of Nairobi located?', 'Kenya', 'Tanzania', 'Uganda', 'Rwanda'),
        ('Geography', 'multiple', 'easy', 'Which river forms part of the border between the United States and Canada?', 'St. Lawrence River', 'Columbia River', 'Mississippi River', 'Ohio River'),
        ('Geography', 'multiple', 'easy', 'In which U.S. state is the Joshua Tree National Park located?', 'California', 'Arizona', 'Nevada', 'Utah'),
        ('Geography', 'multiple', 'easy', 'Which country is known as the "Land of the Rising Sun"?', 'Japan', 'China', 'Korea', 'Vietnam'),
        ('Geography', 'multiple', 'easy', 'In which country can you find the city of Marrakech?', 'Morocco', 'Algeria', 'Tunisia', 'Libya'),
        ('Geography', 'multiple', 'easy', 'What is the capital city of Finland?', 'Helsinki', 'Stockholm', 'Oslo', 'Copenhagen'),
        ('Geography', 'multiple', 'easy', 'Which strait separates Denmark and Sweden?', 'Øresund Strait', 'Skagerrak Strait', 'Kattegat Strait', 'English Channel');
        """
    ],
]
