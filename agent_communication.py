from uagents import Agent, Bureau, Context, Model

class Message(Model):
    message: str

alice = Agent(name="alice")
bob = Agent(name="bob")

@alice.on_interval(period=3.0)
async def send_message(ctx: Context):
    await ctx.send(bob.address, Message(message="Hello there Bob!"))

@alice.on_message(model=Message)
async def alice_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

@bob.on_message(model=Message)
async def bob_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    await ctx.send(alice.address, Message(message="Hello there Alice!"))

bureau = Bureau()
bureau.add(alice)
bureau.add(bob)

if __name__ == "__main__":
    bureau.run()