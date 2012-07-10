import pytest

from urllib import urlencode

from api import API

class TestAPI(object):

    def setup_method(self, method):
        self.user = 'zoonibot'
        self.key = 'd1b5be9242fb65de9372'
        self.api = API(self.user, self.key)
        self.prefix = ("http://%s:%s@talk.planethunters."
                       "org/api/comments.json") % (self.user, self.key)

    def test_parse_comment_list(self):
        """ Make sure a JSON string turns into the correct Python objects """
        pass

    def test_url_from_comment(self):
        pass

    def test_url_from_search(self):
        """should return the correct list of urls, 1 for each page"""
        tag = 'hello'
        results = self.api.url_from_search([tag])
        expected_pages = 10
        assert len(results) == expected_results

        for i, result in enumerate(results):
            tag = urlencode({'page':i, 'tag': tag})
            url = self.prefix+'?'+tag
            assert result == url
