from mock import MagicMock

from bot import ZooniBot
import entry

def test_find_and_respond():
    user = "test"
    key = "test"
    bot = ZooniBot(user, key)
    bot.post = MagicMock()

    counts = 0
    def post(x):
        global counts
        counts += 1

    def finder(x):
        return [1, 2, 3]

    def responder(x):
        return x

    bot.find_and_respond(finder, responder, wait=0)
    assert bot.post.call_count == 3

class TestZoonibot(object):

    def test_post(self):
        """ WARNING! This *actually* creates a post! """
        return True
        # Create a ZooniBot instance 
        zoonibot = ZooniBot(username="zoonibot", \
                            api_key="d1b5be9242fb65de9372")

        # Create a test ZooniverseComment
        comment = entry.Comment(body="Hello world, I am the semi-sentient #ZooniBot")
        discussion = entry.Discussion(id="4f64be222fa49878e700b2e6")

        zooniverse_comment = entry.ZooniverseComment(comment=comment, discussion=discussion)
        zoonibot.post(zooniverse_comment)
        
    def test_search_comments(self):
        """ """
        
        # Create a ZooniBot instance 
        zoonibot = ZooniBot(username="zoonibot", \
                            api_key="d1b5be9242fb65de9372")
        
        comment_generator = zoonibot.search_comments(tags=["planet"])
        
        comments = []
        for comment in comment_generator:
            comments.append(comment)
        
        assert len(comments) > 0