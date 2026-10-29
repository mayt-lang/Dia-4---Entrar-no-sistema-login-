"""Endpoints relacionados aos usuários."""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import obter_usuario_servico
from app.core.exceptions import ErroDeDominio
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.services.usuario import UsuarioServico

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post(
    "",
    response_model=UsuarioOut,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar usuário",
)
def cadastrar_usuario(
    dados: UsuarioCreate,
    servico: Annotated[UsuarioServico, Depends(obter_usuario_servico)],
):
    try:
        return servico.cadastrar(dados.nome, str(dados.email), dados.senha)
    except ErroDeDominio as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro),
        ) from erro