# main.py
from uagents import Agent, Context
from openai import OpenAI
import os
from models import StudentMessage, NORMAS

# =====================================================
# Configuración del cliente Fetch.ai
# =====================================================
client = OpenAI(
    base_url="https://api.fetch.ai/v1",   
    api_key=os.getenv("OPENAI_API_KEY")  
)

# =====================================================
# Agente universitario
# =====================================================
agent = Agent(
    name="university_agent",
    port=8000,
    seed="reglamento_universidad",
    endpoint=["http://127.0.0.1:8000/submit"]
)

@agent.on_message(model=StudentMessage)
async def handle_message(ctx: Context, sender: str, msg: StudentMessage):
    ctx.logger.info(f"📩 Mensaje recibido: {msg.message}")

    prompt = f"""
Estas son las normas de la universidad (clasificadas en menor y mayor):

Normas menores:
{chr(10).join(NORMAS['menores'])}

Normas mayores:
{chr(10).join(NORMAS['mayores'])}

El estudiante escribió: "{msg.message}"

Pregunta: ¿Esta falta corresponde a una norma menor o mayor?
Responde SOLO con 'menor' o 'mayor'.
"""

    response = client.chat.completions.create(
        model="asimov-one-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    gravedad = response.choices[0].message.content.strip().lower()
    ctx.logger.info(f"🤖 Respuesta del LLM: {gravedad}")

    if "menor" in gravedad:
        ctx.logger.info("✅ Norma menor → preparar correo base.")
    elif "mayor" in gravedad:
        ctx.logger.info("⚠️ Norma mayor → agendar cita en Google Calendar.")
    else:
        ctx.logger.info("🤔 No se pudo clasificar.")

if __name__ == "__main__":
    agent.run()
