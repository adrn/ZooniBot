import json

class API(object):

    def __init__(self, key, base_url):
        pass

    def parse_comment_list(self, json_string):
        """ Takes a raw JSON blob (string) and returns a list of CommentContainer objects """
        commentContainer = json.loads(json_string)
        raise NotImplementedError()

    def url_from_comment(self, comment):
        """ Takes a Comment object, and turns it in to a HTTP GET compliant URL """
        raise NotImplementedError()

    def url_from_search(self, tags):
        """ Takes a comment tag name(s) and produces an HTTP GET request URL """
        raise NotImplementedError()