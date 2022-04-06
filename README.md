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

## Talk References

### Django docs

* [Database access optimization](https://docs.djangoproject.com/en/dev/topics/db/optimization/)
* [Model managers](https://docs.djangoproject.com/en/dev/topics/db/managers/)
* queryset [prefetch_related](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#prefetch-related) and [select_related](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.select_related)
* [queryset conditional expressions](https://docs.djangoproject.com/en/dev/ref/models/conditional-expressions/)
* [queryset aggregation](https://docs.djangoproject.com/en/4.0/topics/db/aggregation/)
* [assertNumQueries](https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries)

### Third-party Packages

* [django-extensions](https://django-extensions.readthedocs.io/en/latest/index.html), for `manage.py shell_plus --print-sql`
* [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)

### Related Articles & Blog posts

* [Lindy Effect](https://en.wikipedia.org/wiki/Lindy_effect) - Wikipedia
* [An Expert Called Lindy](https://medium.com/incerto/an-expert-called-lindy-fdb30f146eaf) by Nassim Taleb
* [Tips for Using Django's ManyToManyField](https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/) by Lacey Williams Henschel
* [Django and the N+1 Queries Problem](https://scoutapm.com/blog/django-and-the-n1-queries-problem) by [Adam Johnson](https://adamj.eu/)
* [Pushing the Django ORM to its limits](https://medium.com/oda-product-tech/pushing-the-orm-to-its-limits-d26d87a66d28) by Sigurd Ljødal

### Postgres-specific articles

* [PostgreSQL execution plan operations](https://use-the-index-luke.com/sql/explain-plan/postgresql/operations)
* [Five Tips For a Healthier Postgres Database in the New Year](https://blog.crunchydata.com/blog/five-tips-for-a-healthier-postgres-database-in-the-new-year) by Craig Kerstiens
* [What is a "Bitmap heap scan" in a query plan?](https://stackoverflow.com/a/6592963/1211429)

### Tools used

* For framing code snippets: [carbon](https://carbon.now.sh/)
* For diagrams: [excalidraw](https://excalidraw.com/)

Both free to use at time of writing.
