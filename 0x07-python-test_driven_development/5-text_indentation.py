#!/usr/bin/python3
"""Module to print text with specific indentation."""

def text_indentation(text):
    """Prints text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace each of the characters with the character followed by two newlines
    for char in ".?:":
        text = (char + "\n\n").join(part.strip() for part in text.split(char))

    # Print the modified text without leading/trailing whitespace
    print(text.strip())

