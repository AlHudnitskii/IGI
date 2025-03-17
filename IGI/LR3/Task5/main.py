# main.py
# Purpose: Working with string
# Lab: 3
# Task: 5
# Version: 1.0
# Developer: Hudnitskii A.V. gr.353502
# Date: 17-03-2025

from scripts import find_min_element
from scripts import sum_between_first_last_positive
from scripts import generate_float_list

def main():
    while True:
        my_list = []
        way_to_our_text = ""
        while way_to_our_text != '1' or way_to_our_text != '2':
            way_to_our_text = input("Use generator or input list by yourself?(1/2)")
            if way_to_our_text == '1':
                length_our_list = ""
                while not (length_our_list.isdigit() and int(length_our_list) > 0):
                    length_our_list = input("Enter a length of our list: ")
                length_our_list = int(length_our_list)
                my_list = generate_float_list(mode='auto', length_our_list = length_our_list)
                break
            elif way_to_our_text == '2':
                my_list = generate_float_list(mode='manual', length_our_list = 0)
                break

        print(f"Список: {my_list}")
        print(f"Минимальный по модулю элемент: {find_min_element(my_list)}")
        print(f"Сумма элементов между первым и последним положительными элементами: {sum_between_first_last_positive(my_list)}")

        continue_program = input("Continue our program?(yes/no)")
        if continue_program != "yes":
            break


if __name__ == "__main__":
    main()
