from mock import MagicMock

from entry import ZooniverseComment, Discussion
from finders import comments_without_zoonibot_responses

def test_comments_without_zoonibot_responses():
    bot = MagicMock()
    bot.search_comments.return_value = [ZooniverseComment(discussion=Discussion(id=1))]
    coms = [ZooniverseComment(discussion=Discussion(id=i)) for i in [1,2,3]]
    result = comments_without_zoonibot_responses(bot, coms)

    assert coms[0] not in result
    assert coms[1] in result
    assert coms[2] in result

