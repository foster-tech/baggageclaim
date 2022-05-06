# Baggage Claim

## How to run

1. Run `pipenv install`;
2. Change the python runtime on VSCode or run `pipenv shell`;
3. Run `python manage.py migrate` inside the environment;
4. Click the start button on Debug session of VSCode or run `python manage.py runserver`;
5. Open `localhost:8000` in your browser.

## Extras

- Create admin user with `python manage.py createsuperuser`;
- Refresh static files `python manage.py collectstatic`
