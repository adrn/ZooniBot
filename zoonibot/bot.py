""" TODO: Describe this module! """

# Standard Library
import base64
import urllib, urllib2
import json
from time import sleep

# Project
import entry
import zootime


class Bot(object):

    def post(self, comment):
        raise NotImplemented

    def find_and_respond(self, finder, responder, wait=1):
        """ Use finder and responder utilities to respond to comments

            Parameters
            ----------
            finder : function
                A function that returns Comments object
            responder : function
                A function to create 'ZooniverseComment's from an input comment
        """
        for comment in finder(self):
            sleep(wait)
            r = responder(comment)
            self.post(r)

class CommentBot(Bot):

    def __init__(self, username, api_key, base_url):
        """ A bot built specifically to automatically comment on forums

            Parameters
            ----------
            username : string
                The username to connect to the API.
            key : string
                The unique API key for the user specified.
            base_url : string
                The base URL of the site we will be sending requests to.
                e.g. http://<user>:<key>@talk.planethunters.org/api/comments.json
        """
        self.username = username
        self.api_key = api_key
        self.base_url = base_url

class ZooniBot(CommentBot):
    """ The ZooniBot is an automated robot for commenting on Zooniverse
        objects. The ZooniBot is specified by an API key, which is unique
        to the zoonibot user on zooniverse.org. This API key is given to
        the bot by instantiating an API() object, and passing it to bot
        instantiator.
    """

    def __init__(self, username, api_key):
        """ Parameters
            ----------
            username : string
                The username to connect to the API.
            key : string
                The unique API key for the user specified.
        """
        zooni_base_url = "http://talk.planethunters.org/api/comments.json"
        super(ZooniBot, self).__init__(username, api_key, zooni_base_url)
        self.urlcls = None

    def _default_header(self):
        """Form the HTTP header to pass with the POST request"""
        headers = dict()
        headers["Content-Type"] = "application/json"
        base64string = base64.encodestring(
            "{0}:{1}".format(self.username, self.api_key))[:-1]
        headers["Authorization"] = "Basic {0}".format(base64string)
        return headers

    def _get_request(self, url, header=None):
        """ Interface for get requests

        Parameters
        ----------
        url : string of url
        header : dict (optional) header data

        Returns
        -------
        A url response object
        """
        header = header or self._default_header()
        urlcls = self.urlcls or urllib2
        request = urlcls.Request(url, headers=header)
        response = urlcls.urlopen(request)
        return response

    def _post_request(self, data, url=None, header=None):
        """ Interface for post requests

        Parameters
        ----------
        data : dict of post data
        url : optional url to post to (if not base url)
        header : dict (optional) header data

        Returns
        -------
        A url response object
        """
        url = url or self.base_url
        header = header or self._default_header()
        urlcls = self.urlcls or urllib2
        request = urlcls.Request(url, headers=header, data=json.dumps(data))
        response = urlcls.urlopen(request)
        return response

    def post(self, zooniverse_comment):
        """ Post the comment to the Zooniverse by zoonibot

            Parameters
            ----------
            zooniverse_comment : ZooniverseComment
                Posts the specified comment by using the text from
                ZooniverseComment.comment.body and posting to the discussion
                ZooniverseComment.discussion.id

            ..Note::
                Fails if the response code is *not* 201, e.g. 'create'.
        """

        discussion_id = zooniverse_comment.discussion.id
        comment = zooniverse_comment.comment
        data = {"discussion_id" : discussion_id,
                "comment" : {"body" : comment.body}}
        result = self._post_request(data)
        response_code = result.getcode()

        if response_code != 201:
            raise ValueError("Post failed with response code: {}".format(response_code))

    def search_comments(self, tags=None, since_date=None):
        """Return  list of ZooniverseComponents for a comment search"""
        # TODO: check tags to make sure it's a list-like container
        tags = tags or []
        per_page = 10
        since = since_date or '2012-01-01' # or zootime.zoo_yesterday()

        def get_data(page):
            # APW TODO: this is hellish.. maybe we move to
            # using 'request' package?

            data = [('page', page),
                    ('per_page', per_page),
                    ('since', since)]
            data.extend([('tags', t) for t in tags])
            url = "{0}?{1}".format(self.base_url, urllib.urlencode(data))

            response = self._get_request(url).read()
            json_data = json.loads(response)
            return json_data

        json_data = get_data(1)
        total_pages = int(json_data["total_pages"])

        # returns a generator for comment objects
        for comment_dict in json_data["comments"]:
            yield comment_dictionary_to_zooniversecomment(comment_dict)

        for page_number in range(2, total_pages+1):
            json_data = get_data(page_number)

            # returns a generator for comment objects
            for comment_dict in json_data["comments"]:
                yield comment_dictionary_to_zooniversecomment(comment_dict)

def comment_dictionary_to_zooniversecomment(comment_dict):
    """ convert a comment json entry into a ZooniverseComment object"""
    return entry.ZooniverseComment(
        comment=entry.Comment(**comment_dict["comment"]), \
        author=entry.Author(**comment_dict["author"]), \
        discussion=entry.Discussion(**comment_dict["discussion"]), \
        light_curve=entry.LightCurve(**comment_dict["light_curve"]), \
        source=entry.Source(**comment_dict["source"]) \
    )


def encode_tags(tags):
    """ Converts a list of tags to a long &tags=item string
    tags are urlencoded to escape proper characters.
    """
    result = '&'.join([urllib.urlencode({'tags':t}) for t in tags])
    if len(tags) != 0:
        result = '&' + result
    return result
