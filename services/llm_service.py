import requests

class LLMService:

    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def responder_contextual(self, pergunta, contexto):

        prompt = f"""
Você é um assistente financeiro.

Use exclusivamente os dados abaixo para responder.

{contexto}

Pergunta: {pergunta}

Se a resposta não estiver nos dados, diga que não encontrou.
"""

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]