""" """

# Standard Library
import os,sys
import urllib, urllib2
import json
    
class Bot(object):
    pass
    
class CommentBot(Bot):
    pass
    
class ZooniBot(CommentBot):
    """ The ZooniBot is an automated robot for commenting on Zooniverse 
        objects. The ZooniBot is specified by an API key, which is unique
        to the zoonibot user on zooniverse.org. This API key is given to 
        the bot by instantiating an API() object, and passing it to bot
        instantiator.
    """
    
    def __init__(self, api):
        self.api = api
    
    def post(comment):
        """ Post the comment to the Zooniverse by zoonibot """
        raise NotImplementedError()
    
    def search_comments(tags):
        raise NotImplementedError()