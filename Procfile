release: python kslab_study.archive/manage.py migrate
web: daphne kslab_study.archive/kslab_study.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python kslab_study.archive/manage.py runworker channels --settings=kslab_study.archive/kslab_study.settings -v2