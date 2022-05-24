#!/usr/bin/python3
"""file name: 5-text_indentation.py
Text intdent: prints text with 2 new lines
Prototype: def text_indentation(text):
"""


from cmath import phase


def text_indentation(text):
    """
    size: the number of # to print
    
    Raises:
            TypeError: size must be an integr
            TypeError: size must be >= 0
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    phrase = ""
    i = 0
    while i < len(text):
        if text[i] != "." and text[i] !=  "?" and text[i] != ":":
            phrase += text[i]
        else:
            phrase += text[i]
            print(phrase)
            print()
            phrase = ""
            while i < (len(text) - 1) and text[i+1] == " ":
                i += 1
        i += 1
    print(phrase, end="")
