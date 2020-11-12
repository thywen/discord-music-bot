import asyncio


class Game:

    def __init__(self, client):
        self.__running = False
        self.questions = 5
        self._client = client
        self._songs = [{'band': 'Metallica', 'song': ''}]
        self._asked = []
        self.scores = {}
        self._channel = {}

    async def start_game(self, channel):
        if self.__running:
            await channel.send('Quiz already started in channel {}, you can stop it with !stop or !halt'
                               .format(self._channel.name))
        else:
            self._channel = channel
            self.__running = True
            await channel.send('@here Quiz starting in 10 seconds...')
            await asyncio.sleep(10)
            await channel.send('Started!')

    async def stop_game(self, channel):
        if self.__running:
            self.__running = False
            await channel.send('Quiz stopped')
        else:
            await channel.send('Why do you want to stop a not running game?')
