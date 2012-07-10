import responses
import entry

c = entry.Comment(body = "Test comment",
                  tags = ['test1', 'test2'])
TEST_ZOOCOMMENT = entry.ZooniverseComment(comment=c)

def test_yourmom():
    result = responses.yourmom_response(TEST_ZOOCOMMENT)
    expect = "Uh, your mom posted about test1, test2."
    assert result.comment.body == expect

def test_help_response():
    result = responses.help_response(TEST_ZOOCOMMENT)
    assert result.comment.body.startswith("Hiya")
