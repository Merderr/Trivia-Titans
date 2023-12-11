1. `Functionality`: Articulate the capabilities of your app or service. :hammer_and_wrench:

- E.g.: Our RESTful API enables CRUD operations for movie reviews.

2. `User Stories/Scenarios`: Outline key use-cases, ideally using Gherkin syntax. :cucumber:

- E.g.: `Given` a user is logged in, `When` they post a review, `Then` it appears on their profile.

3. `Intended Market`:
   Trivia Titans is crafted for individuals who revel in the thrill of trivia battles, seeking a competitive yet enjoyable solo gaming experience with planned multiplayer expansion.

   Key Features Tailored for Trivia Titans:

   - Competitive solo gameplay with leaderboard rankings.
   - A vast array of challenging trivia questions spanning diverse categories.
   - Achievement system to recognize and reward accomplishments.
   - Mobile-friendly interface for seamless gaming anytime, anywhere.

4. `Stretch Goals`:

   - Potential multiplayer head to head game mode.

5. `Onboarding`:

   To fully enjoy this application on your local machine, please make sure to follow these steps:

   1. Clone the repository down to your local machine
   2. CD into the new project directory
   3. Run docker volume create postgrestriviadb
   4. Run docker compose build
   5. Run docker compose up

   Goodluck on the games!

   Deployment of our application was made to Cirrus by Galvanize https://cirrus.mod3projects.com/ to manage cloud instances.
   We performed the following steps to deploy our whatevr application:

   1. Add a Dockerfile for the deployment of each of your services.
   2. Write a pipeline that builds the container for each service.
   3. Run the pipeline to generate the images in your gitlab registry for each service.
   4. Deploy the image on Galvanize Cirrus using the SDK.

   When running our application locally, we used docker-compose to build and run our application. When deploying our application to Cirrus, we used the SDK to build and run our application. The SDK is a command line tool that allows you to interact with the Cirrus API. The SDK is installed on the Cirrus instance and is used to build and run the application. The SDK is also installed on your local machine and is used to deploy the application to Cirrus. The SDK is used to create a pipeline that builds the container for each service and runs the pipeline to generate the images in your gitlab registry for each service. The SDK is also used to deploy the image on Galvanize Cirrus.
   We used the following commands to build and deploy our application to Cirrus:

   `glv-cloud-cli deploy -a api -i registry.gitlab.com/ice-climbers/trivia-titans/api:latest -e SIGNING_KEY=AC8C8396F9F516FCE01A6805FF8C3D8E -e postgresql://exampleuser:secret@aug-2023-2-pt-db-service.default.svc.cluster.local/postgrestriviadata -e CORS_HOST=https://ice-climbers.gitlab.io`

   We used the following commands to build our Postgres DB into Cirrus:

   `glv-cloud-cli deploy -a db -i postgres:14.5-bullseye -e POSTGRES_DB=postgrestriviadata -e POSTGRES_USER=example_user -e POSTGRES_PASSWORD=secret -m /var/lib/postgresql -p 5432 -x=false`

6. `Tech Stack`:

   - Frontend: React
   - Backend: FastAPI
   - Database: PostgreSQL
   - Containerization: Docker

7. `Journaling`:

   Please see journals folder.

8. `Documentation`: Attach DB schemas, wireframes, and API contracts. :clipboard:
   -E.g.: point to the documents dir

9. `Issue Tracking`:

   https://gitlab.com/ice-climbers/trivia-titans/-/boards

10. `Testing`:

    test_get_users:

    - Purpose: Tests the endpoint for retrieving users. Overrides the dependency for the UserRepository with FakeUserRepo. Sends a GET request to "/api/users/". Resets the dependency overrides. Checks if the response status code is 200 and the returned JSON is an empty list. Created by Seth Porche.

    test_get_all_users:

    - Purpose: Another test for retrieving users, possibly for a different endpoint. Uses the override_dependencies() context manager. Sends a GET request to "/api/users". Verifies the response status code and checks if the returned JSON is an empty list. Created by Mason Doney.

    test_get_question:

    - Purpose: Tests the endpoint for retrieving a specific question. Overrides the dependency for the QuestionRepository with FakeQuestionRepo. Sends a GET request to "/api/questions/1". Resets the dependency overrides. Verifies the response status code and checks if the returned JSON matches the expected QuestionModelOut. Created by Taylor Pearce.

    test_get_token:

    - Purpose: Tests the endpoint for retrieving a token. Sends a GET request to "/token". Checks the response status code and the structure of the returned JSON, ensuring the presence and types of certain fields. Created by Hamza Ahmed.
