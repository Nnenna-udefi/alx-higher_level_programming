#!/usr/bin/python3
"""Defines a text indentation function"""

def text_indentation(text):
    """Prints a text with 2 new lines after each of these : ., ? and :
    with no space at the beginning or at the end of each printed line

    Raise:
    TypeError if text is not a string

    Args:
    text(sting)
    """
    if type(text) not in str:
        raise TypeError("text must be a string")

    words = 0
    while word < len(text) and text[words] == ' ':
        words += 1

    while words < len(text):
        print(text[words], end="")
        if text[words] == '\n' or text[words] in ".?:":
            if text[words] in ".?:":
                print("\n")
            words += 1
            while words < len(text) and text[words] == ' ':
                words += 1
                continue
        words += 1


