import unittest
from bot.anonymous_quote import AnonymousQuote

RE_PATTERN = '^".*"$'
class TestCommentMatch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.comment_normal_anonymous = '"can you believe that?"'
        cls.comment_normal_attributed = '"can you believe that?" -Somebody'
        cls.comment_multiline = \
            """"can you believe that?"
-Me"""
        cls.comment_multiline_anonymous = \
            """\"Is this the real life?
Is this just fantasy?\""""
        cls.comment_multiple_quotes=\
            """\"can you believe that?\" \"no, I cannot\""""
        
    
    def test_match_simple(self):
        comment=self.comment_normal_anonymous
        self.assertTrue(AnonymousQuote.is_comment_quote(comment))
    
    def test_match_multiline(self):
        comment=self.comment_multiline_anonymous
        self.assertTrue(AnonymousQuote.is_comment_quote(comment))
    
    def test_fail_attrib(self):
        comment=self.comment_normal_attributed
        self.assertFalse(AnonymousQuote.is_comment_quote(comment))

    def test_fail_multiline(self):
        comment=self.comment_multiline
        self.assertFalse(AnonymousQuote.is_comment_quote(comment))

    def test_fail_manyquotes(self):
        comment=self.comment_multiple_quotes
        self.assertFalse(AnonymousQuote.is_comment_quote(comment))

if __name__ == "__main__":
    unittest.main()