FROM python:3.14.3-slim

WORKDIR /app

# Instala o FastAPI, servidor Uvicorn e o Protobuf
RUN pip install --no-cache-dir fastapi uvicorn betterproto

# Expõe a porta que você escolheu
EXPOSE 9300

# O --host 0.0.0.0 é OBRIGATÓRIO para acessar de outro PC na rede
CMD ["uvicorn", "back_end.main:app", "--host", "0.0.0.0", "--port", "9300", "--reload"]