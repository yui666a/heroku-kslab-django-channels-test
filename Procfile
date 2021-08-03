release: python kslab_study/manage.py migrate
web: daphne kslab_study.kslab_study.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python kslab_study/manage.py runworker channels --settings=kslab_study/kslab_study.settings -v2