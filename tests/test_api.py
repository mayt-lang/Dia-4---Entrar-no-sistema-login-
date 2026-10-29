"""Testes dos endpoints HTTP."""


def test_rota_raiz(cliente):
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert resposta.json()["mensagem"] == "todo-list online"


def test_cadastrar_usuario(cliente):
    resposta = cliente.post(
        "/usuarios",
        json={
            "nome": "Kennedy",
            "email": "KENNEDY@EXEMPLO.COM",
            "senha": "senha123",
        },
    )

    assert resposta.status_code == 201
    dados = resposta.json()
    assert dados["nome"] == "Kennedy"
    assert dados["email"] == "kennedy@exemplo.com"
    assert "senha" not in dados
    assert "senhaHash" not in dados
    assert "criadoEm" in dados


def test_cadastro_rejeita_dados_invalidos(cliente):
    resposta = cliente.post(
        "/usuarios",
        json={
            "nome": "Kennedy",
            "email": "email-invalido",
            "senha": "123",
        },
    )
    assert resposta.status_code == 422


def test_nao_permite_email_repetido(cliente):
    dados = {
        "nome": "Kennedy",
        "email": "k@exemplo.com",
        "senha": "senha123",
    }

    assert cliente.post("/usuarios", json=dados).status_code == 201
    resposta = cliente.post("/usuarios", json=dados)
    assert resposta.status_code == 409