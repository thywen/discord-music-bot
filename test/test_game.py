from pytest import fixture, mark
from unittest.mock import AsyncMock, Mock

from game.game import Game


# class AsyncMock(MagicMock):
#     async def __call__(self, *args, **kwargs):
#         return super(AsyncMock, self).__call__(*args, **kwargs)


@fixture
def game_fixture():
    mock_client = Mock()
    return Game(mock_client)


def test_game_not_running_when_initialised(game_fixture):
    assert game_fixture.game_running() is False


@mark.asyncio
async def test_start_game_sets_game_to_started(game_fixture):
    mock_channel = AsyncMock()
    await game_fixture.start_game(mock_channel)

    mock_channel.send.assert_called_with('@here Quiz starting in 10 seconds...')
    assert game_fixture.game_running() is True


@mark.asyncio
async def test_game_sends_message_and_stops_game(game_fixture):
    mock_channel = AsyncMock()
    await game_fixture.start_game(mock_channel)
    await game_fixture.stop_game(mock_channel)

    mock_channel.send.assert_called_with('Quiz stopped')
    assert game_fixture.game_running() is False


@mark.asyncio
async def test_does_not_stop_if_not_started(game_fixture):
    mock_channel = AsyncMock()
    await game_fixture.stop_game(mock_channel)

    mock_channel.send.assert_called_with("Why do you want to stop a not running game?")
    assert game_fixture.game_running() is False


@mark.asyncio
async def test_unable_to_start_twice(game_fixture):
    mock_channel = AsyncMock()
    mock_channel.name = "test_channel"
    print(mock_channel.name)
    await game_fixture.start_game(mock_channel)
    await game_fixture.start_game(mock_channel)

    mock_channel\
        .send.assert_called_with("Quiz already started in channel test_channel, you can stop it with !stop")
    assert game_fixture.game_running() is True
