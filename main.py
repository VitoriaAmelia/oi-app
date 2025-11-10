from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="FastAPI",
    description="Simples aplicação FastAPI.",
)

@app.get("/", tags=["Root"], response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>Minha API FastAPI</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f5f5f5;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background: white;
                    padding: 40px;
                    border-radius: 12px;
                    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
                    text-align: center;
                }
                h1 {
                    color: #4CAF50;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 18px;
                    color: #555;
                }
                .btn {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 6px;
                    transition: background 0.3s;
                }
                .btn:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Parabéns!</h1>
                <p>Sua API FastAPI deu certo!</p>
                <a class="btn" href="/hello/Visitante">Diga Olá</a>
            </div>
        </body>
    </html>
    """
    return html_content

@app.get("/hello/{name}", tags=["Exemplo"], response_class=HTMLResponse)
async def say_hello(name: str):
    html_content = f"""
    <html>
        <head>
            <title>Olá {name}</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #e0f7fa;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    background: white;
                    padding: 40px;
                    border-radius: 12px;
                    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
                    text-align: center;
                }}
                h1 {{
                    color: #00796b;
                    margin-bottom: 20px;
                }}
                p {{
                    font-size: 18px;
                    color: #555;
                }}
                .btn {{
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #00796b;
                    color: white;
                    text-decoration: none;
                    border-radius: 6px;
                    transition: background 0.3s;
                }}
                .btn:hover {{
                    background-color: #00695c;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Olá, {name}!</h1>
                <p>Seja bem-vindo à API que deu certo!</p>
                <a class="btn" href="/">Voltar</a>
            </div>
        </body>
    </html>
    """
    return html_content
