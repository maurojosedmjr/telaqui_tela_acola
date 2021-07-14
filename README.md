
Rodando Docker:
```shell
make build
make run
```

Rodando local-Dev:
```shell
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

Migrations:
```shell
flask db init
flask db migrate
flask db upgrate
```