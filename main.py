from uagents import Agent, Context, Model
from llm_client import query_llm

# =====================================================
# Modelo de mensaje
# =====================================================
class StudentMessage(Model):
    message: str

# Normas de ejemplo
NORMAS = {
    "menores": [
        "No usar gorra en clase",
        "Llegar 5 minutos tarde"
    ],
    "mayores": [
        "Plagio",
        "Faltar examen sin justificar"
    ]
}

# =====================================================
# Agente
# =====================================================
agent = Agent(
    name="university_agent",
    seed="reglamento_universidad",
    endpoint=["http://127.0.0.1:8000/submit"]
)

@agent.on_message(model=StudentMessage)   # ✅ aquí va el modelo
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

    gravedad = query_llm(prompt).lower()
    ctx.logger.info(f"🤖 Respuesta del LLM: {gravedad}")

    if "menor" in gravedad:
        ctx.logger.info("✅ Norma menor → preparar correo base.")
    elif "mayor" in gravedad:
        ctx.logger.info("⚠️ Norma mayor → agendar cita en Google Calendar.")
    else:
        ctx.logger.info("🤔 No se pudo clasificar.")

if __name__ == "__main__":
    agent.run()
