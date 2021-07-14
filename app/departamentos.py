from flask import Blueprint, current_app, request
from flask_restx import Resource, Namespace, fields
from .model import Departamento, DepartamentoSchema
from typing import Dict, Tuple
from .db_controllers import recuperar_dados, inserir_linha
import json

blueprint_departamento = Blueprint("departamentos", __name__)

ns_dept = Namespace("departamentos", description="Manipulação de Departamentos")

departamento = ns_dept.model(
    "Departamento",
    {
        "nome": fields.String(required=True, description="Nome do departamento"),
    },
)


# @blueprint_departamento.route("/departamentos/listar", methods=["GET"])
@ns_dept.route("/")
class Departamentos(Resource):
    @ns_dept.doc("lista os departamentos")
    def get(self):
        session = current_app.db.session
        lista_de_departamentos, status_code = recuperar_dados(session, Departamento)

        return [dept.to_json() for dept in lista_de_departamentos], status_code


    # @blueprint_departamento.route("/departamentos/cadastrar", methods=["POST"])
    @ns_dept.doc("insere departamento")
    @ns_dept.expect(departamento)
    def post(self):
        session = current_app.db.session
        schema = DepartamentoSchema()
        departamento_data: Dict[str, str] = schema.load(data=json.loads(request.data))
        resultado: Tuple[Dict[str, str], int] = inserir_linha(
            session, Departamento, departamento_data
        )
        return resultado
