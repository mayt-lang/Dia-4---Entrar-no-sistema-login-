# Todo List API

API feita em Python com FastAPI para iniciar o cadastro de usuários.

## Requisitos
- Python 3.11 ou superior
- Git (opcional)

## Instalação no Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Se o PowerShell bloquear a ativação do ambiente, execute os comandos de instalação usando o terminal configurado no seu computador.

## Executar

```powershell
uvicorn app.main:app --reload
```

Abra http://127.0.0.1:8000 para verificar a API e http://127.0.0.1:8000/docs para testar o cadastro.

## Cadastro

`POST /usuarios` recebe `nome`, `email` e `senha`. A senha é armazenada como hash e não é devolvida na resposta.

Exemplo de JSON:

```json
{
  "nome": "Kennedy",
  "email": "kennedy@exemplo.com",
  "senha": "senha123"
}
```

## Testes

```powershell
pytest -q
```

O arquivo `.env` e o banco local `todo_list.db` são ignorados pelo Git. Não envie senhas ou credenciais reais ao repositório.
