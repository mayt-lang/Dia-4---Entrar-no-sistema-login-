"""Leitura e validação da configuração da aplicação."""
from dataclasses import dataclass
from functools import lru_cache
import os

from dotenv import load_dotenv

load_dotenv()


class ConfiguracaoInvalida(RuntimeError):
    """Erro lançado quando uma configuração obrigatória está ausente."""


@dataclass(frozen=True)
class Configuracao:
    """Configuração imutável da aplicação."""
    database_url: str = ""

    @classmethod
    def do_ambiente(cls) -> "Configuracao":
        return cls(database_url=os.getenv("DATABASE_URL", "").strip())

    @property
    def url_banco(self) -> str:
        if not self.database_url:
            raise ConfiguracaoInvalida(
                "DATABASE_URL não foi definida. Copie .env.example para .env e configure o banco."
            )
        return self.database_url


@lru_cache(maxsize=1)
def obter_configuracao() -> Configuracao:
    return Configuracao.do_ambiente()