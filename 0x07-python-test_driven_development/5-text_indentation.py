#!/usr/bin/python3

"""
Module contains function text_indentation
And it is tested by the doctest 5-text_indentation.txt
"""


def text_indentation(text):
    """
    Formats text and by adding two lines next to every '.', '?' and ':'
    Each line printed has no space at the beginning or at the end.
    If text is not a string, TypeError is raised

    Args:
        text (str): text to be formatted
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text_len = len(text)
    #  If there are any spaces in the beginning of the text, clear them
    while True:
        if text[0] == ' ' or text[0] == '\t':
            text = text[:0] + text[1:]
            text_len -= 1
        else:
            break

    text_len = len(text)
    i = 0
    while i < text_len:
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            #  Clear spaces before the ., ? or :
            while True:
                if text[i - 1] == ' ' or text[i - 1] == '\t':
                    text = text[:i - 1] + text[i:]
                    text_len -= 1
                    i -= 1
                else:
                    break

            #  Clear spaces after the ., ? or :
            while True and i + 1 < text_len:
                if text[i + 1] == ' ' or text[i + 1] == '\t':
                    text = text[:i + 1] + text[i + 2:]
                    text_len -= 1
                else:
                    break
        i += 1

    for i in text:
        print(i, end="")
        if i == '.' or i == '?' or i == ':':
            print('\n')
