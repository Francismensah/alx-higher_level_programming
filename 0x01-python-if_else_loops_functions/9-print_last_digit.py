#!/usr/bin/python3
# Author - Francis Morkeh Mensah

#!/usr/bin/python3
def print_last_digit(number):
    '''prints the last digit of a number'''
    last_digit = abs(number) % 10
    print(f"{last_digit}", end='')
    return last_digit
