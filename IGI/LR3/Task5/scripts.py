import random
from email.contentmanager import raw_data_manager


def find_min_element(my_list):
    """
    Find min abs element in float list.

    Args: my_list (List) : Given list
    Returns: element (float) : Minimal abs element.
    """
    return min(my_list, key=abs)


def sum_between_first_last_positive(my_list):
    """
    Counts the sum between first and last positive in the list.

    Args: my_list (List) : Given float list
    Returns: sum (float) : The sum between first and last positive in the list.
    """
    first_positive_index = None
    for i in range(len(my_list)):
        if my_list[i] > 0:
            first_positive_index = i
            break

    last_positive_index = None
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] > 0:
            last_positive_index = i
            break

    if first_positive_index is None or last_positive_index is None:
        return 0
    else:
        return sum(my_list[first_positive_index + 1:last_positive_index])

def generate_float_list(mode, length_our_list):
    """
    Generate float list.

    Args: mode (string), length_our_list (int) : Mode to create list, length of list
    Returns: my_list (float) : Our float list.
    """
    if mode == 'auto':
        return [random.uniform(-100.0, 100.0) for _ in range(length_our_list)]
    else:
        my_list = []
        while True:
            try:
                num = input("Введите элемент списка (или 'q' для завершения ввода): ")
                if num.lower() == 'q':
                    break
                my_list.append(float(num))
            except ValueError:
                print("Ошибка: введите корректное вещественное число.")
        return my_list