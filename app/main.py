"""Ponto de entrada da Todo List API."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import usuarios
from app.db.database import criar_tabelas


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    criar_tabelas()
    yield


app = FastAPI(
    title="Todo List API",
    description="Back-end do sistema Todo List.",
    version="0.2.0",
    lifespan=ciclo_de_vida,
)
app.include_router(usuarios.router)


@app.get("/", tags=["Status"], summary="Verificar se a API está no ar")
def raiz() -> dict[str, str]:
    return {"mensagem": "todo-list online", "documentacao": "/docs"}
"""Ponto de entrada da Todo List API."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import usuarios
from app.db.database import criar_tabelas


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    criar_tabelas()
    yield


app = FastAPI(
    title="Todo List API",
    description="Back-end do sistema Todo List.",
    version="0.2.0",
    lifespan=ciclo_de_vida,
)

app.include_router(usuarios.router)


@app.get("/", tags=["Status"], summary="Verificar se a API está no ar")
def raiz() -> dict[str, str]:
    return {"mensagem": "todo-list online", "documentacao": "/docs"}