import random

def count_lowercase_consonant_words(our_text):
    """
    Counts the number of words that start with a lowercase consonant in the given text.

    Args: our_text (str) : Given string to find the number of specific words
    Returns: count (int) : The count of words starting with a lowercase consonant.
    """
    vowels = {"a", "e", "i", "o", "u", "y"}
    separators = {" ", ",", ".", ":", ";", "(", ")", "[", "]", "<", ">", "/", "|"}
    count = 0
    for i in range(len(our_text) - 1):
        if i == 0:
            if 97 <= ord(our_text[i]) <= 122 and our_text[i] not in vowels:
                count += 1
        if our_text[i] in separators and 97 <= ord(our_text[i + 1]) <= 122 and our_text[i + 1] not in vowels:
            count += 1

    return count


def our_text_generator(length_our_text):
    """
    Generates a random string of a given length using English letters (both cases) and separators.

    Args: length (int): The length of the string.
    Returns: our_text (string): A randomly generated string.
    """
    our_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ                ,.!?;:'
    our_text = ''.join(random.choice(our_chars) for char in range(length_our_text))

    return our_text