'''
7. Reverse Integer
Medium
Topics
Companies
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1

'''


class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            reversed_value = int('-'+str(x)[::-1][:-1])
        else:
            reversed_value = int(str(x)[::-1])

        if ((2**31) - 1)>reversed_value>-2**31:
            return reversed_value
        else:
            return 0

if __name__ == '__main__':
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),   # Overflow case
        (-2147483648, 0),  # Overflow case
        (1463847412, 2147483641),
        (-1463847412, -2147483641),
        (1000000003, 0),   # Overflow case
        (-1000000003, 0)   # Overflow case
    ]
    s = Solution()
    for case in test_cases:
        value = s.reverse(case[0])
        print(value, value==case[1])
