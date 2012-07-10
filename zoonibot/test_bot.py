from mock import MagicMock

from bot import ZooniBot
import entry

class TestZoonibot(object):

    def setup_method(self, method):
        zoonibot = ZooniBot(username="zoonibot", \
                            api_key="d1b5be9242fb65de9372")
        zoonibot.urlcls = MagicMock() # do not remove! will create posts
        self.bot = zoonibot

    def test_find_and_respond(self):
        """ Find and respond should pass find results through responder, and post"""
        bot = self.bot
        bot.post = MagicMock()

        def finder(x):
            return [1, 2, 3]

        def responder(x):
            return x

        bot.find_and_respond(finder, responder, wait=0)
        assert bot.post.call_count == 3

    def test_post(self):
        """ WARNING! This *actually* creates a post! """
        return True
        zoonibot = self.bot

        # Create a test ZooniverseComment
        comment = entry.Comment(body="Hello world, I am the semi-sentient #ZooniBot")
        discussion = entry.Discussion(id="4f64be222fa49878e700b2e6")
        zooniverse_comment = entry.ZooniverseComment(comment=comment,
                                                     discussion=discussion)
    def test_search_comments_parses_results(self):
        """ """
        # Create a ZooniBot instance
        zoonibot = self.bot

        urlopen = MagicMock()
        urlopen.read.return_value = SAMPLE_SEARCH
        zoonibot.urlcls.urlopen.return_value = urlopen

        result = list(zoonibot.search_comments(tags=['transit']))
        assert zoonibot.urlcls.Request.call_count == 1
        assert len(result) == 2

    def test_search_comments_url(self):
        zoonibot = self.bot

        urlopen = MagicMock()
        urlopen.read.return_value = EMPTY_SEARCH
        zoonibot.urlcls.urlopen.return_value = urlopen
        list(zoonibot.search_comments(tags=['transit']))

        assert zoonibot.urlcls.Request.call_count == 1
        args, kwargs = zoonibot.urlcls.Request.call_args
        url, = args

        header = kwargs['headers']
        assert url.startswith('http://talk.planethunters.org/api/comments.json')
        assert 'tags=transit' in url

    def test_search_comments_url_twotag(self):
        zoonibot = self.bot

        urlopen = MagicMock()
        urlopen.read.return_value = EMPTY_SEARCH
        zoonibot.urlcls.urlopen.return_value = urlopen
        list(zoonibot.search_comments(tags=['transit', 'test']))

        assert zoonibot.urlcls.Request.call_count == 1
        args, kwargs = zoonibot.urlcls.Request.call_args
        url, = args

        header = kwargs['headers']
        assert url.startswith('http://talk.planethunters.org/api/comments.json')
        assert 'tags=transit' in url
        assert 'tags=test' in url

SAMPLE_SEARCH = """{"results":170,"current_page":2,"total_pages":1,"comments":[{"comment":{"id":"4ffc990dbf45202605000121","body":"Transit? 10.3","created_at":"2012-07-10T21:05:17Z","mentions":[],"tags":[]},"author":{"id":"4f86d2a88307f8793f005def","name":"mr think"},"discussion":{"id":"4f650c4b516bcbfc5c0005be","zooniverse_id":"DPH101b8br","subject":"APH52025083"},"light_curve":{"id":"4f650c4b516bcbfc5c0005bd","zooniverse_id":"APH52025083","tags":[]},"source":{"id":"4d485cc2d2796c0a00033b0d","zooniverse_id":"SPH10025083","tags":[]}},{"comment":{"id":"4ffc98fbbf4520260500011f","body":"Good spot IMO. Looks very unusual! Also like day 11.5 spike/dip ending at ~ day 14 with 3dot drop. ?? Lensing. KID 4078693","created_at":"2012-07-10T21:04:59Z","mentions":[],"tags":[]},"author":{"id":"4f172fcf1740d504290051d8","name":"mjtbarrett"},"discussion":{"id":"4d094a40516bcb90290077ca","zooniverse_id":"DPH1000btx","subject":"APH10102241"},"light_curve":{"id":"4d094a40516bcb90290077c9","zooniverse_id":"APH10102241","tags":["eclipsingbinary"]},"source":{"id":"4d484e86d2796c0a0000853b","zooniverse_id":"SPH10102241","tags":[]}}]}"""

EMPTY_SEARCH = """{"results":0,"current_page":2,"total_pages":0,"comments":[]}"""