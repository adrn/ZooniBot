""" TODO: Describe this module! """

# Standard Library
import base64
import urllib, urllib2
import json
from time import sleep

# Project
import entry

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
        data = {"discussion_id" : discussion_id, "comment" : {"body" : comment.body}}

        # Form the HTTP header to pass with the POST request
        headers = dict()
        headers["Content-Type"] = "application/json"
        base64string = base64.encodestring("{}:{}".format(self.username, self.api_key))[:-1]
        headers["Authorization"] = "Basic {}".format(base64string)

        # Create the request object with the necessary header and JSON data declarations
        request = urllib2.Request(self.base_url, headers=headers, data=json.dumps(data))
        response = urllib2.urlopen(request)
        response_code = response.getcode()

        if response_code != 201:
            raise ValueError("Post failed with response code: {}".format(response_code))

    def search_comments(self, tags=[], since_date="2012-07-10"):
        """ """
        # TODO: since_data parameter should be *yesterday*, using datetime module
        # TODO: check tags to make sure it's a list-like container

        per_page = 10

        def get_data(page):
            data = {"page" : page, \
                    "per_page" : per_page, \
                    "since" : since_date}
            # APW TODO: this is hellish.. maybe we move to using 'request' package?
            params = urllib.urlencode(data)

            params = "{}{}".format(params, encode_tags(tags))

            headers = dict()
            headers["Content-Type"] = "application/json"
            base64string = base64.encodestring("{}:{}".format(self.username, self.api_key))[:-1]
            headers["Authorization"] = "Basic {}".format(base64string)

            request = urllib2.Request("{}?{}".format(self.base_url,params), headers=headers)
            json_data = json.loads(urllib2.urlopen(request).read())
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
    """ """
    return entry.ZooniverseComment(
        comment=entry.Comment(**comment_dict["comment"]), \
        author=entry.Author(**comment_dict["author"]), \
        discussion=entry.Discussion(**comment_dict["discussion"]), \
        light_curve=entry.LightCurve(**comment_dict["light_curve"]), \
        source=entry.Source(**comment_dict["source"]) \
    )


def encode_tags(tags):
    result = urllib.quote("&tags=".join(tags))
    if len(tags) > 0:
        result = '&tags=' + result
    return result
