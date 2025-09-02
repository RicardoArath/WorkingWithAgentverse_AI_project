# models.py
from uagents import Model

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
