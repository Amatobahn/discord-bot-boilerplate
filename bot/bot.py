import os
import discord
import asyncio
import configparser
from bot.commands import Command

client = discord.Client()


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
    elif command.startswith('!leet'):
        response = Command.leet_speak(command.replace('!leet', ''))
        yield from client.send_message(message.channel, '{0}'.format(response))


# Set up the base bot
class DiscordBot(object):
    def __init__(self):
        self.token = None
        self.config = configparser.ConfigParser()

    def create_config(self):
        # Ask user for bot token
        self.token = input('Bot Token:')
        # Creates base config file
        self.config.add_section('DiscordBot')
        self.config.set('DiscordBot', 'token', self.token)
        with open('{0}\{1}'.format(os.getcwd(), 'config.ini'), 'w') as configfile:
            self.config.write(configfile)

    def get_token(self):
        self.config.read('{0}\{1}'.format(os.getcwd(), 'config.ini'))
        self.token = self.config.get('DiscordBot', 'token')

    def set_token(self, token):
        self.config.read('{0}\{1}'.format(os.getcwd(), 'config.ini'))
        self.config.set('DiscordBot', 'token', token)
        with open('{0}\{1}'.format(os.getcwd(), 'config.ini'), 'w') as configfile:
            self.config.write(configfile)

    def run(self):
        client.run(self.token)
