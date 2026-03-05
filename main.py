from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from ./static if the folder exists
if os.path.isdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    return {"status": "ok"}


@app.get("/llm")
async def llm_endpoint(pregunta: str):
    # Lógica para comunicarse con el LLM
    from google import genai

    # The client gets the API key from the environment variable GEMINI_API_KEY.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=pregunta
    )

    # Extraer texto de la respuesta y devolver como JSON para el frontend
    text = getattr(response, "text", None)
    if text is None:
        text = str(response)

    return JSONResponse(content={"respuesta": text})




