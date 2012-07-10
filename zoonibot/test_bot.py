from mock import MagicMock

from bot import ZooniBot
import entry

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

class TestZoonibot(object):

    def test_post(self):
        """ WARNING! This *actually* creates a post! """

        # Create a ZooniBot instance
        zoonibot = ZooniBot(username="zoonibot", \
                            api_key="d1b5be9242fb65de9372")

        # Create a test ZooniverseComment
        comment = entry.Comment(body="Hello world, I am the semi-sentient #ZooniBot")
        discussion = entry.Discussion(id="4f64be222fa49878e700b2e6")

        zooniverse_comment = entry.ZooniverseComment(comment=comment, discussion=discussion)
        zoonibot.post(zooniverse_comment)

