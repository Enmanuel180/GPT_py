import discord
import response


def run_discord_bot():
    TOKEN = 'discord token'
    intents = discord.Intents.default()
    intents.message_content = True
    # ADD CLIENT DISCORD
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        user_name = message.author
        content = message.content
        channel = message.channel
        if 'CHATGPT:' in content:
            try:
                responses = response.chatgpt_response(user_name, content)
                await channel.send(responses)
            except Exception as error:
                print(error)
    client.run(TOKEN)