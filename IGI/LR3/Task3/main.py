# main.py
# Purpose: Count lowercase consonant words
# Lab: 3
# Task: 3
# Version: 1.0
# Developer: Hudnitskii A.V. gr.353502
# Date: 13-03-2025

from scripts import count_lowercase_consonant_words
from scripts import our_text_generator

def main():
    while True:
        way_to_our_text, our_text = "", ""
        while way_to_our_text != '1' or way_to_our_text != '2':
            way_to_our_text = input("Use generator or input string by yourself?(1/2)")
            if way_to_our_text == '1':
                length_our_text = ""
                while not (length_our_text.isdigit() and int(length_our_text) > 0):
                    length_our_text = input("Enter a length of our string: ")
                length_our_text = int(length_our_text)
                our_text = our_text_generator(length_our_text)
                print(f"Our string: {our_text}")
                break
            elif way_to_our_text == '2':
                our_text = input("Enter a string: ")
                break

        count = count_lowercase_consonant_words(our_text)
        print(f"Number of lowercase consonant words: {count}")

        continue_program = input("Continue our program?(yes/no)")
        if continue_program != "yes":
            break

if __name__ == "__main__":
    main()

