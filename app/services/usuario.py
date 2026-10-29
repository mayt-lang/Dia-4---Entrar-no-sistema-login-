"""Regras de negócio para cadastro de usuários."""
from app.core.exceptions import RegraDeNegocioViolada
from app.core.security import HashDeSenha
from app.models.usuario import Usuario
from app.repositories.usuario import UsuarioRepositorio


class UsuarioServico:
    def __init__(self, repositorio: UsuarioRepositorio, hasher: HashDeSenha):
        self._repositorio = repositorio
        self._hasher = hasher

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        existente = self._repositorio.buscar_por_email(email)
        if existente is not None:
            raise RegraDeNegocioViolada(
                "Já existe uma conta com este e-mail."
            )

        usuario = Usuario(nome=nome, email=email)
        usuario.definir_senha(senha, self._hasher)
        return self._repositorio.salvar(usuario)