# max_digit_sum.py

def max_digit_sum(strings):
    max_sum = 0
    for s in strings:
        current = 0
        for ch in s:
            if '0' <= ch <= '9':
                current += ord(ch) - ord('0')
        if current > max_sum:
            max_sum = current
    return max_sum


if __name__ == '__main__':
    data = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
    print(max_digit_sum(data))
    print(max_digit_sum(["abc", "xyz"])) 
