

# Setup

I would suggest to make use of virtual environments to run any kind of application. (I personally use [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html))

`requirements.txt` can be found at top level directory of the project folder.


## Install pipenv

Windows Users

`pip install pipenv`


Mac/Linux Users

`pip3 install pipenv`


Use `pipenv shell` to create a virtual environment. Once, the environment is created.

If you only have a `requirements.txt` file available when running `pipenv install`, pipenv will automatically import the contents of this file and create a `Pipfile` for you.

You can also specify `pipenv install -r path/to/requirements.txt` to import a requirements file.


# Setting up Database

We need to set an environment variable `FLASK_APP` on our machine. The value will be the entry point of our project(in our case it is `app.py`)

Windows Users

`set FLASK_APP=app.py`


Mac/Linux Users

`export FLASK_APP=app.py`


Next, we initialize database using `flask db init`. This will initialize the database and create a `.sqlite` file as well as `migrations` folder.

Next, we migrate our models to database using `flask db migrate`. Finally, we use `flask db upgrade` to apply the changes.

You can refer: https://flask-migrate.readthedocs.io/en/latest/#example for further understanding.


# Running the Flask Application

Windows Users

`python app.py`

Mac/Linux Users

`python3 app.py`


> Congratulations! 🎉 Your Flask application is ready and running @ http://127.0.0.1:5000/
