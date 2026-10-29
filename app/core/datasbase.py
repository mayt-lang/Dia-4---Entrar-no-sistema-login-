
"""Conexão com o banco de dados e gerenciamento de sessões."""
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import obter_configuracao


def _opcoes_do_engine(url: str) -> dict:
    """Retorna as opções específicas para cada banco de dados."""
    if url.startswith("sqlite"):
        return {
            "connect_args": {"check_same_thread": False},
            "poolclass": StaticPool,
        }
    return {"pool_pre_ping": True}


_url = obter_configuracao().url_banco

engine = create_engine(
    _url,
    echo=False,
    **_opcoes_do_engine(_url),
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def criar_tabelas() -> None:
    """Cria as tabelas dos modelos registrados."""
    import app.models

    Base.metadata.create_all(bind=engine)


def obter_sessao() -> Generator:
    """Entrega uma sessão e garante seu fechamento."""
    sessao = SessionLocal()
    try:
        yield sessao
    finally:
        sessao.close()
