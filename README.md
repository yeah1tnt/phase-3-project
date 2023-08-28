# Dictionary Game

## Overview
Based of the idea of my last project, flash card generator [here](https://github.com/yeah1tnt/phase-2-project).

This project is a game where user can input word, with the part of speech and the project wil pull a definition from a public [API](https://dictionaryapi.dev/) to store them in dictionary.db

The user can use the generated word (either by manual input or automation) to play a multiple choice game, where they can choose which definition/word is correct.

## Installtion

You will need to run 
```
pipenv install
```
to install this project's perspective's libraries

If the list of word in the library/user/score are not to your liking, go to lib/db/seed.py and uncomment the specific line, delete_all() will delete everything in the database, in the delete_all() function, you can comment out the user/gamedata/dictionary if you want to keep a certain database as well.
```python

def delete_all():
    session.query(User).delete()
    session.query(Dictionary).delete()
    session.query(GameData).delete()
    session.commit()

if __name__ == '__main__':
    # delete_all()
    # create_user()
    create_dictionary()
    # create_game_data()
    
    session.close()
    session.commit()
```


## Log

Decided to keep a log of my progress this time, click below to expand, some part might not be updated due to time constrait. Might go back when time permit.
<details>
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

11 - dictionary, showing word and adding word with choice of what part of speech it will be. 

12 - generate a random word and find its definition based on random chance of a part of speech. Force the function to return a value if it did not find any the first time based on the word generated. Added delete function to delete word off the database

13 - Worked on game menu, show highest score, current user's score.

14 - Worked on actual guessing game. Word and definition are pulled from the database, most challenging part of this project.

15 - 8/27/2023 project is completed, every function should work as intended, some bug might not be found yet.
</details>

## License

This work is published under [MIT](https://github.com/yeah1tnt/phase-2-project/blob/main/LICENSE) License