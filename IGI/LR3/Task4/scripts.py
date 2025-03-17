def min_length_count(input_string):
    """
    Counts the number of words with minimal length in the given text.

    Args: input_string (str) : Given string
    Returns: count (int) : The count of words starting with minimal length.
    """
    words_in_string = input_string.split()
    min_length = min(len(word) for word in words_in_string)
    count = 0
    for word in words_in_string:
        if len(word) == min_length:
            count += 1
    print(f"Количество слов с минимальной длиной ({min_length}): {count}")



def point_before(input_string):
    """
    Find all words after point.

    Args: input_string (str) : Given string
    Returns: count (int) : The list of words starting after point.
    """
    words_in_string = input_string.split()
    words_before_point = []

    for i in range(len(words_in_string) - 1):
        if words_in_string[i + 1].endswith("."):
            words_before_point.append(words_in_string[i + 1])

    print("Слова, за которыми следует точка:", words_before_point)


def max_length_with_r(input_string):
    """
    Find the longest word that ends on "r".

    Args: input_string (str) : Given string
    Returns: count (int) : The longest word that ends on "r"t.
    """
    words_in_string = input_string.split()

    words_ending_with_r = []
    for  word in words_in_string:
        if word.lower().endswith('r'):
            words_ending_with_r.append(word)

    longest_word = max(words_ending_with_r, key=len)
    print("Самое длинное слово, заканчивающееся на 'r':", longest_word)





