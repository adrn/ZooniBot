from mock import MagicMock

from bot import ZooniBot

def test_find_and_respond():
    user = "test"
    key = "test"
    bot = ZooniBot(user, key)
    bot.post = MagicMock

    def finder():
        return [1, 2, 3]

    def responder(x):
        return x

    bot.find_and_respond(finder, responder)
    assert bot.post.call_count == 3

