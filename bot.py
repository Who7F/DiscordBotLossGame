import discord
import responses

async def sendMessage(message, userMessage, isPrivate):
    try:
        response = responses.handleRespomse
        await message.author,send(response) if isPrivate else await message.channal.sent(response)
    except Exception as e:
        print(e)

def runDiscordBot(TOKEN):
    
    intents=discord.Intents.default()
    
    intents.message_content = True
    
    client = discord.Client(intents=intents)
    
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        userName = str(message.author)
        userMessage = str(message.content)
        channal = str(message.channel)

        print(f'{userName} said: {userMessage} in: {channal}')
        print(message.content)

    client.run(TOKEN)
    
