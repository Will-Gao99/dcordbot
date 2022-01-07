import discord
import random
import scraper


# Grab token
with open('token.txt') as f:
    lines = f.readlines()
    TOKEN = lines[0]
    f.close()


client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
    if user_message.lower() == "!anywhere":
        await message.channel.send("This can be used anywhere!")
        return
    if user_message[:3].lower()=="!ev":
        print(user_message[4:])
        scraperInstance = scraper.Bulbapedia(user_message[4:]) 
        await message.channel.send(scraperInstance.search())
              
            
if (__name__ == "__main__"):
    client.run(TOKEN)

