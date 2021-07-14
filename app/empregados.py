from flask import Blueprint, current_app, request
from flask_restx import Resource, Namespace, fields
from .model import Departamento, DepartamentoSchema, Empregado, EmpregadoSchema
from typing import Dict, Tuple
from .db_controllers import recuperar_dados, inserir_linha
import json

blueprint_empregados = Blueprint("empregados", __name__)

ns_emps = Namespace("empregados", description="Manipulação de Empregados")

empregado = ns_emps.model(
    "Empregado",
    {
        "nome_completo": fields.String(
            required=True, description="Nome completo do empregado"
        ),
        "dpt_id": fields.Integer(required=True, description="Id do departamento"),
        "dependentes": fields.String(
            description="Nome dos dependentes separado por vírgula"
        ),
    },
)


@ns_emps.route("/")
class Empregados(Resource):
    @ns_emps.doc("lista os empregados")
    def get(self):
        session = current_app.db.session
        lista_de_empregados, status_code = recuperar_dados(session, Empregado)
        return [emp.to_json() for emp in lista_de_empregados], status_code

    # @blueprint_departamento.route("/departamentos/cadastrar", methods=["POST"])
    @ns_emps.doc("insere empregado")
    @ns_emps.expect(empregado)
    def post(self):
        session = current_app.db.session
        schema = EmpregadoSchema()
        empregado_data: Dict[str, str] = schema.load(data=json.loads(request.data))
        resultado: Tuple[Dict[str, str], int] = inserir_linha(
            session, Empregado, empregado_data
        )
        return resultado