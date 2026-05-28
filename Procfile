web: cd catering && python manage.py migrate && python manage.py createsuperuser --noinput || true && gunicorn catering.wsgi --bind 0.0.0.0:$PORT --log-file -
