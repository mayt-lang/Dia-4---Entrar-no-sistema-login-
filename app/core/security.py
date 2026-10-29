"""Contrato e implementação de hash de senhas."""
from abc import ABC, abstractmethod
import bcrypt

LIMITE_BYTES_SENHA = 72


class HashDeSenha(ABC):
    """Contrato para gerar e verificar hashes de senha."""

    @abstractmethod
    def gerar(self, senha: str) -> str:
        """Gera um hash seguro para a senha."""

    @abstractmethod
    def verificar(self, senha: str, hash_armazenado: str) -> bool:
        """Confere uma senha com um hash já armazenado."""


class HashBcrypt(HashDeSenha):
    """Implementação usando bcrypt."""

    def gerar(self, senha: str) -> str:
        senha_bytes = senha.encode("utf-8")
        if len(senha_bytes) > LIMITE_BYTES_SENHA:
            raise ValueError("A senha não pode ultrapassar 72 bytes em UTF-8.")
        return bcrypt.hashpw(senha_bytes, bcrypt.gensalt()).decode("utf-8")

    def verificar(self, senha: str, hash_armazenado: str) -> bool:
        senha_bytes = senha.encode("utf-8")
        if len(senha_bytes) > LIMITE_BYTES_SENHA:
            return False
        try:
            return bcrypt.checkpw(senha_bytes, hash_armazenado.encode("utf-8"))
        except (ValueError, TypeError):
            return False