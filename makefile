TEST_PATH=./

clean-pyc:
    find . -name '*.pyc' -exec rm --force {} +
    find . -name '*.pyo' -exec rm --force {} +
    find . -name '*~' -exec rm --force  {} +

clean-build:
    rm --force --recursive build/
    rm --force --recursive dist/
    rm --force --recursive *.egg-info

isort:
    sh -c "isort --skip-glob=.tox --recursive . "

lint:
    flake8 --exclude=.tox

test: clean-pyc
    py.test --verbose --color=yes $(TEST_PATH)

run:
    python manage.py runserver

docker-run:
    docker build \
      --file=./Dockerfile \
      --tag=my_project ./
    docker run \
      --detach=false \
      --name=my_project \
      --publish=$(HOST):8080 \
      my_project
