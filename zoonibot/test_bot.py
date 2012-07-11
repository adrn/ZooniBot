import os
import json

from mock import MagicMock
import pytest

from bot import ZooniBot, encode_tags
import entry

class TestZoonibot(object):

    def setup_method(self, method):
        try:
            username = os.environ["ZOONAME"]
            api_key = os.environ["ZOOKEY"]
        except KeyError:
            raise KeyError("Zooniverse environment variables not set!")
            
        zoonibot = ZooniBot(username=username, \
                            api_key=api_key)
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
        """ Post should send proper headers and post data to web api """
        zoonibot = self.bot
        stub_urlcls_for_post(zoonibot)

        comment = entry.Comment(body="Testing")
        discussion = entry.Discussion(id="123")
        zooniverse_comment = entry.ZooniverseComment(comment=comment,
                                                     discussion=discussion)

        zoonibot.post(zooniverse_comment)
        args, kwargs = zoonibot.urlcls.Request.call_args
        url = args,
        data = json.loads(kwargs['data'])

        print data
        assert data['comment']['body'] == "Testing"
        assert data['discussion_id'] == "123"

    def test_post_raises_on_bad_status(self):
        zoonibot = self.bot
        stub_urlcls_for_post(zoonibot, fail=True)

        comment = entry.Comment(body="Testing")
        discussion = entry.Discussion(id="123")
        zooniverse_comment = entry.ZooniverseComment(comment=comment,
                                                     discussion=discussion)
        with pytest.raises(ValueError):
            result = zoonibot.post(zooniverse_comment)

    def test_search_comments_parses_results(self):
        """ search method should propery parse json into results """
        zoonibot = self.bot
        stub_urlcls_for_get(zoonibot, SAMPLE_SEARCH)

        result = list(zoonibot.search_comments(tags=['transit']))
        assert zoonibot.urlcls.Request.call_count == 1
        assert len(result) == 2

    def search_comments_url(self, tags):
        zoonibot = self.bot
        stub_urlcls_for_get(zoonibot, EMPTY_SEARCH)

        list(zoonibot.search_comments(tags=tags, since_date="1992-01-01"))
        assert zoonibot.urlcls.Request.call_count == 1

        args, kwargs = zoonibot.urlcls.Request.call_args
        url, = args
        return url

    def test_search_comments_url(self):
        """ search comments should propery parse 1 tag into url """
        base = 'http://talk.planethunters.org/api/comments.json?'
        query = 'page=1&per_page=10&since=1992-01-01&tags=transit'
        assert self.search_comments_url(['transit']) == base + query

    def test_search_comments_url_twotag(self):
        """ search comments should parse 2 tags into url"""
        base = 'http://talk.planethunters.org/api/comments.json?'
        query = 'page=1&per_page=10&since=1992-01-01&tags=transit&tags=test'
        assert self.search_comments_url(['transit', 'test']) == base + query

    def test_search_comments_no_tag(self):
        """ search comments correctly parses no tags """
        base = 'http://talk.planethunters.org/api/comments.json?'
        query = 'page=1&per_page=10&since=1992-01-01'
        assert self.search_comments_url([]) == base + query

def stub_urlcls_for_post(zoonibot, fail=False):
    result = MagicMock()
    result.getcode.return_value = 201 if not fail else 500
    zoonibot.urlcls.urlopen.return_value = result


def stub_urlcls_for_get(zoonibot, result):
    urlopen = MagicMock()
    urlopen.read.return_value = result
    zoonibot.urlcls.urlopen.return_value = urlopen

SAMPLE_SEARCH = """{"results":170,"current_page":2,"total_pages":1,"comments":[{"comment":{"id":"4ffc990dbf45202605000121","body":"Transit? 10.3","created_at":"2012-07-10T21:05:17Z","mentions":[],"tags":[]},"author":{"id":"4f86d2a88307f8793f005def","name":"mr think"},"discussion":{"id":"4f650c4b516bcbfc5c0005be","zooniverse_id":"DPH101b8br","subject":"APH52025083"},"light_curve":{"id":"4f650c4b516bcbfc5c0005bd","zooniverse_id":"APH52025083","tags":[]},"source":{"id":"4d485cc2d2796c0a00033b0d","zooniverse_id":"SPH10025083","tags":[]}},{"comment":{"id":"4ffc98fbbf4520260500011f","body":"Good spot IMO. Looks very unusual! Also like day 11.5 spike/dip ending at ~ day 14 with 3dot drop. ?? Lensing. KID 4078693","created_at":"2012-07-10T21:04:59Z","mentions":[],"tags":[]},"author":{"id":"4f172fcf1740d504290051d8","name":"mjtbarrett"},"discussion":{"id":"4d094a40516bcb90290077ca","zooniverse_id":"DPH1000btx","subject":"APH10102241"},"light_curve":{"id":"4d094a40516bcb90290077c9","zooniverse_id":"APH10102241","tags":["eclipsingbinary"]},"source":{"id":"4d484e86d2796c0a0000853b","zooniverse_id":"SPH10102241","tags":[]}}]}"""

EMPTY_SEARCH = """{"results":0,"current_page":2,"total_pages":0,"comments":[]}"""