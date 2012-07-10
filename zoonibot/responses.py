""" TODO: Describe this module! """

# Standard Library
import copy

# Project
import entry

def response_packer(old_comment, response):
    result = copy.deepcopy(old_comment)
    result.comment = response
    return result

def yourmom_response(zooniverse_comment):
    """ Returns a ZooniverseComment object containing a canned response
        to an input ZooniverseComment object.
    """

    tag_list_str = ", ".join(zooniverse_comment.comment.tags)
    response_comment = entry.Comment(body="Uh, your mom posted about {0}.".format(tag_list_str))
    
    return response_packer(zooniverse_comment, response_comment)

def help_response(zooniverse_comment):
    """ Returns a ZooniverseComment object with the canned #help response
        from Meg Schwamb (e.g. https://github.com/adrn/ZooniBot/wiki/responses-and-tags)
    """
    
    response_comment = entry.Comment(body="Hiya Have you tried our [tutorial video](http://www.planethunters.org/site_guide#video "") and [site guide](http://www.planethunters.org/site_guide "") - they are both good resources for new people")
    return response_packer(zooniverse_comment, response_comment)
