# test_max_digit_sum.py

from max_digit_sum import max_digit_sum

def test_example():
    arr = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
    assert max_digit_sum(arr) == 13

def test_no_digits():
    assert max_digit_sum(["abc", "xyz"]) == 0
def test_exceeds_limit():
    try:
        max_digit_sum(["a1"] * 11) # 11 string
        assert False, "Should raise error for >10 strings"
    except ValueError:
        pass

def test_long_string():
    try:
        max_digit_sum(["a1b2c3d4e5f6g"])  # 13 character
        assert False, "Should raise error for string >12 chars"
    except ValueError:
        pass
        

if __name__ == '__main__':
    import pytest
    raise SystemExit(pytest.main([__file__]))
