from flask import Flask
from flask_restx import Resource, Api
from .model import configure_db, configure_ma
from flask_migrate import Migrate
from .departamentos import ns_dept
from .empregados import ns_emps


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/telacrud.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # configuração de banco
    configure_db(app)
    configure_ma(app)

    # config migrate
    Migrate(app, app.db)

    # blueprints
    from .departamentos import blueprint_departamento
    from .empregados import blueprint_empregados

    app.register_blueprint(blueprint_departamento)
    app.register_blueprint(blueprint_empregados)

    api = Api(
        app,
        version="1.0",
        title="Docs Acmevita, e afins",
        description="Desafio Técnico e Estudos Mutidisciplinares",
    )
    # namespaces
    api.add_namespace(ns_dept)
    api.add_namespace(ns_emps)

    return app


if __name__ == "__main__":
    create_app()
