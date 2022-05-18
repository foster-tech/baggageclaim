web: gunicorn app.wsgi
worker: celery -A app worker -l info -B