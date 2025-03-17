# main.py
# Purpose: Working with string
# Lab: 3
# Task: 4
# Version: 1.0
# Developer: Hudnitskii A.V. gr.353502
# Date: 17-03-2025

from Task4.decorator import my_decorator
from Task4.scripts import min_length_count
from Task4.scripts import point_before
from Task4.scripts import max_length_with_r

@my_decorator
def main():
    input_string = (
        "So she was considering in her own mind, as well as she could, "
        "for the hot day made her feel very sleepy and stupid, whether "
        "the pleasure of making a daisy-chain would be worth the trouble "
        "of getting up and picking the daisies, when suddenly a White "
        "Rabbit with pink eyes ran close by her."
    )
    min_length_count(input_string)
    point_before(input_string)
    max_length_with_r(input_string)


if __name__ == "__main__":
    main()
