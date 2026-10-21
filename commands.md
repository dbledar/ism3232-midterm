# Terminal Record: Cloudstep Software

## 1. Building the project
The commands I typed to build this project, in order, were:

**mkdir ~/ism3232/ism3232-midterm**: created the project folder

**cd ~/ism3232/ism3232-midterm**: moved into the project folder

**touch business_rules.py main.py**: created the two python files

**touch commands.md README.md**: created the two markdown files

**venv**: alias used to run python -m venv .venv quicker

**activate**: alias used to run source .venv/bin/activate quicker

**pip install ruff pytest**: installed pytest and ruff for the git ritual

**pip freeze requirements.txt**: saved the files used in the virtual environment to a text file

**git init**: initialized a new git session

**git remote add origin https://github.com/dbledar/ism3232-midterm.git**: connected the current git session to the related github repository

**echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore**: made sure the virtual environment and cache of pytest runs don't get saved to the github repository

**touch tests/__init__.py tests/test_business_rules.py**: setup the python files necessary for pytest to run during the git ritual

## 2. The virtual environment
Running which python3 in my terminal returns /home/drpet/ism3232/ism3232-midterm/.venv/bin/python3. This demonstrates that I am running in the virtual environment because the current python interpreter is listed as being located in the .venv file.

## 3. The project structure
Running tree -L 2 shows the entire project structure, including main.py, business_rules.py, commands.md, README.md, and the tests directory. The command does not display my Documents or Downloads folder. This is because these folders exist outside the scope of the ism3232-midterm folder. If I had run tree -L 2 from my home directory, I would've seen those folders.

## 4. Every function and test