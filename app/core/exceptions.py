"""Exceções independentes de HTTP para as regras de negócio."""


class ErroDeDominio(Exception):
    """Classe base para erros do domínio."""
    mensagem = "Ocorreu um erro de domínio."

    def __init__(self, mensagem: str | None = None):
        super().__init__(mensagem or self.mensagem)


class RegraDeNegocioViolada(ErroDeDominio):
    """Indica que uma regra de negócio foi desrespeitada."""
    mensagem = "Uma regra de negócio foi desrespeitada."


class ValorInvalido(RegraDeNegocioViolada):
    """Indica que um valor informado não é válido."""
    mensagem = "O valor informado é inválido."