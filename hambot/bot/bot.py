import os
import discord
import asyncio
import configparser
from bot.commands import Command
from chatterbot import ChatBot as Chatterbot

client = discord.Client()

cb = Chatterbot('NLTK', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
cb.train('chatterbot.corpus.english')


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as: {0} - {1}'.format(client.user.name, client.user.id))
    print('-'*20)


@client.event
@asyncio.coroutine
def on_message(message):
    command = message.content.lower()
    if message.author == client.user:
        return
    elif command == '!':
        yield from client.send_message(message.channel, '<@{0}>, No command has been passed.'.format(message.author.id))

    # Utilities
    elif command.startswith('!shorten'):
        response = Command.url_shorten(command)
        yield from client.send_message(message.channel, '<@{0}>, your requested url: {1}'.format(message.author.id,
                                                                                                 response))
    # Troll Commands
    elif command.startswith('!leet'):
        response = Command.leet_speak(command)
        yield from client.send_message(message.channel, '{0}'.format(response))
    elif command.startswith('!joke'):
        response = Command.get_dad_joke()
        yield from client.send_message(message.channel, '<@{0}> {1}'.format(message.author.id, response))
    elif any(substring in command for substring in ('livepd', 'live pd')):
        yield from client.send_message(message.channel, "That is <@{0}>'s favorite show.".format('203288765068738562'))
    else:
        yield from client.send_message(message.channel, '{0}'.format(cb.get_response(command)))


# Set up the base bot
class HamBot(object):
    def __init__(self):
        self.token = None
        self.config = configparser.ConfigParser()

    def create_config(self):
        # Ask user for bot token
        self.token = input('Bot Token:')
        # Creates base config file
        self.config.add_section('HamBot')
        self.config.set('HamBot', 'token', self.token)
        with open('{0}\{1}'.format(os.getcwd(), 'config.ini'), 'w') as configfile:
            self.config.write(configfile)

    def get_token(self):
        self.config.read('{0}\{1}'.format(os.getcwd(), 'config.ini'))
        self.token = self.config.get('HamBot', 'token')

    def set_token(self, token):
        self.config.read('{0}\{1}'.format(os.getcwd(), 'config.ini'))
        self.config.set('HamBot', 'token', token)
        with open('{0}\{1}'.format(os.getcwd(), 'config.ini'), 'w') as configfile:
            self.config.write(configfile)

    def run(self):
        client.run(self.token)
