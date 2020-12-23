# BlueStacks Discord Bot

## Problem Statement:
   ##### [click here](https://github.com/bluestacks/backend-developer-challenge)

## Test Bot
   ##### [invite link](https://discord.gg/rD9P8seTwv)    

### Expected Output -

1. If a user sends 'hi', the bot will reply 'hey'
2. if a user sends '!google YOUR_QUERY_HERE', and it'll reply with the top five links
3. if a user sends '!recent YOUR_QUERY_HERE', and it'll reply with a list of similar searches in the user's history


## Steps to create your own bot:

1. Create a virtual environment -
   `conda create --name <env> --file requirements.txt`
2. activate virtual env - 
   `activate <env>`
3. Create your discord bot by visiting [developers console](https://discordapp.com/developers/applications)
4. Create google [custom search api](https://developers.google.com/custom-search/v1/overview) credentials
5. Create your **_PostgreSQL database_**
6. Create the **_table 'searches'_** using the SQL query:
   `CREATE TABLE searches (user_id VARCHAR(256), keyword VARCHAR(256), search_time TIMESTAMP);`
7. Update secret.env file.
8. Run the app -
   `python bot.py`
