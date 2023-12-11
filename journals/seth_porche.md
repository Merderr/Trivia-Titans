# 11/7/2023: Wireframe Discussion:

Collaborated with the team to decide upon a project, guided largely by whichever third party API we could find that was free and functional.

# 11/8/2023: Wireframe Discussion:

Worked with the team to discuss project plans. Put together an excalidraw of the user experience.

# 11/13/2023: Gitlab Issue / Project Setup:

Worked with the team to create a series of gitlab issues for us to track and plan the progress of our project. Worked on basic project setup as a team.

# 11/14/2023: Presentation / Project Setup:

Our team presented our project plans to the class. Again, worked on basic project setup as a team.

# 11/15/2023: Backend User Routers/Queries:

Set up the SQL table for the user model and began making the associated routers for CRUD.

# 11/16/2023: User Routers/Queries:

Started to build out the create_user query, using the table as a guide. Nothing too complicated, just a username, password, score, and their name. It's not a social media site, after all.

# 11/16/2023: User Routers/Queries:

Ditched the third party api in lieu of formulating our own questions in a pre-loaded SQL database. The api was unreliable as the site was down a couple times during this short period of development, probably due to thousands of other students using the same api?

Also got the get_users function working, now on to the id-specific user search.

# 11/20/2023: Backend Authorization

Worked with the Team in a mob coding session to get backend authorization working with JWT-down. jwt-down isn't the most up to date and doesn't interact very well with React + Vite, but we got it working.

# 11/21/2023: Frontend Authorization

Worked on getting frontend authorization working with JWT-Down. Ran into a lot of issues as JWT-Down doesn't work well with VITE-REACT and even though it was created to make authorization easier it is a rigid setup that is difficult to modify.

# 11/22/2023 User Routers/Queries:

Went back through my work to fix up any create or get calls that weren't interacting with the password hashing the way we wanted them to, also moved on to update_user and delete_user.

# 11/27/2023 Update User/Delete User:

Worked on adding score updating functionality to game, ensuring that user High Score is dynamic.

# 11/28/2023 Update User/Delete User:

Got Delete User up and working in Docs, moved on to Update.

# 11/29/2023 Update User/Delete User:

Got update user mostly working, need to fine tune it to ensure it will work with the score updating with each game.

# 11/30/2023 Update User/Delete User:

Fully integrated Update User to work with the game, fixing bugs that were resetting the score to zero when certain interactions with the navbar took place.

# 12/1/2023 Minor QoL Fixes

Changed font on certain pages to be easier to read amongst purple/pink background, including the NavBar.

# 12/4/2023 Leaderboard Feature

Edited Leaderboard to highlight current user. Made styling changes on leaderboard fonts and items.

# 12/5/2023 Leaderboard Feature/Error Hunting

Worked on finishing up leaderboard highlight feature, looked into where we would need error handling.

# 12/6/2023 Deployment Changes

We ran into a bunch of errors trying to get our code to work with deployment, I just cleared some errors. Also, changed the pre-made user scores to be more realistic for a new user to try and climb the leaderboard through.

# 12/7/2023 Unit Test

Started working on making a create_user unit test, it seems like the authentication we have in place is making it difficult to test.

# 12/8/2023 Unit Test

After trying unsuccessfully to make a create user test, I switched to get_all_users, only to realize upon finishing the test that we already have that unit test working.

# 12/11/2023 Unit Test Changes

Working on changing the unit test to check for a specific user within our database. Also, checking for error handling such as the 500 error that happens on the homepage when a user is not logged in. It doesn't break anything, but it would be nice to clear the error just to have everything running smoothly before presenting the project.
