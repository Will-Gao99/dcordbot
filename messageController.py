import discord
from scraper import Bulbapedia


class MessageController:

    def __init__(self):
        '''
        The username of the author of the message
        Type: string
        '''
        self.author = None

        '''
        The message itself
        Type: string
        '''
        self.message = None

        '''
        The channel the message came from
        Type: string
        '''
        self.channel = None

        '''
        The message object that Discord encodes messages into
        Type: 
        '''
        self.rawMessage = None

    '''
    Returns True if the first n characters of the message are the same as the
    first n characters of the command, where n is the length of the command. 
    Returns False otherwise
    '''
    def _matchCommand(message, command):
        if len(command) > len(message):
            return False
        for i in range(len(command)):
            if command[i] != message[i]:
                return False
        return True

    '''
    Receives a message sent by app.py, populating the fields 
    of the class with the message's metadata. This method also
    contains the branching logic for message processing
    '''
    def receive(self, message):
        self.author = str(message.author).split('#')[0]
        self.message = str(message.content)
        self.channel = str(message.channel.name)
        self.rawMessage = message
        print(f'{self.author}: {self.contents} (Sent in #{self.channel}')

        # User is asking for the Effort Values of a Pokemon
        if _matchCommand(self.message.lower(), "!ev"):
            scraper = Bulbapedia(self.message[4:])
            await self.channel.send(scraper.getEvs())

        # User is asking for a Competitive Set for this Pokemon
        if _matchCommand(self.message.lower(), "!comp"):
            print("Not implemented yet")

        # TODO: Send the help message as a DM or hidden from other users?
        # User is asking for help
        if _matchCommand(self.message.lower(), "!help"):
            with open('help.txt') as f:
                lines = f.readlines()
                f.close()
                output = ""
                for line in lines:
                    output += (line + "\n")
                await self.channel.send(output)