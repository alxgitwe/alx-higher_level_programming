#!/usr/bin/python3
"""
text
"""


def text_indentation(text):
    """print"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in ['.', '?', ':']:
        if i in text:
            text = text.replace(i, i + '\n\n\a')

    j = text.split('\a')
    for y in j:
        print(y.strip(' '), end="")
