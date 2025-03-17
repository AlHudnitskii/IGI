import random

def sum_of_list(my_list):
    """
    Counts the sum of list.

    Args: my_list (List) : Given the int list
    Returns: sum (int) : The sum of the list.
    """
    return sum(my_list)

def generate_int_list(mode):
    """
    Generate int list.

    Args: mode (string) : Mode to create list
    Returns: my_list (int) : Our int list.
    """
    my_list = []
    if mode == 'auto':
        prev = 0
        while prev != 1:
            prev = random.randint(-5, 5)
            my_list.append(prev)

        my_list.remove(prev)
        return [value for i, value in enumerate(my_list) if i % 2 != 0]

    elif mode == "by_yourself":
        while True:
            try:
                num = input("Введите элемент списка (или '1' для завершения ввода): ")
                if num == '1':
                    break
                my_list.append(int(num))
            except ValueError:
                print("Ошибка: введите корректное вещественное число.")
        return [value for i, value in enumerate(my_list) if i % 2 != 0]
