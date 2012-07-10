import pytest

from urllib import urlencode

from api import API

class TestAPI(object):

    def test_parse_comment_list(self):
        """ Make sure a JSON string turns into the correct Python objects """
        pass

    def test_url_from_comment(self):
        pass

    def test_url_from_search(self):
        """should return the correct list of urls, 1 for each page"""
        api = API('user', 'key')
        tag = 'hello'
        result = api.url_from_search(tag)
        expected = "user:key@http://talk.planethunters.org/api/comments.json?tag=hellogit"
        assert result == expected