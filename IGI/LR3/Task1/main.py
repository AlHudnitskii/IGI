# main.py
# Purpose: Working with string
# Lab: 3
# Task: 1
# Version: 1.0
# Developer: Hudnitskii A.V. gr.353502
# Date: 17-03-2025

import math
from scripts import calculate_exp

def main():
    while True:
        x = float(input("Введите значение x: "))
        eps = float(input("Введите точность eps: "))
        n, result = calculate_exp(x, eps)

        print(f"| x {x}")
        print(f"| n {n}")
        print(f"| F(x) {result}")
        print(f"| Math F(x) {math.exp(x)}")
        print(f"| eps {eps}")

        continue_program = input("Continue our program?(yes/no)")
        if continue_program != "yes":
            break


if __name__ == "__main__":
    main()
