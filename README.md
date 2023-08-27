# phase-3-project

1 - Set up python environment with 
```pipenv install sqlalchemy alembic```

2 - Set up layout based on project template
```
|- Pipfile
|- Pipfile.lock
|- README.md
|- lib
    |- cli.py
    |- debug.py
    |- helpers.py
    |- db
        |-models.py
        |-seed.py
```

3 - Set up a simple layout for the ```cli.py``` with 3 options. Add, search and exit.

4 - Install Faker, set up alembic.ini and edit env.py.

5 - Set up models.py, with User, Dictionary and GameData, fix alembic.ini, and started on seed.py to generate data. Use alembic to generate dictionary.db
```alembic revision --autogenerate -m ""``` and ```alembic upgrade head```

6 - test seed.py and data input. Test pulling definition from https://dictionaryapi.dev/ with a random word generated, the data pulled a json type. Pulling the first definition, but will need user input to pull noun, verb or adjective 

source: https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script

7 - re-structuring cli
```
|- Ask for username
    |               (|- Register username (if user/name isn't in db))
    |- Access user data
        |= Show all users and their score
        |- Reset current user's score
    |- Access dictionary ()
    |   |- List all word/definition
    |   |- Add word manually
    |       |- Choose adjective (return success message or fail message)
    |   |- Add word randomly
    |       |- Choose adjective (return success message or fail message)
    |   |- Delete word
    |       |- Enter word to delete
    |   |- Search word
    |- Play dictionary game
```

8 - installed ipdb for troubleshooting, restructuring main menu and option. Added function to register new user

9 - Have to reset alembic due to error, redo revision and upgrade head, foreign key for user_id and relationship

10 - refined show all user and score and reset user's score