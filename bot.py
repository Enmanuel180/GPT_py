import discord
import response


def run_discord_bot():
    TOKEN = 'MTA5NzI2NjgyNzI3NDUwMjMwNQ.Gu50be.DD1bzQpa728dJ00xWqCq3AcgSMPzNW1nCzNWs8'
    intents = discord.Intents.default()
    intents.message_content = True
    # ADD CLIENT DISCORD
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    client.run(TOKEN)