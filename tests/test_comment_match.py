import re
import unittest

RE_PATTERN = '^".*"$'
class TestCommentMatch(unittest.TestCase):
    def test_match_simple(self):
        comment='"can you believe that?"'
        self.assertTrue(re.search(RE_PATTERN,comment))

    def test_fail_multiline(self):
        comment=\
            """"can you believe that?"
-Me"""
        self.assertEqual(re.search(RE_PATTERN,comment),None)

    def test_fail_manyquotes(self):
        comment=\
            """\"can you believe that?\" \"no, I cannot\""""
        # print(comment)
        self.assertTrue(re.search(RE_PATTERN,comment))
        ql = re.findall("\"",comment)
        # print(ql)
        self.assertFalse(comment.count('"') == 2)


if __name__ == '__main__':
    unittest.main()