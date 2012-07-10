""" TODO: Describe this module! """

class Entry(object):
    _fields = []
    def __init__(self, **kwargs):
        for f in self._fields:
            self.__setattr__(f, None)

        for field in kwargs:
            if field not in self._fields:
                raise TypeError("Invalid keyword: %s %s" % (field, self._fields))
            self.__setattr__(field, kwargs[field])

    def __str__(self):
        result = "%s\n" % self.__class__.__name__
        result += "\n".join(["  %s = %s" % (f, self.__getattribute__(f))
                             for f in self._fields])
        return result

class ZooniverseComment(Entry):
    _fields = ['comment', 'author', 'discussion', 'light_curve', 'source']

class Comment(Entry):
    _fields = ['id', 'body', 'created_at', 'mentions', 'tags']

class Author(Entry):
    _fields = ['id', 'name']

class Discussion(Entry):
    _fields = ['id', 'zooniverse_id', 'subject']

class LightCurve(Entry):
    _fields = ['id', 'zooniverse_id', 'tags']

class Source(Entry):
    _fields = ['id', 'zooniverse_id', 'tags']
