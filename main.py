from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()


@app.get("/llm{pregunta}")
async def read_root(pregunta):
    # Crear una logica que me permita comunicarme con un LLM
    from google import genai

    # The client gets the API key from the environment variable GEMINI_API_KEY.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=pregunta
    )
    print(response.text)




