release: python manage.py migrate
web: daphne kslab_study.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=kslab_study.settings -v2