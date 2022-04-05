# cph22

Repo backing talk at [Django Day CPH 2022](https://2022.djangoday.dk/).

Talk link [here](https://2022.djangoday.dk/talks/joseph/).

## Installation

Set up virtual environment. And then:

```
pip install -r requirements.txt
```

### Database setup

The code by default talks to a postgres instance on a local Docker container. You will have to set that up yourself. Then change the variables within the connection string `DATABASES` setting.

If you want to avoid setting up and just run the code against `sqlite` replace the `DATABASES` setting. Here's the code:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

## Loading sample data

Can be done using `pizzas.tests.utils.load_data` function. This is also used to set up data for unit tests.

Run the below:

```
python manage.py shell_plus
```

In the terminal:

```python
from pizzas.tests.utils import load_data
load_data()
```

## Running tests

```
python manage.py test
```
