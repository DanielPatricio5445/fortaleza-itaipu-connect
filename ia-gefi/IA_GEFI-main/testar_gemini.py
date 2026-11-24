
import os
from openai import OpenAI

cliente = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

modelos = cliente.models.list()

for modelo in modelos.data:
    if "gemini" in modelo.id.lower():
        print(modelo.id)
