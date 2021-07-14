from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from datetime import datetime

db = SQLAlchemy()
ma = Marshmallow()


def configure_db(app):
    db.init_app(app)
    app.db = db


def configure_ma(app):
    ma.init_app(app)


class CamposDefault:
    created_at = db.Column(db.DateTime, default=datetime.now())
    last_modified = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now()
    )


class Departamento(db.Model, CamposDefault):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), unique=True)

    def to_json(self):
        return {"id": self.id, "nome": self.nome}


class DepartamentoSchema(ma.Schema):
    class Meta:
        model = Departamento

    nome = fields.Str(required=True)


class Empregado(db.Model, CamposDefault):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(150), unique=True)
    dependentes = db.Column(db.String(300))
    dpt_id = db.Column(db.Integer, db.ForeignKey(Departamento.id), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome_completo,
            "departamento": self.dpt_id,
            "have_dependents": True if self.dependentes else False,
        }


class EmpregadoSchema(ma.Schema):
    class Meta:
        model = Empregado

    nome_completo = fields.Str(required=True)
    dependentes = fields.Str()
    dpt_id = fields.Integer(required=True)