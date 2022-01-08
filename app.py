from messageController import MessageController
import discord
import random

'''
This file is the entrance point of our Discord Bot. It contains the routes/listeners
through which the bot receives stimulus. Upon receiving an input, the application
will delegate the handling of the input to its respective controller.
'''

def main():
    # Grabs the authentication token from token.txt
    with open('token.txt') as f:
        lines = f.readlines()
        TOKEN = lines[0]
        f.close()

    # Instantiates the client-side bot
    client = discord.Client()
    #Instantiates messageController
    messageController = MessageController()

    # Runs the client with the auth token, connecting to the server
    client.run(TOKEN)
    
    '''
    Begin listeners
    '''
    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        else:
            await messageController.receive(message)
              

def test():
    messageController = MessageController()
    print("Hello")


if (__name__ == "__main__"):
    #main()
    test()

