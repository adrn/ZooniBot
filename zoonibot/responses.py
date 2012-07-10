import entry
import copy

def response_packer(old_comment, response):
    result = copy.deepcopy(old_comment)
    result.comment = response
    return result

def yourmom_response(zoocomment):
    """Returns a ZooniverseComment object containing a canned response
    to an input ZooniverseComment object.
    """

    separator = ',' + ' '
    tag_list_str = separator.join(zoocomment.comment.tags)
    response_body = (
            "Uh, your mom posted about {0}.".format(tag_list_str))

    # Make a deep copy of the input ZooniverseComment.  Modify only
    # the comment.body and author fields.
    zooresponse = copy.deepcopy(zoocomment)
    zooresponse.comment.body = response_body
    zooresponse.author = ''

    return zooresponse

def help_response(zoocomment):

    result = entry.Comment(body="""Hiya Have you tried our [tutorial video](http://www.planethunters.org/site_guide#video "") and [site guide](http://www.planethunters.org/site_guide "") - they are both good resources for new people #zoonibotans""")
    return response_packer(zoocomment, result)
