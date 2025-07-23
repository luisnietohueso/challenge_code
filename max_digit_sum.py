# max_digit_sum.py
'''
Find Max Sum

Given an array of strings, each made up of a combination of letters and digits, write the functionality to find and return the largest sum of digits within a string.

Considering a variety of different input arrays, state any assumptions or design choices you had to make.

Notes:

Each digit should be considered its own 1-digit number i.e. in the third string below 36 is evaluated as 3 and 6 separately.
The input arrays can vary in length; however, they will not be larger than 10 strings.
Strings can vary in length; however, they will not be larger than 12 characters.
Example:

Input		[ "dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw" ]
has the sums		11, 4, 10, 13 respectively
so the output is		13
'''

def max_digit_sum(strings):
    if len(strings) > 10:
        raise ValueError("Input cannot contain more than 10 strings.")
    
    max_sum = 0

    for s in strings:
        if len(s) > 12:
            raise ValueError(f"String '{s}' exceeds the 12-character limit.")
    for s in strings:
        current = 0
        for ch in s:
            if '0' <= ch <= '9':
                # check if ch is a digit by its ASCII code
                current += ord(ch) - ord('0')
        if current > max_sum:
            max_sum = current
    return max_sum


if __name__ == '__main__':
    data = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
    print(max_digit_sum(data))
    print(max_digit_sum(["abc", "xyz"]))
    print(max_digit_sum(["a1"] * 11))
