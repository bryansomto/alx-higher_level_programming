#!/usr/bin/python3

def no_c(my_string):
    my_list = list(my_string)
    for letter in my_list:
        if letter == 'c' or letter == 'C':
            index = my_list.index(letter)
            my_list.pop(index)
    return("".join(my_list))
