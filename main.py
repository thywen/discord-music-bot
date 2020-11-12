import discord
import os

from game.game import Game

TOKEN = os.environ.get("BOT_TOKEN")

client = discord.Client()
game = Game(client)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!start'):
        await game.start_game(message.channel)
    if message.content.startswith('!stop'):
        await game.stop_game(message.channel)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


if __name__ == '__main__':
    client.run(TOKEN)

