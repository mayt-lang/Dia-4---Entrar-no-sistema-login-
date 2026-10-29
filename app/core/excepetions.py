class ErroDeDominio(Exception):
    """Classe base de todo erro previsto de negócio."""

    mensagem = "Não foi possível concluir a operação."

    def __init__(self, mensagem: str | None = None) -> None:
        self.mensagem = mensagem or type(self).mensagem
        super().__init__(self.mensagem)


class RegraDeNegocioViolada(ErroDeDominio):
    """A operação é compreensível, mas contraria uma regra de negócio."""

    mensagem = "Operação recusada por uma regra de negócio."


class ValorInvalido(RegraDeNegocioViolada):
    """Valor fora do conjunto aceito para um campo do domínio."""

    mensagem = "Valor inválido para o campo."