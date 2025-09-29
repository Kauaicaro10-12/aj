# railway-job-backend

Backend FastAPI simples para envio e recebimento de JobId, pronto para deploy no Railway.

## Como usar

1. Clone este repositório.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Rode localmente para testar:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
4. Faça deploy no [Railway](https://railway.app/) conectando este repositório.

## Endpoints

- `POST /job` — Atualiza o JobId
- `GET /job` — Retorna o JobId mais recente
