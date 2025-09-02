# student_agent.py
from uagents import Agent, Context
from models import StudentMessage
import random

# Dirección del agente universitario (sacado de logs de main.py)
UNIVERSITY_AGENT_ADDRESS = "agent1qdf5eexy8dvvznntfsuefwxmyypej2sqxj909vnxywswwl929cf5us6a69d"

MESSAGES = [
    "Llegué 5 minutos tarde a clase",
    "No usé la gorra en clase",
    "Falté al examen sin justificación",
    "Cometí plagio en el trabajo final",
    "Llegué tarde a la biblioteca",
    "No entregué la tarea a tiempo"
]

student_agent = Agent(
    name="student_agent",
    port=8001,
    seed="student123",
    endpoint=["http://127.0.0.1:8001/submit"]
)

@student_agent.on_interval(period=10.0)
async def send_message(ctx: Context):
    msg_text = random.choice(MESSAGES)
    msg = StudentMessage(message=msg_text)
    await ctx.send(UNIVERSITY_AGENT_ADDRESS, msg)
    ctx.logger.info(f"📨 Mensaje enviado al agente universitario: {msg_text}")

if __name__ == "__main__":
    student_agent.run()
