import json
from urllib import urlencode

class API(object):

    def __init__(self, user, key):
        self.user = user
        self.key = key
        self.prefix = ("%s:%s@http://talk.planethunters."
                       "org/api/comments.json") % (self.user, self.key)

    def parse_comment_list(self, json_string):
        """ Takes a raw JSON blob (string) and returns a list of CommentContainer objects """
        commentContainer = json.loads(json_string)
        raise NotImplementedError()

    def url_from_comment(self, comment):
        """ Takes a Comment object, and turns it in to a HTTP GET compliant URL """
        raise NotImplementedError()

    def url_from_search(self, tags):
        """Tags a set of tags, returns the URL to search the first
        reult page for a search on those coment tags
        """
        result = urlencode({'tag' : tags})
        return self.prefix + '?' + result
