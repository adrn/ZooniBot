import pytest

import entry

class TestEntries(object):
    """Entries are simple"""

    def assert_valid_present(self, cls, field):
        """You can pass a valid field to init"""
        cls(**{field:None})

    def assert_invalid_not_present(self, cls, field):
        """Invalid fields raise type error"""
        with pytest.raises(TypeError):
            cls(**{field:None})

    def assert_valid(self, cls):
        for field in cls._fields:
            self.assert_valid_present(cls, field)
        self.assert_invalid_not_present(cls, '___INVALID___')

    def test_comment_container(self):
        self.assert_valid(entry.CommentContainer)

    def test_comment(self):
        self.assert_valid(entry.Comment)

    def test_author(self):
        self.assert_valid(entry.Author)

    def test_discussion(self):
        self.assert_valid(entry.Discussion)

    def test_lightcurve(self):
        self.assert_valid(entry.LightCurve)

    def test_soruce(self):
        self.assert_valid(entry.Source)

