# phase-3-project

1. Set up python environment with 
```pipenv install sqlalchemy alembic```

2. Set up layout based on project template
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

3. Set up a simple layout for the ```cli.py``` with 3 options. Add, search and exit.