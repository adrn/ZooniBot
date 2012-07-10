import entry
import copy

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
    """Returns a ZooniverseComment object with help information based
    on the tags in the input ZooniverseComment object.
    """

    


    pass
