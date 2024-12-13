import re

""" Tokenize Arabic text into words. """
def tokenize_text(text):
    return re.findall(r'\w+', text)
