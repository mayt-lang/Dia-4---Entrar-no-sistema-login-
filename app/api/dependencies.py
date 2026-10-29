"""Construção das dependências usadas pelas rotas."""
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.security import HashBcrypt
from app.db.database import obter_sessao
from app.repositories.usuario import UsuarioRepositorio
from app.services.usuario import UsuarioServico


def obter_hasher():
    return HashBcrypt()


def obter_usuario_servico(
    sessao: Session = Depends(obter_sessao),
    hasher=Depends(obter_hasher),
) -> UsuarioServico:
    return UsuarioServico(UsuarioRepositorio(sessao), hasher)