import re

class AnonymousQuote:
    '''Starts and ends with a double quote. Only Two quotes in comment.'''
    # PATTERN = '^"[.\s]*"$'
    ALLOWED_QUOTES = 2

    @staticmethod
    def is_comment_quote(comment:str):
        quotes_in_comment = comment.count('"')
        char_len = len(comment)
        # matches_pattern = re.search(AnonymousQuote.PATTERN,comment)
        if (comment[0:1] == '"' and comment[(char_len-1):] == '"') and \
            quotes_in_comment == AnonymousQuote.ALLOWED_QUOTES:
            return True
        return False
