from fastapi import APIRouter, HTTPException
from db import get_connection
from models import Departamento


router = APIRouter()

@router.post("/departamento")
async def criar_departamento(dep: Departamento):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO departamento(dnumero, dnome, cpf_gerente, data_inicio_gerente) VALUES (%s. %s, %s, %s)"
            (dep.dnumero, dep.dnome, dep.cpf_gerente, dep.data_inicio_gerente)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Erro ao crirar departamento")
    finally:
        cur.close()
        conn.close()
    return {"msg": "Departamento criado com sucesso"}
        