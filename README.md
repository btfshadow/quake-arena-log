# The Quake 3 Arena Log Parser

this project has the objective to create a log parse to be used in quake 3 arena servers. 


# How To RUN 

You need to have Python 3.9 and the PIP installed

using the command 'export PYTHONPATH=./' inside the project root to not have some issues in python imports

Now you will install the Poetry using the command

`pip install poetry` or `pip3 install poetry`

now you run the poetry install

using the command `poetry install`

to run the project only need to run 

`poetry run local_file_reader.py`

and to run the tests

`poetry run pytest`


## Todo List

- Improve the tests
- Make some API or Django to consume the parse
- Make Performance tests
- Improve CI Speed
- Make a CD template using Heroku or Vercel

