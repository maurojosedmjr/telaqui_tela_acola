import json
from typing import Dict, Tuple


def recuperar_dados(session, model, filtro=None) -> Tuple[Dict[str, str], int]:
    query = session.query(model)
    try:
        if filtro:
            return query.filter(filtro), 200
        return query.all(), 200
    except Exception as err:
        print(str(err))
        return {"error": "Algo deu errado. Contate o suporte."}, 400


def inserir_linha(session, model, data) -> Tuple[Dict[str, str], int]:
    try:
        session.add(model(**data))
        session.commit()
    except Exception as err:
        print(str(err))
        return {"error": "Algo deu errado. Contate o suporte."}, 304
    return {
        "success": f"Registro {json.dumps(data)} inserido com sucesso no modelo {model.__name__}."
    }, 201
