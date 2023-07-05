#!/usr/bin/python3

"""
python code
"""


def text_indentation(text):
    """
    The `text_indentation` function takes a string
    as input and removes leading whitespace
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text_length = len(text)

    while 1:
        if text[0] == ' ' or text[0] == '\t':
            text = text[:0] + text[1:]
            text_length = text_length - 1
        else:
            break

    text_len = len(text)
    iterate = 0
    while iterate < text_len:
        if text[iterate] == '.' or text[iterate] == '?'\
               or text[iterate] == ':':

            while True:
                if text[iterate - 1] == ' ' or text[iterate - 1] == '\t':
                    text = text[:iterate - 1] + text[iterate:]
                    text_len -= 1
                    iterate -= 1
                else:
                    break

            while True and iterate + 1 < text_len:
                if text[iterate + 1] == ' ' or text[iterate + 1] == '\t':
                    text = text[:iterate + 1] + text[iterate + 2:]
                    text_len -= 1
                else:
                    break
        iterate += 1

    for i in text:
        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print("")
