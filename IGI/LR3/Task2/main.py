# main.py
# Purpose: Working with string
# Lab: 3
# Task: 2
# Version: 1.0
# Developer: Hudnitskii A.V. gr.353502
# Date: 17-03-2025

from scripts import sum_of_list
from scripts import generate_int_list

def main():
    while True:
        way_to_our_text = ""
        my_list = []
        while way_to_our_text != '1' or way_to_our_text != '2':
            way_to_our_text = input("Use generator or input list by yourself?(1/2)")
            if way_to_our_text == '1':
                my_list = generate_int_list(mode = 'auto')
                break
            elif way_to_our_text == '2':
                my_list = generate_int_list(mode = 'by_yourself')
                break

        print(f"Сумма каждого второго элемента: {sum_of_list(my_list)}")
        continue_program = input("Continue our program?(yes/no)")
        if continue_program != "yes":
            break


if __name__ == "__main__":
    main()
