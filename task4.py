#! python3
"""
Create a function called is Integer()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

print(is_integer_num(100))
# True

print(is_integer_num(1.23))
# False

print(is_integer_num(100.0))
# True

print(is_integer_num('100'))
# False