from fastapi import FastAPI

app = FastAPI(
    title="FastAPI",
    description="Simples aplicação FastAPI.",
)

@app.get("/", tags=["Root"])
async def root():
    return {"message": " Parabéns! Sua API FastAPI deu certo!"}

@app.get("/hello/{name}", tags=["Exemplo"])
async def say_hello(name: str):
    return {"message": f"Olá, {name}! Seja bem-vindo à API que deu certo!"}
