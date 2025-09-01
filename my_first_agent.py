from uagents import Agent, Context

alice = Agent(name="Alice", seed="alice recovery phrase")

@alice.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'Hello my name is {alice.name}')

if __name__ == "__main__":
    alice.run()