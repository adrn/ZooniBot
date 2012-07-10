""" """
# Standard Library
import os,sys
import base64
import urllib, urllib2
import json
from time import sleep

class Bot(object):

    def post(self, comment):
        raise NotImplemented

    def find_and_respond(self, finder, responder):
        """ Use finder and responder utilities to respond to comments
        Parameters
        ----------
        finder : function to return Comments object
        responder : function to create ZooniverseComments from a input comment
        """
        for comment in finder():
            sleep(1)
            r = responder(comment)
            self.post(r)


class CommentBot(Bot):

    def __init__(self, username, api_key, base_url):
        """ Parameters
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
        """ Post the comment to the Zooniverse by zoonibot """

        discussion_id = zooniverse_comment.discussion.id
        comment = zooniverse_comment.comment
        data = {"discussion_id" : discussion_id, "comment" : {"body" : comment.body}}

        # Form the HTTP header to pass with the POST request
        headers = dict()
        headers["Content-Type"] = "application/json"
        base64string = base64.encodestring("{}:{}".format(self.username, self.api_key))[:-1]
        headers["Authorization"] = "Basic {}".format(base64string)

        request = urllib2.Request(self.base_url, headers=headers, data=json.dumps(data))
        response = urllib2.urlopen(request)
        response_code = response.getcode()
<<<<<<< HEAD

        if response_code != 200:
=======
        
        if response_code != 201:
>>>>>>> 21b22cd1865222af020d08e2d7a764c131d4b79c
            raise ValueError("Post failed with response code: {}".format(response_code))

    def search_comments(self, tags):
        """ """

        data = [("page", 1), ("per_page", 10), ("since", "2012-05-02")]

        headers = dict()
        headers["Content-Type"] = "application/json"
        base64string = base64.encodestring("{}:{}".format(self.username, self.api_key))[:-1]
        headers["Authorization"] = "Basic {}".format(base64string)

        request = urllib2.Request(self.base_url, headers=headers)
        json_data = json.loads(urllib2.urlopen(request).read())

        print json_data

        # returns a generator for comment objects