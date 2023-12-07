from queries.pool import pool
from pydantic import BaseModel
from typing import Optional, List, Union


class Error(BaseModel):
    message: str


class QuestionModelIn(BaseModel):
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answer_1: str
    incorrect_answer_2: str
    incorrect_answer_3: str

    class Config:
        orm_mode = True


class QuestionModelOut(BaseModel):
    id: int
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answer_1: str
    incorrect_answer_2: str
    incorrect_answer_3: str

    class Config:
        orm_mode = True


class QuestionRepository:
    def get_one_question(self, question_id: int) -> Optional[QuestionModelOut]:
        try:
            # connect to the database
            with pool.connection() as conn:
                # get a named cursor (something to run SQL with)
                with conn.cursor(name="get_one_cursor") as db:
                    # Run our SELECT statement
                    db.execute(
                        """
                        SELECT id, category, type, difficulty, question,
                        correct_answer, incorrect_answer_1, incorrect_answer_2,
                        incorrect_answer_3
                        FROM questions
                        WHERE id = %s
                        """,
                        [question_id],
                    )
                    record = db.fetchone()
                    if record is None:
                        return None
                    print(record)
                    return self.record_to_question_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that question"}

    def get_questions(self) -> Union[Error, List[QuestionModelOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, category, type, difficulty, question,
                        correct_answer, incorrect_answer_1, incorrect_answer_2,
                        incorrect_answer_3
                        FROM questions
                        ORDER BY category;
                        """
                    )
                    result_list = []
                    for record in result:
                        question = QuestionModelOut(
                            id=record[0],
                            category=record[1],
                            type=record[2],
                            difficulty=record[3],
                            question=record[4],
                            correct_answer=record[5],
                            incorrect_answer_1=record[6],
                            incorrect_answer_2=record[7],
                            incorrect_answer_3=record[8],
                        )
                        result_list.append(question)
                    return result_list
        except Exception as e:
            print(e)
            return {"message": "Could not get questions"}

    def create_all(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO questions (category, type, difficulty, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3)
                    VALUES ('Geography', 'multiple', 'easy', 'What is the capital city of France?', 'Paris', 'Rome', 'Madrid', 'Berlin'),
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
                    ('Geography', 'multiple', 'easy', 'Which strait separates Denmark and Sweden?', 'Øresund Strait', 'Skagerrak Strait', 'Kattegat Strait', 'English Channel'),
                    ('Geography', 'multiple', 'medium', 'Which river is the longest in the world?', 'Nile', 'Amazon', 'Yangtze', 'Mississippi'),
                    ('Geography', 'multiple', 'medium', 'Which mountain range is the longest in the world?', 'Andes', 'Himalayas', 'Rockies', 'Alps'),
                    ('Geography', 'multiple', 'medium', 'What is the largest desert in the world?', 'Antarctica', 'Sahara', 'Arabian', 'Gobi'),
                    ('Geography', 'multiple', 'medium', 'Which continent is known as the "Land of the Rising Sun"?', 'Asia', 'Africa', 'Europe', 'Australia'),
                    ('Geography', 'multiple', 'medium', 'Which country is known as the "Land of the Midnight Sun"?', 'Norway', 'Canada', 'Russia', 'Sweden'),
                    ('Geography', 'multiple', 'medium', 'In which continent is the Amazon Rainforest located?', 'South America', 'Africa', 'Asia', 'North America'),
                    ('Geography', 'multiple', 'medium', 'What is the smallest country in the world?', 'Vatican City', 'Monaco', 'San Marino', 'Nauru'),
                    ('Geography', 'multiple', 'medium', 'Which two European countries are separated by the Pyrenees Mountains?', 'Spain and France', 'Italy and Switzerland', 'Austria and Germany', 'Norway and Sweden'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of South Africa?', 'Pretoria', 'Cape Town', 'Johannesburg', 'Durban'),
                    ('Geography', 'multiple', 'medium', 'Which sea is bordered by Italy, Croatia, and Greece?', 'Adriatic Sea', 'Mediterranean Sea', 'Ionian Sea', 'Aegean Sea'),
                    ('Geography', 'multiple', 'medium', 'In which country can you find the ancient city of Petra?', 'Jordan', 'Egypt', 'Iraq', 'Lebanon'),
                    ('Geography', 'multiple', 'medium', 'What is the highest mountain in North America?', 'Denali (Mount McKinley)', 'Mount Rainier', 'Mount St. Elias', 'Mount Logan'),
                    ('Geography', 'multiple', 'medium', 'Which river is known as the "Cradle of Civilization"?', 'Tigris and Euphrates', 'Indus', 'Nile', 'Yellow River'),
                    ('Geography', 'multiple', 'medium', 'In which continent is the Serengeti National Park located?', 'Africa', 'Asia', 'South America', 'Australia'),
                    ('Geography', 'multiple', 'medium', 'Which European city is known as the "City of Canals"?', 'Venice', 'Amsterdam', 'Copenhagen', 'Bruges'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Argentina?', 'Buenos Aires', 'Rio de Janeiro', 'Lima', 'Santiago'),
                    ('Geography', 'multiple', 'medium', 'Which African country is known as the "Pearl of Africa"?', 'Uganda', 'Kenya', 'Tanzania', 'Rwanda'),
                    ('Geography', 'multiple', 'medium', 'What is the largest lake in Africa?', 'Lake Victoria', 'Lake Tanganyika', 'Lake Malawi', 'Lake Chad'),
                    ('Geography', 'multiple', 'medium', 'In which country is the city of Istanbul located?', 'Turkey', 'Greece', 'Bulgaria', 'Romania'),
                    ('Geography', 'multiple', 'medium', 'Which desert is often called the "Roof of the World"?', 'Tibetan Plateau', 'Gobi Desert', 'Karakum Desert', 'Dasht-e Kavir'),
                    ('Geography', 'multiple', 'medium', 'Which river is the boundary between the United States and Mexico?', 'Rio Grande', 'Colorado River', 'Mississippi River', 'Columbia River'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of New Zealand?', 'Wellington', 'Auckland', 'Christchurch', 'Hamilton'),
                    ('Geography', 'multiple', 'medium', 'Which ocean is the smallest in the world?', 'Arctic Ocean', 'Southern Ocean', 'Indian Ocean', 'Atlantic Ocean'),
                    ('Geography', 'multiple', 'medium', 'In which country is the city of Marrakech located?', 'Morocco', 'Tunisia', 'Algeria', 'Libya'),
                    ('Geography', 'multiple', 'medium', 'In which country can you find the city of Cusco, the former capital of the Inca Empire?', 'Peru', 'Ecuador', 'Bolivia', 'Colombia'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Saudi Arabia?', 'Riyadh', 'Jeddah', 'Mecca', 'Medina'),
                    ('Geography', 'multiple', 'medium', 'Which African country is known as the "Giant of Africa"?', 'Nigeria', 'South Africa', 'Ethiopia', 'Kenya'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Sweden?', 'Stockholm', 'Oslo', 'Copenhagen', 'Helsinki'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Egypt?', 'Cairo', 'Alexandria', 'Luxor', 'Aswan'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Spain?', 'Madrid', 'Barcelona', 'Seville', 'Valencia'),
                    ('Geography', 'multiple', 'medium', 'Which two countries are connected by the Channel Tunnel?', 'France and the United Kingdom', 'Germany and Austria', 'Italy and Switzerland', 'Spain and Portugal'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of India?', 'New Delhi', 'Mumbai', 'Kolkata', 'Chennai'),
                    ('Geography', 'multiple', 'medium', 'In which U.S. state is the Great Smoky Mountains National Park located?', 'Tennessee', 'North Carolina', 'Georgia', 'Kentucky'),
                    ('Geography', 'multiple', 'medium', 'Which desert is located in the southwestern United States?', 'Sonoran Desert', 'Mojave Desert', 'Great Basin Desert', 'Chihuahuan Desert'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of South Korea?', 'Seoul', 'Busan', 'Incheon', 'Daegu'),
                    ('Geography', 'multiple', 'medium', 'Which lake is the deepest in the world?', 'Lake Baikal', 'Lake Superior', 'Lake Victoria', 'The Aral Sea'),
                    ('Geography', 'multiple', 'medium', 'In which country can you find the ancient city of Machu Picchu?', 'Peru', 'Ecuador', 'Bolivia', 'Colombia'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Iran?', 'Tehran', 'Baghdad', 'Ankara', 'Riyadh'),
                    ('Geography', 'multiple', 'medium', 'Which river runs through the Grand Canyon?', 'Colorado River', 'Mississippi River', 'Columbia River', 'Rio Grande'),
                    ('Geography', 'multiple', 'medium', 'In which country can you find the city of Budapest?', 'Hungary', 'Austria', 'Czech Republic', 'Slovakia'),
                    ('Geography', 'multiple', 'medium', 'What is the smallest ocean in the world?', 'Arctic Ocean', 'Southern Ocean', 'Indian Ocean', 'Atlantic Ocean'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Peru?', 'Lima', 'Bogota', 'Quito', 'Caracas'),
                    ('Geography', 'multiple', 'medium', 'Which mountain range separates Europe from Asia?', 'Ural Mountains', 'Carpathian Mountains', 'Caucasus Mountains', 'Alps'),
                    ('Geography', 'multiple', 'medium', 'In which African country can you find Mount Kilimanjaro?', 'Tanzania', 'Kenya', 'Uganda', 'Rwanda'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Portugal?', 'Lisbon', 'Madrid', 'Barcelona', 'Seville'),
                    ('Geography', 'multiple', 'medium', 'In which U.S. state is the Denali National Park and Preserve located?', 'Alaska', 'Washington', 'Oregon', 'Montana'),
                    ('Geography', 'multiple', 'medium', 'Which country is known as the "Land of Fire and Ice"?', 'Iceland', 'Greenland', 'Norway', 'New Zealand'),
                    ('Geography', 'multiple', 'medium', 'In which country can you find the city of Casablanca?', 'Morocco', 'Algeria', 'Tunisia', 'Libya'),
                    ('Geography', 'multiple', 'medium', 'Which sea is bordered by Italy, Croatia, and Albania?', 'Adriatic Sea', 'Mediterranean Sea', 'Ionian Sea', 'Aegean Sea'),
                    ('Geography', 'multiple', 'medium', 'In which continent is the Kalahari Desert located?', 'Africa', 'Australia', 'South America', 'Asia'),
                    ('Geography', 'multiple', 'medium', 'Which two countries are connected by the Suez Canal?', 'Egypt and Israel', 'Saudi Arabia and Jordan', 'Turkey and Greece', 'Morocco and Spain'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Switzerland?', 'Bern', 'Zurich', 'Geneva', 'Basel'),
                    ('Geography', 'multiple', 'medium', 'In which U.S. state is the Redwood National and State Parks located?', 'California', 'Oregon', 'Washington', 'Alaska'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of Kenya?', 'Nairobi', 'Dar es Salaam', 'Kampala', 'Addis Ababa'),
                    ('Geography', 'multiple', 'medium', 'In which country can you find the city of Auckland?', 'New Zealand', 'Australia', 'Fiji', 'Papua New Guinea'),
                    ('Geography', 'multiple', 'medium', 'Which country is known as the "Land of a Thousand Lakes"?', 'Finland', 'Sweden', 'Norway', 'Canada'),
                    ('Geography', 'multiple', 'medium', 'In which U.S. state is the Rocky Mountain National Park located?', 'Colorado', 'Montana', 'Wyoming', 'New Mexico'),
                    ('Geography', 'multiple', 'medium', 'Which African country is known as the "Rainbow Nation"?', 'South Africa', 'Kenya', 'Nigeria', 'Ghana'),
                    ('Geography', 'multiple', 'medium', 'Which lake is located on the border of the United States and Canada?', 'Lake Superior', 'Lake Michigan', 'Lake Huron', 'Lake Erie'),
                    ('Geography', 'multiple', 'medium', 'What is the capital city of the Philippines?', 'Manila', 'Cebu', 'Davao', 'Quezon City'),
                    ('Geography', 'multiple', 'medium', 'In which U.S. state is the Great Basin National Park located?', 'Nevada', 'Utah', 'Idaho', 'Wyoming'),
                    ('Geography', 'multiple', 'hard', 'In which mountain range is K2, the second-highest mountain in the world?', 'Himalayas', 'Andes', 'Karakoram Range', 'Rockies'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Bhutan?', 'Thimphu', 'Paro', 'Punakha', 'Jakar'),
                    ('Geography', 'multiple', 'hard', 'In which country can you find the Atacama Desert?', 'Chile', 'Peru', 'Argentina', 'Bolivia'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Great Dismal Swamp located?', 'Virginia', 'North Carolina', 'Maryland', 'Delaware'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Suriname?', 'Paramaribo', 'Georgetown', 'Cayenne', 'Port of Spain'),
                    ('Geography', 'multiple', 'hard', 'Which strait separates Greenland and Canada?', 'Davis Strait', 'Baffin Bay', 'Hudson Strait', 'Labrador Strait'),
                    ('Geography', 'multiple', 'hard', 'In which African country is the Nubian Desert located?', 'Sudan', 'Egypt', 'Chad', 'Libya'),
                    ('Geography', 'multiple', 'hard', 'What is the highest mountain in South America?', 'Aconcagua', 'Huascaran', 'Fitz Roy', 'Monte Pissis'),
                    ('Geography', 'multiple', 'hard', 'In which country can you find the Tien Shan mountain range?', 'Kyrgyzstan', 'Tajikistan', 'Kazakhstan', 'Uzbekistan'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Mozambique?', 'Maputo', 'Nairobi', 'Lusaka', 'Harare'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Gates of the Arctic National Park and Preserve located?', 'Alaska', 'Washington', 'Montana', 'Idaho'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Uzbekistan?', 'Tashkent', 'Samarkand', 'Bukhara', 'Andijan'),
                    ('Geography', 'multiple', 'hard', 'Which lake is the largest in Africa by surface area?', 'Lake Victoria', 'Lake Tanganyika', 'Lake Malawi', 'Lake Turkana'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Papua New Guinea?', 'Port Moresby', 'Suva', 'Honiara', 'Nukualofa'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Lebanon?', 'Beirut', 'Damascus', 'Amman', 'Tel Aviv'),
                    ('Geography', 'multiple', 'hard', 'Which strait separates Russia and Alaska?', 'Bering Strait', 'Chukchi Strait', 'Luzon Strait', 'Korea Strait'),
                    ('Geography', 'multiple', 'hard', 'In which country can you find the city of Addis Ababa?', 'Ethiopia', 'Kenya', 'Uganda', 'Somalia'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Laos?', 'Vientiane', 'Luang Prabang', 'Pakse', 'Savannakhet'),
                    ('Geography', 'multiple', 'hard', 'Which island group is known as the "Islands of the Four Mountains"?', 'Aleutian Islands', 'Hawaiian Islands', 'Galápagos Islands', 'Marquesas Islands'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Myanmar?', 'Naypyidaw', 'Yangon', 'Mandalay', 'Bagan'),
                    ('Geography', 'multiple', 'hard', 'In which country can you find the city of Ulaanbaatar?', 'Mongolia', 'China', 'Russia', 'Kazakhstan'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Bangladesh?', 'Dhaka', 'Chittagong', 'Khulna', 'Rajshahi'),
                    ('Geography', 'multiple', 'hard', 'Which lake is the largest in Central America?', 'Lake Nicaragua', 'Lake Managua', 'Lake Izabal', 'Lake Atitlan'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Petrified Forest National Park located?', 'Arizona', 'New Mexico', 'Texas', 'Utah'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Nepal?', 'Kathmandu', 'Pokhara', 'Lalitpur', 'Bhaktapur'),
                    ('Geography', 'multiple', 'hard', 'In which African country is the Ennedi Plateau located?', 'Chad', 'Niger', 'Mali', 'Sudan'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Belarus?', 'Minsk', 'Vilnius', 'Riga', 'Tallinn'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Sudan?', 'Khartoum', 'Omdurman', 'Port Sudan', 'Nyala'),
                    ('Geography', 'multiple', 'hard', 'Which island group is known as the "Land of the Long White Cloud"?', 'New Zealand', 'Fiji', 'Tonga', 'Samoa'),
                    ('Geography', 'multiple', 'hard', 'In which country can you find the city of Timbuktu?', 'Mali', 'Niger', 'Burkina Faso', 'Senegal'),
                    ('Geography', 'multiple', 'hard', 'What is the capital city of Slovenia?', 'Ljubljana', 'Zagreb', 'Belgrade', 'Sarajevo'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Arches National Park located?', 'Utah', 'Arizona', 'Colorado', 'New Mexico'),
                    ('Geography', 'multiple', 'hard', 'Which mountain range is often called the "Backbone of the World"?', 'The Himalayas', 'The Andes', 'The Rockies', 'The Alps'),
                    ('Geography', 'multiple', 'hard', 'In which African country is the Great Rift Valley located?', 'Kenya', 'Ethiopia', 'Tanzania', 'Uganda'),
                    ('Geography', 'multiple', 'hard', 'What is the highest mountain in Africa?', 'Mount Kilimanjaro', 'Mount Kenya', 'Ras Dashen', 'Simien Mountains'),
                    ('Geography', 'multiple', 'hard', 'In which country can you find the Karakoram Highway, one of the highest paved international roads?', 'Pakistan', 'India', 'China', 'Afghanistan'),
                    ('Geography', 'multiple', 'hard', 'Which island group is known for its famous giant tortoises?', 'Galápagos Islands', 'Hawaiian Islands', 'Maldives', 'Andaman and Nicobar Islands'),
                    ('Geography', 'multiple', 'hard', 'What is the deepest point in the Atlantic Ocean?', 'Puerto Rico Trench', 'Mariana Trench', 'Sargasso Sea', 'Mid-Atlantic Ridge'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Crater Lake National Park located?', 'Oregon', 'Washington', 'California', 'Idaho'),
                    ('Geography', 'multiple', 'hard', 'Which desert is the largest in Asia?', 'Gobi Desert', 'Karakum Desert', 'Taklamakan Desert', 'Thar Desert'),
                    ('Geography', 'multiple', 'hard', 'In which African country is the Kalahari Desert located?', 'Botswana', 'Namibia', 'South Africa', 'Angola'),
                    ('Geography', 'multiple', 'hard', 'What is the highest mountain in Oceania?', 'Puncak Jaya (Carstensz Pyramid)', 'Mount Wilhelm', 'Mount Cook', 'Mauna Kea'),
                    ('Geography', 'multiple', 'hard', 'Which lake is the largest in Central Asia?', 'Caspian Sea', 'Aral Sea', 'Lake Balkhash', 'Issyk-Kul'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Bryce Canyon National Park located?', 'Utah', 'Arizona', 'Colorado', 'Nevada'),
                    ('Geography', 'multiple', 'hard', 'Which strait separates Spain and Morocco?', 'Strait of Gibraltar', 'Strait of Hormuz', 'Bosphorus Strait', 'Davis Strait'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Glacier National Park located?', 'Montana', 'Wyoming', 'Idaho', 'Washington'),
                    ('Geography', 'multiple', 'hard', 'Which island is the easternmost point in the Caribbean Sea?', 'Barbados', 'Saint Kitts', 'Trinidad', 'Antigua'),
                    ('Geography', 'multiple', 'hard', 'What is the highest mountain in the Southern Hemisphere?', 'Mount Aconcagua', 'Mount Kilimanjaro', 'Mount Vinson', 'Puncak Jaya'),
                    ('Geography', 'multiple', 'hard', 'In which African country is the Namib Desert located?', 'Namibia', 'Botswana', 'South Africa', 'Angola'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Great Sand Dunes National Park and Preserve located?', 'Colorado', 'New Mexico', 'Arizona', 'Utah'),
                    ('Geography', 'multiple', 'hard', 'Which mountain range separates Spain and France?', 'Pyrenees', 'Alps', 'Apennines', 'Cantabrian Mountains'),
                    ('Geography', 'multiple', 'hard', 'What is the highest mountain in the Caribbean?', 'Pico Duarte', 'Blue Mountain', 'La Grande Soufrière', 'El Toro'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Shenandoah National Park located?', 'Virginia', 'West Virginia', 'Maryland', 'North Carolina'),
                    ('Geography', 'multiple', 'hard', 'Which island group is known for its "Moa" birds, now extinct?', 'New Zealand', 'Fiji', 'Hawaiian Islands', 'Galápagos Islands'),
                    ('Geography', 'multiple', 'hard', 'What is the highest peak in the Caucasus mountain range?', 'Mount Elbrus', 'Mount Kazbek', 'Dychtau', 'Shkhara'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Black Canyon of the Gunnison National Park located?', 'Colorado', 'Utah', 'Arizona', 'New Mexico'),
                    ('Geography', 'multiple', 'hard', 'What is the largest island in the Baltic Sea?', 'Gotland', 'Saaremaa', 'Bornholm', 'Hiiumaa'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Guadalupe Mountains National Park located?', 'Texas', 'New Mexico', 'Arizona', 'Oklahoma'),
                    ('Geography', 'multiple', 'hard', 'What is the highest mountain in the Scandinavian mountain range?', 'Galdhøpiggen', 'Kebnekaise', 'Snøhetta', 'Sarektjåkkå'),
                    ('Geography', 'multiple', 'hard', 'Which sea is the largest marginal sea of the Atlantic Ocean?', 'Mediterranean Sea', 'Caribbean Sea', 'Baltic Sea', 'North Sea'),
                    ('Geography', 'multiple', 'hard', 'In which African country is the Rwenzori mountain range located?', 'Uganda', 'Democratic Republic of the Congo', 'Rwanda', 'Tanzania'),
                    ('Geography', 'multiple', 'hard', 'What is the highest peak in the Ural Mountains?', 'Mount Narodnaya', 'Mount Yamantau', 'Mount Karpinsky', 'Mount Kachkanar'),
                    ('Geography', 'multiple', 'hard', 'In which U.S. state is the Badlands National Park located?', 'South Dakota', 'North Dakota', 'Wyoming', 'Montana'),
                    ('History', 'multiple', 'easy', 'Who was the first Emperor of the Roman Empire?', 'Augustus', 'Julius Caesar', 'Tiberius', 'Nero'),
                    ('History', 'multiple', 'easy', 'In which year did the Battle of Gettysburg take place during the American Civil War?', '1863', '1858', '1871', '1885'),
                    ('History', 'multiple', 'easy', 'Who was the famous nurse known for her work during the Crimean War?', 'Florence Nightingale', 'Clara Barton', 'Mary Seacole', 'Dorothea Dix'),
                    ('History', 'multiple', 'easy', 'Which ancient civilization is known for its contributions to philosophy, democracy, and theater?', 'Ancient Greece', 'Ancient Rome', 'Ancient Egypt', 'Mesopotamia'),
                    ('History', 'multiple', 'easy', 'In which year did the Wright brothers make their first powered, controlled, and sustained flight?', '1903', '1899', '1910', '1922'),
                    ('History', 'multiple', 'easy', 'Who was the leader of the Allied forces during World War II?', 'Dwight D. Eisenhower', 'Winston Churchill', 'Joseph Stalin', 'Charles de Gaulle'),
                    ('History', 'multiple', 'easy', 'Which U.S. president is known for the Louisiana Purchase?', 'Thomas Jefferson', 'James Madison', 'James Monroe', 'John Adams'),
                    ('History', 'multiple', 'easy', 'In which year did the Berlin Wall fall, symbolizing the end of the Cold War?', '1989', '1991', '1985', '1993'),
                    ('History', 'multiple', 'easy', 'Who was the first woman to become Prime Minister of the United Kingdom?', 'Margaret Thatcher', 'Indira Gandhi', 'Angela Merkel', 'Theresa May'),
                    ('History', 'multiple', 'easy', 'Which ancient civilization is known for constructing the Great Wall?', 'Ancient China', 'Ancient India', 'Ancient Persia', 'Ancient Babylon'),
                    ('History', 'multiple', 'easy', 'In which year did the Apollo 11 mission successfully land humans on the moon?', '1969', '1971', '1965', '1973'),
                    ('History', 'multiple', 'easy', 'Who was the primary author of the Declaration of Independence?', 'Thomas Jefferson', 'John Adams', 'Benjamin Franklin', 'George Washington'),
                    ('History', 'multiple', 'easy', 'What treaty officially ended World War I?', 'Treaty of Versailles', 'Treaty of Brest-Litovsk', 'Treaty of Trianon', 'Treaty of Saint-Germain-en-Laye'),
                    ('History', 'multiple', 'easy', 'Who was the famous leader of the civil rights movement in the United States?', 'Martin Luther King Jr.', 'Malcolm X', 'Rosa Parks', 'Harriet Tubman'),
                    ('History', 'multiple', 'easy', 'In which year did the Boston Tea Party take place?', '1773', '1765', '1781', '1790'),
                    ('History', 'multiple', 'easy', 'Who was the first woman to win a Nobel Prize?', 'Marie Curie', 'Rosa Parks', 'Amelia Earhart', 'Jane Addams'),
                    ('History', 'multiple', 'easy', 'In which year did the Industrial Revolution begin?', '18th century', '19th century', '17th century', '20th century'),
                    ('History', 'multiple', 'easy', 'Who was the leader of the Soviet Union during the Cuban Missile Crisis?', 'Nikita Khrushchev', 'Joseph Stalin', 'Leon Trotsky', 'Vladimir Lenin'),
                    ('History', 'multiple', 'easy', 'What was the main cause of the French Revolution?', 'Social Inequality', 'Economic Crisis', 'Political Corruption', 'Religious Conflict'),
                    ('History', 'multiple', 'easy', 'Who is known for the theory of evolution by natural selection?', 'Charles Darwin', 'Gregor Mendel', 'Alfred Russel Wallace', 'Thomas Huxley'),
                    ('History', 'multiple', 'easy', 'Which queen of ancient Egypt is known for her relationships with Julius Caesar and Mark Antony?', 'Cleopatra', 'Nefertiti', 'Hatshepsut', 'Isis'),
                    ('History', 'multiple', 'easy', 'Who was the first woman to fly solo across the Atlantic Ocean?', 'Amelia Earhart', 'Bessie Coleman', 'Harriet Quimby', 'Jacqueline Cochran'),
                    ('History', 'multiple', 'easy', 'In which year did the United States declare its independence from Great Britain?', '1776', '1789', '1799', '1765'),
                    ('History', 'multiple', 'easy', 'Who was the founder of the Mongol Empire?', 'Genghis Khan', 'Kublai Khan', 'Attila the Hun', 'Timur'),
                    ('History', 'multiple', 'easy', 'Which Roman emperor is known for "crossing the Rubicon"?', 'Julius Caesar', 'Augustus', 'Nero', 'Caligula'),
                    ('History', 'multiple', 'easy', 'Who wrote the "Iliad" and the "Odyssey"?', 'Homer', 'Virgil', 'Sophocles', 'Aristophanes'),
                    ('History', 'multiple', 'easy', 'What ancient civilization built the city of Machu Picchu?', 'Inca Empire', 'Aztec Empire', 'Maya Civilization', 'Olmec Civilization'),
                    ('History', 'multiple', 'easy', 'Who was the first President of the United States?', 'George Washington', 'Thomas Jefferson', 'John Adams', 'James Madison'),
                    ('History', 'multiple', 'easy', 'What event marked the beginning of World War I?', 'Assassination of Archduke Franz Ferdinand', 'Battle of the Somme', 'Treaty of Versailles', 'Russian Revolution'),
                    ('History', 'multiple', 'easy', 'What year did World War II end?', '1945', '1944', '1946', '1943'),
                    ('History', 'multiple', 'easy', 'Who was the first man to walk on the moon?', 'Neil Armstrong', 'Buzz Aldrin', 'Michael Collins', 'Yuri Gagarin'),
                    ('History', 'multiple', 'easy', 'In what year was the Declaration of Independence signed?', '1776', '1775', '1777', '1774'),
                    ('History', 'multiple', 'easy', 'Who was the British monarch during the American Revolution?', 'King George III', 'Queen Victoria', 'King George II', 'Queen Elizabeth I'),
                    ('History', 'multiple', 'easy', 'What was the name of the first ship that brought the Pilgrims to America?', 'Mayflower', 'Santa Maria', 'Pinta', 'Nina'),
                    ('History', 'multiple', 'easy', 'What was the name of the last queen of France?', 'Marie Antoinette', 'Catherine de Medici', 'Anne of Austria', 'Mary Stuart'),
                    ('History', 'multiple', 'easy', 'Who was the Roman god of war?', 'Mars', 'Jupiter', 'Neptune', 'Pluto'),
                    ('History', 'multiple', 'easy', 'What was the name of the first satellite launched into space?', 'Sputnik 1', 'Apollo 11', 'Voyager 1', 'Hubble Space Telescope'),
                    ('History', 'multiple', 'easy', 'Who was the first African American to serve as the U.S. Secretary of State?', 'Colin Powell', 'Condoleezza Rice', 'Madeleine Albright', 'Hillary Clinton'),
                    ('History', 'multiple', 'easy', 'What was the name of the first successful vaccine developed in history?', 'Smallpox', 'Polio', 'Measles', 'Tuberculosis'),
                    ('History', 'multiple', 'easy', 'What was the name of Martin Luther King Jr.s famous speech delivered during the March on Washington?', 'I Have a Dream', 'Letter from Birmingham Jail', 'Beyond Vietnam', 'The Other America'),
                    ('History', 'multiple', 'easy', 'Who was the first emperor of Rome?', 'Augustus', 'Julius Caesar', 'Nero', 'Marcus Aurelius'),
                    ('History', 'multiple', 'easy', 'What was the name of the plane that dropped the first atomic bomb?', 'Enola Gay', 'Bockscar', 'Little Boy', 'Fat Man'),
                    ('History', 'multiple', 'easy', 'Who was the first person to reach the South Pole?', 'Roald Amundsen', 'Robert Falcon Scott', 'Ernest Shackleton', 'Edmund Hillary'),
                    ('History', 'multiple', 'easy', 'What was the name of the peace treaty that ended World War I?', 'Treaty of Versailles', 'Treaty of Tordesillas', 'Treaty of Paris', 'Treaty of Westphalia'),
                    ('History', 'multiple', 'easy', 'Who was the first African American to win the Nobel Peace Prize?', 'Ralph Bunche', 'Martin Luther King Jr.', 'Barack Obama', 'Malcolm X'),
                    ('History', 'multiple', 'easy', 'What was the name of the first dog in space?', 'Laika', 'Belka', 'Strelka', 'Yuri'),
                    ('History', 'multiple', 'easy', 'What was the name of the first cloned sheep?', 'Dolly', 'Molly', 'Polly', 'Holly'),
                    ('History', 'multiple', 'easy', 'Who was the first African American to play in Major League Baseball?', 'Jackie Robinson', 'Hank Aaron', 'Willie Mays', 'Babe Ruth'),
                    ('History', 'multiple', 'easy', 'What was the name of the first successful printing press?', 'Gutenberg Press', 'Aldine Press', 'Caxton Press', 'Kelmscott Press'),
                    ('History', 'multiple', 'easy', 'What was the name of the first man-made satellite to orbit the Earth?', 'Sputnik 1', 'Explorer 1', 'Apollo 11', 'Voyager 1'),
                    ('History', 'multiple', 'easy', 'Who was the first African American to serve on the Supreme Court of the United States?', 'Thurgood Marshall', 'Clarence Thomas', 'Ruth Bader Ginsburg', 'Sonia Sotomayor'),
                    ('History', 'multiple', 'easy', 'What was the name of the first vaccine developed in history?', 'Smallpox', 'Polio', 'Measles', 'Tuberculosis'), ('History', 'multiple', 'difficult', 'Who was the first European explorer to reach India by sea?', 'Vasco da Gama', 'Christopher Columbus', 'Ferdinand Magellan', 'John Cabot'),
                    ('History', 'multiple', 'difficult', 'What year did the Spanish Civil War occur?', '1936-1939', '1914-1918', '1939-1945', '1886-1889'),
                    ('History', 'multiple', 'difficult', 'Which ancient civilization invented the wheel?', 'Sumerians', 'Egyptians', 'Romans', 'Greeks'),
                    ('History', 'multiple', 'difficult', 'Who was the first female Prime Minister of Australia?', 'Julia Gillard', 'Margaret Thatcher', 'Indira Gandhi', 'Angela Merkel'),
                    ('History', 'multiple', 'difficult', 'When did Australia become a federation?', '1901', '1910', '1890', '1920'),
                    ('History', 'multiple', 'difficult', 'Which iconic LGBTQ rights event in the United States occurred in June 1969 and is often considered the catalyst for the modern LGBTQ rights movement?', 'Stonewall riots', 'Comptons Cafeteria riot', 'Mattachine Society protest', 'Daughters of Bilitis sit-in'),
                    ('History', 'multiple', 'difficult', 'Who was the fourth president of the United States?', 'James Madison', 'George Washington', 'Thomas Jefferson', 'John Adams'),
                    ('History', 'multiple', 'difficult', 'Which era marked a switch from agricultural practices to industrial practices?', 'The Industrial Revolution', 'The Agricultural Revolution', 'The Renaissance', 'The Enlightenment'),
                    ('History', 'multiple', 'difficult', 'What was the name of the series of programs and projects President Franklin D. Roosevelt enacted during The Great Depression?', 'The New Deal', 'The Fair Deal', 'The Square Deal', 'The New Frontier'),
                    ('History', 'multiple', 'difficult', 'Which four presidents are on Mount Rushmore?', 'George Washington, Abraham Lincoln, Thomas Jefferson, and Theodore Roosevelt', 'George Washington, John Adams, Thomas Jefferson, and James Madison', 'George Washington, Abraham Lincoln, Franklin D. Roosevelt, and John F. Kennedy', 'George Washington, Thomas Jefferson, Andrew Jackson, and Abraham Lincoln'),
                    ('History', 'multiple', 'difficult', 'Who was the first woman to make a million dollars in the United States?', 'Madam C.J. Walker', 'Elizabeth Arden', 'Coco Chanel', 'Estée Lauder'),
                    ('History', 'multiple', 'difficult', 'What do the stripes on the American flag represent?', 'The 13 original colonies', 'The 50 states', 'The founding fathers', 'The branches of government'),
                    ('History', 'multiple', 'difficult', 'Where was Martin Luther King, Jr. born?', 'Atlanta, Georgia', 'Birmingham, Alabama', 'Memphis, Tennessee', 'Washington, D.C.'),
                    ('History', 'multiple', 'difficult', 'What was the name of the landmark Supreme Court case that ruled the racial segregation of schools unconstitutional?', 'Brown v. Board of Education', 'Plessy v. Ferguson', 'Roe v. Wade', 'Miranda v. Arizona'),
                    ('History', 'multiple', 'difficult', 'What year was the Vietnam Veterans Memorial dedicated in Washington, D.C.?', '1982', '1975', '1980', '1973'),
                    ('History', 'multiple', 'difficult', 'Which of the following countries was formerly known as Siam?', 'Thailand', 'Vietnam', 'Cambodia', 'Laos'),
                    ('History', 'multiple', 'difficult', 'What percentage of the worlds Muslim population lives in the Middle East?', '20%', '50%', '80%', '100%'),
                    ('History', 'multiple', 'difficult', 'What percentage of the Middle Easts population is Muslim?', '90%', '50%', '70%', '100%'),
                    ('History', 'multiple', 'difficult', 'In which year was the Australian national anthem “Advance Australia Fair” officially adopted?', '1984', '1901', '1956', '1975'),
                    ('History', 'multiple', 'difficult', 'Who was the first European to reach North America?', 'Leif Erikson', 'Christopher Columbus', 'John Cabot', 'Amerigo Vespucci'),
                    ('History', 'multiple', 'difficult', 'What was the first capital of ancient Egypt?', 'Memphis', 'Thebes', 'Alexandria', 'Cairo'),
                    ('History', 'multiple', 'difficult', 'Who was the pioneering transgender activist and self-identified drag queen known for her role in the Stonewall riots of 1969?', 'Marsha P. Johnson', 'Sylvia Rivera', 'Miss Major Griffin-Gracy', 'Stormé DeLarverie'),
                    ('History', 'multiple', 'difficult', 'Which ancient emperor created an empire going from Macedonia to Egypt and from Greece to India?', 'Alexander the Great', 'Julius Caesar', 'Napoleon Bonaparte', 'Genghis Khan'),
                    ('History', 'multiple', 'difficult', 'Who was Cleopatra having an affair with?', 'Julius Caesar and Mark Antony', 'Julius Caesar and Augustus', 'Mark Antony and Augustus', 'Augustus and Tiberius'),
                    ('History', 'multiple', 'difficult', 'Which of these African civilizations was the only one to experience the Bronze Age?', 'Ancient Egypt', 'Carthage', 'Mali Empire', 'Kingdom of Aksum'),
                    ('History', 'multiple', 'difficult', 'When was the Organization of African Unity (OAU) established?', '1963', '1945', '1957', '1970'),
                    ('History', 'multiple', 'difficult', 'Who was the famous British mathematician, logician, and computer scientist known for his work in breaking the German Enigma code during World War II, and who was later persecuted for his homosexuality?', 'Alan Turing', 'John von Neumann', 'Alonzo Church', 'Kurt Gödel'),
                    ('History', 'multiple', 'difficult', 'Which of the following countries was formerly known as Burma?', 'Myanmar', 'Thailand', 'Laos', 'Cambodia'),
                    ('Nature and Science', 'multiple', 'easy', 'How many wings does a bee have?', '4', '2', '6', '8'),
                    ('Nature and Science', 'multiple', 'easy', 'What do you call a series of large waves caused by an underwater earthquake?', 'Tsunami', 'Tidal wave', 'Surge', 'Ripple'),
                    ('Nature and Science', 'multiple', 'easy', 'How many eyes does a spider typically have?', '8', '2', '4', '6'),
                    ('Nature and Science', 'multiple', 'easy', 'Canis is the Latin word for which animal?', 'Dog', 'Cat', 'Horse', 'Bird'),
                    ('Nature and Science', 'multiple', 'easy', 'If a tree produces acorns, what type of tree is it?', 'Oak tree', 'Pine tree', 'Maple tree', 'Birch tree'),
                    ('Nature and Science', 'multiple', 'easy', 'What animal is known as the ship of the desert?', 'Camel', 'Horse', 'Elephant', 'Kangaroo'),
                    ('Nature and Science', 'multiple', 'easy', 'Which chemical element has O as a symbol?', 'Oxygen', 'Osmium', 'Oganesson', 'Oxygenium'),
                    ('Nature and Science', 'multiple', 'easy', 'In which TV show can you see a group of scientists including Sheldon Cooper and Leonard Hofstadter?', 'Big Bang Theory', 'Friends', 'How I Met Your Mother', 'Breaking Bad'),
                    ('Nature and Science', 'multiple', 'easy', 'Which British naturalist is credited for the theory of natural selection and famous for his contribution to the science of evolution?', 'Charles Darwin', 'Isaac Newton', 'Albert Einstein', 'Stephen Hawking'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the nearest planet to the sun?', 'Mercury', 'Venus', 'Earth', 'Mars'),
                    ('Nature and Science', 'multiple', 'easy', 'How many teeth does an adult human typically have?', '32', '30', '28', '34'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the largest planet in the solar system?', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the hottest planet in the solar system?', 'Venus', 'Mercury', 'Mars', 'Jupiter'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the rarest blood type?', 'AB-', 'O+', 'A-', 'B+'),
                    ('Nature and Science', 'multiple', 'easy', 'On what part of your body would you find the pinna?', 'Ear', 'Hand', 'Foot', 'Nose'),
                    ('Nature and Science', 'multiple', 'easy', 'What part of the plant conducts photosynthesis?', 'Leaves', 'Roots', 'Stem', 'Flower'),
                    ('Nature and Science', 'multiple', 'easy', 'Whats the boiling point of water in degrees Celsius?', '100', '0', '50', '212'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the largest known land animal?', 'African Elephant', 'Blue Whale', 'Giraffe', 'Brown Bear'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the largest known animal?', 'Blue Whale', 'African Elephant', 'Giraffe', 'Brown Bear'),
                    ('Nature and Science', 'multiple', 'easy', 'What tissues connect the muscles to the bones?', 'Tendons', 'Ligaments', 'Cartilage', 'Fascia'),
                    ('Nature and Science', 'multiple', 'easy', 'Who was the scientist to propose the three laws of motion?', 'Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Nikola Tesla'),
                    ('Nature and Science', 'multiple', 'easy', 'The planet Earth is surrounded by different layers of gas, which when taken together, we call the…?', 'Atmosphere', 'Biosphere', 'Stratosphere', 'Troposphere'),
                    ('Nature and Science', 'multiple', 'easy', 'Animals that eat both plants and meat are called what?', 'Omnivores', 'Herbivores', 'Carnivores', 'Insectivores'),
                    ('Nature and Science', 'multiple', 'easy', 'Diabetes develops as the result of a problem with which specific organ in the body?', 'Pancreas', 'Liver', 'Kidney', 'Heart'),
                    ('Nature and Science', 'multiple', 'easy', 'True or false: sound travels faster in air than in water.', 'False', 'True', 'Depends on the temperature', 'Depends on the pressure'),
                    ('Nature and Science', 'multiple', 'easy', 'How long does a human red blood cell survive?', '120 days', '30 days', '365 days', '7 days'),
                    ('Nature and Science', 'multiple', 'easy', 'True or false, lightning is hotter than the sun.', 'True', 'False', 'Depends on the type of lightning', 'Depends on the part of the sun'),
                    ('Nature and Science', 'multiple', 'easy', 'This planet spins the fastest, completing one whole rotation in just 10 hours. Which planet is it?', 'Jupiter', 'Earth', 'Mars', 'Venus'),
                    ('Nature and Science', 'multiple', 'easy', 'How many elements are there in the periodic table?', '118', '100', '150', '92'),
                    ('Nature and Science', 'multiple', 'easy', 'This planet has a collective 53 moons, making it the planet in our solar system with the most number of moons. Which planet is it?', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'),
                    ('Nature and Science', 'multiple', 'easy', 'Where can you find the smallest bone in the human body?', 'Ear', 'Hand', 'Foot', 'Nose'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the largest organ in the human body?', 'Skin', 'Liver', 'Brain', 'Lungs'),
                    ('Nature and Science', 'multiple', 'easy', 'The worlds fastest-growing plant is a species of what?', 'Bamboo', 'Fern', 'Grass', 'Ivy'),
                    ('Nature and Science', 'multiple', 'easy', 'How often does Halleys Comet appear in the sky?', 'Every 76 years', 'Every 100 years', 'Every 50 years', 'Every 150 years'),
                    ('Nature and Science', 'multiple', 'easy', 'What melted rock eventually becomes lava?', 'Magma', 'Granite', 'Basalt', 'Sediment'),
                    ('Nature and Science', 'multiple', 'easy', 'On what continent would you not find bees?', 'Antarctica', 'Africa', 'Asia', 'Australia'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the heaviest organ in the human body?', 'Liver', 'Skin', 'Brain', 'Lungs'),
                    ('Nature and Science', 'multiple', 'easy', 'What is the name of the gas that plants absorb from the atmosphere during photosynthesis?', 'Carbon dioxide', 'Oxygen', 'Nitrogen', 'Hydrogen'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the Astronomical Unit (AU) based on?', 'The average distance between Earth and the Sun', 'The average distance between Earth and the Moon', 'The average distance between the Sun and the Moon', 'The average distance between Earth and Mars'),
                    ('Nature and Science', 'multiple', 'difficult', 'What general name is also given to natural satellites?', 'Moons', 'Stars', 'Planets', 'Asteroids'),
                    ('Nature and Science', 'multiple', 'difficult', 'Humans and chimpanzees share roughly how much DNA?', '98%', '50%', '75%', '85%'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is known as the “master gland” of the human body?', 'Pituitary gland', 'Thyroid gland', 'Adrenal gland', 'Pineal gland'),
                    ('Nature and Science', 'multiple', 'difficult', 'How much taller is the Eiffel Tower during the summer?', '15 cm', '5 cm', '1 m', '10 cm'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the only planet that spins clockwise?', 'Venus', 'Earth', 'Mars', 'Jupiter'),
                    ('Nature and Science', 'multiple', 'difficult', 'The Horsehead Nebula can be found in what constellation?', 'Orion', 'Ursa Major', 'Cassiopeia', 'Cygnus'),
                    ('Nature and Science', 'multiple', 'difficult', 'How many planets in our solar system have moons?', '6', '8', '4', '7'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the largest species in the Felidae family?', 'Tiger', 'Lion', 'Leopard', 'Cheetah'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the most abundant gas in the Earths atmosphere?', 'Nitrogen', 'Oxygen', 'Carbon dioxide', 'Argon'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for gold?', 'Au', 'Ag', 'Fe', 'Gd'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the hardest natural substance on the Earth?', 'Diamond', 'Graphite', 'Quartz', 'Corundum'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the brightest star in the night sky?', 'Sirius', 'Vega', 'Polaris', 'Betelgeuse'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the most common type of blood in humans?', 'O+', 'A+', 'B+', 'AB+'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the largest ocean on Earth?', 'Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the tallest mountain on Earth?', 'Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the longest river on Earth?', 'Nile', 'Amazon', 'Yangtze', 'Mississippi'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the smallest bone in the human body?', 'Stapes', 'Malleus', 'Incus', 'Cochlea'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the largest gland in the human body?', 'Liver', 'Pancreas', 'Thyroid', 'Adrenal'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the powerhouse of the cell?', 'Mitochondria', 'Nucleus', 'Ribosome', 'Endoplasmic reticulum'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for silver?', 'Ag', 'Au', 'Si', 'Al'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the speed of light?', '299,792 kilometers per second', '150,000 kilometers per second', '1,080,000 kilometers per hour', '1,000,000 miles per hour'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the most common element in the universe?', 'Hydrogen', 'Helium', 'Oxygen', 'Carbon'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for iron?', 'Fe', 'Ir', 'In', 'I'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the largest moon in the solar system?', 'Ganymede', 'Titan', 'Callisto', 'Io'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for lead?', 'Pb', 'Ld', 'Le', 'Pd'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the most common isotope of hydrogen?', 'Protium', 'Deuterium', 'Tritium', 'Hydrium'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the densest planet in the solar system?', 'Earth', 'Jupiter', 'Saturn', 'Mercury'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for potassium?', 'K', 'P', 'Po', 'Pt'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the largest continent on Earth?', 'Asia', 'Africa', 'North America', 'Antarctica'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for sodium?', 'Na', 'S', 'So', 'Sa'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the smallest planet in the solar system?', 'Mercury', 'Mars', 'Venus', 'Earth'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for tin?', 'Sn', 'Ti', 'Tn', 'Si'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for copper?', 'Cu', 'Co', 'Cp', 'Cr'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the highest waterfall in the world?', 'Angel Falls', 'Niagara Falls', 'Victoria Falls', 'Iguazu Falls'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the chemical symbol for zinc?', 'Zn', 'Zi', 'Zc', 'Z'),
                    ('Nature and Science', 'multiple', 'difficult', 'What is the deepest point in the ocean?', 'Mariana Trench', 'Challenger Deep', 'Puerto Rico Trench', 'Java Trench'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who directed the movie "Jaws"?', 'Steven Spielberg', 'George Lucas', 'James Cameron', 'Martin Scorsese'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Which actor played Tony Stark in the "Iron Man" series?', 'Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'What is the name of the kingdom in the movie "Frozen"?', 'Arendelle', 'Atlantis', 'Agrabah', 'Auradon'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who composed the music for "Star Wars"?', 'John Williams', 'Hans Zimmer', 'Danny Elfman', 'James Horner'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'What is the name of the hobbit played by Elijah Wood in "The Lord of the Rings"?', 'Frodo Baggins', 'Samwise Gamgee', 'Peregrin Took', 'Meriadoc Brandybuck'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who won an Oscar for Best Actor for his role in "The Kings Speech"?', 'Colin Firth', 'Tom Hanks', 'Brad Pitt', 'Leonardo DiCaprio'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'What is the name of the fictional African country in "Black Panther"?', 'Wakanda', 'Zamunda', 'Narnia', 'Asgard'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Hermione Granger in "Harry Potter"?', 'Emma Watson', 'Emma Stone', 'Emily Blunt', 'Emilia Clarke'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'What is the name of the main character in "The Matrix"?', 'Neo', 'Morpheus', 'Trinity', 'Cypher'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Jack Dawson in "Titanic"?', 'Leonardo DiCaprio', 'Brad Pitt', 'Johnny Depp', 'Tom Cruise'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'What is the name of the island in "Jurassic Park"?', 'Isla Nublar', 'Isla Sorna', 'Isla Pena', 'Isla Matanceros'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Gollum in "The Lord of the Rings"?', 'Andy Serkis', 'Ian McKellen', 'Viggo Mortensen', 'Sean Astin'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who directed the movie "Inception"?', 'Christopher Nolan', 'Steven Spielberg', 'James Cameron', 'Quentin Tarantino'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Maximus in "Gladiator"?', 'Russell Crowe', 'Joaquin Phoenix', 'Tom Hanks', 'Brad Pitt'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the villain in "The Dark Knight"?', 'The Joker', 'The Penguin', 'The Riddler', 'Two-Face'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Black Widow in "The Avengers"?', 'Scarlett Johansson', 'Gwyneth Paltrow', 'Natalie Portman', 'Elizabeth Olsen'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who directed the movie "E.T. the Extra-Terrestrial"?', 'Steven Spielberg', 'George Lucas', 'James Cameron', 'Martin Scorsese'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Indiana Jones?', 'Harrison Ford', 'Tom Cruise', 'Brad Pitt', 'Robert Downey Jr.'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the director of the "Transformers" series?', 'Michael Bay', 'Steven Spielberg', 'James Cameron', 'Christopher Nolan'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Don Vito Corleone in "The Godfather"?', 'Marlon Brando', 'Al Pacino', 'Robert De Niro', 'James Caan'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the voice of Woody in "Toy Story"?', 'Tom Hanks', 'Tim Allen', 'John Ratzenberger', 'Don Rickles'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Jack Sparrow in "Pirates of the Caribbean"?', 'Johnny Depp', 'Orlando Bloom', 'Keira Knightley', 'Geoffrey Rush'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who directed the movie "Psycho"?', 'Alfred Hitchcock', 'Stanley Kubrick', 'Martin Scorsese', 'Francis Ford Coppola'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Rocky Balboa?', 'Sylvester Stallone', 'Arnold Schwarzenegger', 'Bruce Willis', 'Jean-Claude Van Damme'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the director of "Pulp Fiction"?', 'Quentin Tarantino', 'Martin Scorsese', 'Steven Spielberg', 'Christopher Nolan'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Marty McFly in "Back to the Future"?', 'Michael J. Fox', 'Christopher Lloyd', 'Crispin Glover', 'Thomas F. Wilson'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Han Solo in "Star Wars"?', 'Harrison Ford', 'Mark Hamill', 'Carrie Fisher', 'Billy Dee Williams'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the director of "The Shining"?', 'Stanley Kubrick', 'Alfred Hitchcock', 'Steven Spielberg', 'Martin Scorsese'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Neo in "The Matrix"?', 'Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss', 'Hugo Weaving'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the director of "Avatar"?', 'James Cameron', 'Steven Spielberg', 'George Lucas', 'Christopher Nolan'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Rose in "Titanic"?', 'Kate Winslet', 'Cate Blanchett', 'Nicole Kidman', 'Julia Roberts'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of James Bond in "Casino Royale"?', 'Daniel Craig', 'Sean Connery', 'Pierce Brosnan', 'Roger Moore'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the director of "The Dark Knight"?', 'Christopher Nolan', 'Steven Spielberg', 'James Cameron', 'Quentin Tarantino'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Thor in "Thor: Ragnarok"?', 'Chris Hemsworth', 'Chris Evans', 'Chris Pratt', 'Chris Pine'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the director of "Interstellar"?', 'Christopher Nolan', 'Steven Spielberg', 'James Cameron', 'Quentin Tarantino'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Wolverine in "X-Men"?', 'Hugh Jackman', 'Patrick Stewart', 'Ian McKellen', 'James McAvoy'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the director of "Mad Max: Fury Road"?', 'George Miller', 'Steven Spielberg', 'James Cameron', 'Christopher Nolan'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who played the character of Lara Croft in "Tomb Raider"?', 'Angelina Jolie', 'Scarlett Johansson', 'Charlize Theron', 'Halle Berry'),
                    ('Entertainment and Movies', 'multiple', 'easy', 'Who is the director of "The Grand Budapest Hotel"?', 'Wes Anderson', 'Steven Spielberg', 'James Cameron', 'Christopher Nolan'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the film "Inception," what is the name of the device used to enter and manipulate dreams?', 'Totem', 'Dreamweaver', 'Mind Matrix', 'Reality Spinner'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who directed the 1994 film "Pulp Fiction"?', 'Quentin Tarantino', 'Martin Scorsese', 'Christopher Nolan', 'Steven Spielberg'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the movie "Blade Runner," what is the term used for bioengineered beings that are virtually identical to humans?', 'Replicants', 'Synthoids', 'Humanoids', 'BioClones'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which actor played the character of Anton Chigurh in the film "No Country for Old Men"?', 'Javier Bardem', 'Heath Ledger', 'Daniel Day-Lewis', 'Tom Hardy'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the 1971 film "A Clockwork Orange," what is the name of the protagonist?', 'Alex DeLarge', 'Winston Smith', 'Travis Bickle', 'Randle McMurphy'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the highest-grossing animated film of all time, as of 2023?', 'Frozen II', 'The Lion King', 'Toy Story 4', 'Finding Nemo'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the movie "Eternal Sunshine of the Spotless Mind," what company provides the memory erasure service?', 'Lacuna, Inc.', 'MindWipe Solutions', 'ForgetMeNot Labs', 'MemoryGuard Systems'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which actress won an Academy Award for her role in the 2015 film "Room"?', 'Brie Larson', 'Jennifer Lawrence', 'Cate Blanchett', 'Natalie Portman'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the film "The Matrix," what pill does Neo take from Morpheus?', 'Red Pill', 'Blue Pill', 'Green Pill', 'Yellow Pill'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who played the role of Howard Hughes in the 2004 film "The Aviator"?', 'Leonardo DiCaprio', 'Tom Hanks', 'Johnny Depp', 'Brad Pitt'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the name of the fictional band in the film "Almost Famous"?', 'Stillwater', 'Fever Dog', 'Penny Lane', 'Golden Slumbers'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the movie "The Usual Suspects," who is Keyser Söze?', 'Roger "Verbal" Kint', 'Dean Keaton', 'Michael McManus', 'Fred Fenster'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which film won the Academy Award for Best Picture in 2017?', 'Moonlight', 'La La Land', 'Manchester by the Sea', 'Hacksaw Ridge'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the 1998 film "The Truman Show," what is Trumans last name?', 'Burbank', 'Anderson', 'Hobbs', 'Wellington'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who directed the science fiction film "Interstellar" released in 2014?', 'Christopher Nolan', 'James Cameron', 'Denis Villeneuve', 'Ridley Scott'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the name of the fictional town where the events of the TV series "Twin Peaks" take place?', 'Twin Peaks', 'Bluebell', 'Pinecrest', 'Cedar Falls'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which actress played the role of Clarice Starling in the film "The Silence of the Lambs"?', 'Jodie Foster', 'Julianne Moore', 'Sigourney Weaver', 'Holly Hunter'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the movie "The Prestige," what is the name of the mysterious object that the magicians try to replicate?', 'The Transported Man', 'The Vanishing Box', 'The Illusionists Secret', 'The Mystic Mirror'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who played the character of Vito Corleone in the film "The Godfather: Part II"?', 'Robert De Niro', 'Marlon Brando', 'Al Pacino', 'Joe Pesci'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the film "Requiem for a Dream," what is the nickname given to the character played by Jared Leto?', 'Harry Goldfarb', 'Tyrone Love', 'Sara Goldfarb', 'Marion Silver'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which film features a character named Tyler Durden and explores themes of consumerism and identity?', 'Fight Club', 'American Psycho', 'Se7en', 'Memento'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the name of the alien species in the 1986 film "Aliens"?', 'Xenomorphs', 'Predators', 'Skrulls', 'Ewoks'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the movie "The Grand Budapest Hotel," who played the character M. Gustave?', 'Ralph Fiennes', 'Jude Law', 'Bill Murray', 'Edward Norton'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which 2000 film directed by Darren Aronofsky explores the intense and competitive world of ballet?', 'Black Swan', 'Whiplash', 'The Wrestler', 'The Fountain'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who directed the 1973 classic horror film "The Exorcist"?', 'William Friedkin', 'Alfred Hitchcock', 'Stanley Kubrick', 'John Carpenter'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who played the character of Tommy DeVito in the 1990 film "Goodfellas"?', 'Joe Pesci', 'Robert De Niro', 'Ray Liotta', 'Al Pacino'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the film "City of God," what is the name of the Brazilian city where the story is set?', 'Rio de Janeiro', 'São Paulo', 'Brasília', 'Salvador'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which actress won the Academy Award for Best Actress for her role in the 2016 film "La La Land"?', 'Emma Stone', 'Natalie Portman', 'Cate Blanchett', 'Jennifer Lawrence'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the title of the 1999 film that stars Edward Norton and Brad Pitt and explores themes of anti-consumerism?', 'Fight Club', 'American Psycho', 'Se7en', 'The Matrix'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the film "American Beauty," what is the name of the character played by Kevin Spacey?', 'Lester Burnham', 'Frank Underwood', 'Jack Vincennes', 'John Doe'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who directed the 2008 film "Slumdog Millionaire" that won eight Academy Awards, including Best Picture?', 'Danny Boyle', 'Steven Spielberg', 'Martin Scorsese', 'Ang Lee'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the name of the mysterious and elusive character played by David Bowie in the film "The Prestige"?', 'Nikola Tesla', 'Thomas Edison', 'Alexander Graham Bell', 'Henry Ford'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the 1985 film "Back to the Future," what is the name of Doc Browns dog?', 'Einstein', 'Newton', 'Galileo', 'Tesla'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who played the character of Mark Zuckerberg in the 2010 film "The Social Network"?', 'Jesse Eisenberg', 'Andrew Garfield', 'Armie Hammer', 'Justin Timberlake'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the movie "A Beautiful Mind," who played the role of John Nash?', 'Russell Crowe', 'Tom Hanks', 'Matt Damon', 'Leonardo DiCaprio'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the title of the 1984 film directed by James Cameron that features a cyborg assassin sent back in time?', 'The Terminator', 'Blade Runner', 'RoboCop', 'WarGames'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which actor played the role of Max Rockatansky in the 1979 film "Mad Max"?', 'Mel Gibson', 'Bruce Willis', 'Sylvester Stallone', 'Kurt Russell'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the film "Casablanca," what is the name of the nightclub owned by Rick Blaine?', 'Ricks Café Américain', 'La Belle Aurore', 'Blue Parrot', 'Café de Paris'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who directed the 1999 film "Magnolia" that features an ensemble cast and interrelated storylines?', 'Paul Thomas Anderson', 'Quentin Tarantino', 'David Fincher', 'Coen Brothers'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the 2006 film "Children of Men," what has caused global infertility?', 'Unknown', 'Nuclear War', 'Alien Invasion', 'Pandemic'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which actor played the role of Freddie Quell in the 2012 film "The Master"?', 'Joaquin Phoenix', 'Philip Seymour Hoffman', 'Tom Hardy', 'Leonardo DiCaprio'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In Disneys "The Little Mermaid," what is the name of Ursulas moray eel sidekick?', 'Flotsam and Jetsam', 'Triton and Nereus', 'Squirt and Bubbles', 'Spike and Splash'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which Disney animated film features a character named Kuzco, who is transformed into a llama?', 'The Emperors New Groove', 'Mulan', 'Tarzan', 'Hercules'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the name of the animated Disney film released in 1940 that consists of eight different segments set to classical music?', 'Fantasia', 'Dumbo', 'Bambi', 'Cinderella'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the movie "Beauty and the Beast," what is the name of Gastons sidekick and henchman?', 'LeFou', 'Maurice', 'Cogsworth', 'Lumière'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which Disney film tells the story of a young boy named Mowgli, raised by wolves in the jungle?', 'The Jungle Book', 'Tarzan', 'Robin Hood', 'Dumbo'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In Disneys "Aladdin," what is the name of the tiger that is Jasmines loyal companion?', 'Rajah', 'Sultan', 'Abu', 'Iago'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the voice actor for the character Scar in Disneys "The Lion King"?', 'Jeremy Irons', 'James Earl Jones', 'Patrick Stewart', 'Ian McKellen'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the animated film "Pocahontas," what is the name of Pocahontass hummingbird companion?', 'Flit', 'Buzz', 'Zazu', 'Wings'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which Disney animated film features the character Frou-Frou, a white horse who serves as a ladys maid to the Duchess?', 'The Aristocats', 'Cinderella', 'Sleeping Beauty', 'Beauty and the Beast'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the birth name of the Sith Lord commonly known as Darth Vader?', 'Anakin Skywalker', 'Obi-Wan Kenobi', 'Luke Skywalker', 'Kylo Ren'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In "Star Wars: Episode VI - Return of the Jedi," what is the name of the desert palace where Jabba the Hutt resides?', 'Jabbas Palace', 'Mos Eisley Cantina', 'Tatooine Outpost', 'Hutt Hideaway'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the actor behind the mask of the bounty hunter Boba Fett in the original "Star Wars" trilogy?', 'Jeremy Bulloch', 'Temuera Morrison', 'Daniel Logan', 'Ray Park'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the name of the forest moon that serves as the location for much of the action in "Star Wars: Episode VI - Return of the Jedi"?', 'Endor', 'Dagobah', 'Hoth', 'Yavin'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In "Star Wars: Episode V - The Empire Strikes Back," who reveals to Luke Skywalker that he is his father?', 'Darth Vader', 'Emperor Palpatine', 'Obi-Wan Kenobi', 'Yoda'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What species is Yoda in the "Star Wars" universe?', 'Unknown', 'Hutt', 'Wookiee', 'Mon Calamari'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the name of the Rebel Alliances base in "Star Wars: Episode IV - A New Hope"?', 'Yavin 4', 'Hoth', 'Endor', 'Dantooine'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which character declares, "I find your lack of faith disturbing" in "Star Wars: Episode IV - A New Hope"?', 'Darth Vader', 'Emperor Palpatine', 'Grand Moff Tarkin', 'Count Dooku'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the only actor to receive an Academy Award nomination for their performance in a "Star Wars" film?', 'Alec Guinness', 'Harrison Ford', 'Mark Hamill', 'Natalie Portman'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In "Star Wars: Episode VII - The Force Awakens," what is the name of the desert scavenger played by Daisy Ridley?', 'Rey', 'Finn', 'Poe Dameron', 'Kylo Ren'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the real name of the Marvel character Deadpool?', 'Wade Wilson', 'Logan Howlett', 'Peter Parker', 'Matt Murdock'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the Marvel Cinematic Universe, what is the name of Thors enchanted hammer?', 'Mjolnir', 'Stormbreaker', 'Gungnir', 'Excalibur'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the primary antagonist in the Marvel film "Black Panther"?', 'Erik Killmonger', 'Ulysses Klaue', 'M Baku', 'N Jadaka'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the Marvel Comics, what is the alias of T Challa, the king and protector of the fictional African nation of Wakanda?', 'Black Panther', 'Black Widow', 'Black Bolt', 'Black Knight'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which Marvel character is known for wielding a shield made of vibranium?', 'Captain America', 'Iron Man', 'Thor', 'Black Widow'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In the Marvel Cinematic Universe, who plays the character Natasha Romanoff, also known as Black Widow?', 'Scarlett Johansson', 'Gal Gadot', 'Brie Larson', 'Jennifer Lawrence'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the real name of the character Iron Fist in Marvel Comics?', 'Danny Rand', 'Luke Cage', 'Matt Murdock', 'Peter Parker'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which Marvel superhero is a master of mystic arts and the Sorcerer Supreme?', 'Doctor Strange', 'Scarlet Witch', 'Hawkeye', 'Black Panther'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'In Marvel Comics, what is the name of the alien symbiote that bonds with Eddie Brock to create Venom?', 'Venom', 'Carnage', 'Riot', 'Scream'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the creator of the Marvel character Spider-Man?', 'Stan Lee', 'Jack Kirby', 'Steve Ditko', 'John Romita Sr.'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the captain of the USS Enterprise in the 2009 "Star Trek" film directed by J.J. Abrams?', 'James T. Kirk', 'Jean-Luc Picard', 'Spock', 'Christopher Pike'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which alien species in "Star Trek" is known for their assimilation of other cultures and technology?', 'Borg', 'Klingon', 'Cardassian', 'Romulan'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who played the character Captain Jean-Luc Picard in the TV series "Star Trek: The Next Generation"?', 'Patrick Stewart', 'William Shatner', 'Avery Brooks', 'Scott Bakula'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the primary bending skill of Toph Beifong, a main character in "Avatar: The Last Airbender"?', 'Earthbending', 'Waterbending', 'Firebending', 'Airbending'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the founder and leader of the Equalists, an anti-bending revolutionary group in "The Legend of Korra"?', 'Amon', 'Unalaq', 'Zaheer', 'Kuvira'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which modern pop artist released the 2017 album "Melodrama," featuring the hit song "Green Light"?', 'Lorde', 'Taylor Swift', 'Billie Eilish', 'Ariana Grande'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which modern rock band is fronted by lead singer Matt Bellamy and is known for hits like "Uprising" and "Starlight"?', 'Muse', 'Coldplay', 'Imagine Dragons', 'The Killers'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the lead vocalist of the rock band Paramore?', 'Hayley Williams', 'Amy Lee', 'Lzzy Hale', 'Florence Welch'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which contemporary R&B artist released the critically acclaimed album "Channel Orange" in 2012?', 'Frank Ocean', 'The Weeknd', 'Miguel', 'Solange'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which American singer-songwriter is known for her folk-rock style and albums like "Jagged Little Pill"?', 'Alanis Morissette', 'Sheryl Crow', 'Tori Amos', 'Ani DiFranco'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Who is the lead singer of the alternative rock band Radiohead, known for albums like "OK Computer" and "Kid A"?', 'Thom Yorke', 'Chris Martin', 'Eddie Vedder', 'Damon Albarn'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which British singer-songwriter released the 2011 album "21," featuring hits like "Rolling in the Deep" and "Someone Like You"?', 'Adele', 'Ed Sheeran', 'Sam Smith', 'Florence Welch'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'What is the stage name of the American rapper and actor whose real name is Marshall Bruce Mathers III?', 'Eminem', 'Jay-Z', 'Kendrick Lamar', 'Drake'),
                    ('Entertainment and Movies', 'multiple', 'difficult', 'Which American singer, known for her powerful vocals and hits like "Vision of Love" and "We Belong Together," is often referred to as the "Songbird Supreme"?', 'Mariah Carey', 'Whitney Houston', 'Celine Dion', 'Beyoncé');
                    """
                )

    def create(self, question: QuestionModelIn) -> QuestionModelOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO questions
                        (category, type, difficulty, question,
                        correct_answer, incorrect_answer_1,
                        incorrect_answer_2, incorrect_answer_3)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        question.category,
                        question.type,
                        question.difficulty,
                        question.question,
                        question.correct_answer,
                        question.incorrect_answer_1,
                        question.incorrect_answer_2,
                        question.incorrect_answer_3,
                    ],
                )
                id = result.fetchone()[0]
                return self.question_in_to_out(id, question)

    def update(
        self, question_id: int, question: QuestionModelIn
    ) -> Union[QuestionModelOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE questions
                        SET category = %s
                        , type = %s
                        , difficulty = %s
                        , question = %s
                        , correct_answer = %s
                        , incorrect_answer_1 = %s
                        , incorrect_answer_2 = %s
                        , incorrect_answer_3 = %s
                        WHERE id = %s
                        """,
                        [
                            question.category,
                            question.type,
                            question.difficulty,
                            question.question,
                            question.correct_answer,
                            question.incorrect_answer_1,
                            question.incorrect_answer_2,
                            question.incorrect_answer_3,
                            question_id,
                        ],
                    )
                return self.question_in_to_out(question_id, question)
        except Exception as e:
            print(e)
            return {"message": "Could not update question"}

    def delete(self, question_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE  FROM questions
                        WHERE id = %s
                        """,
                        [question_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def question_in_to_out(self, id: int, question: QuestionModelIn):
        old_data = question.dict()
        return QuestionModelOut(id=id, **old_data)

    def record_to_question_out(self, record):
        return QuestionModelOut(
            id=record[0],
            category=record[1],
            type=record[2],
            difficulty=record[3],
            question=record[4],
            correct_answer=record[5],
            incorrect_answer_1=record[6],
            incorrect_answer_2=record[7],
            incorrect_answer_3=record[8],
        )
