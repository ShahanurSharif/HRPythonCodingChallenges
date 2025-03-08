'''
9. Palindrome Number
Easy
Topics
Companies
Hint
Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        pass

if __name__ == '__main__':
    solution = Solution()

    # Example Test Cases
    print(solution.isPalindrome(121))  # True
    print(solution.isPalindrome(-121))  # False
    print(solution.isPalindrome(10))  # False

    # Additional Edge Cases
    print(solution.isPalindrome(0))  # True (Single digit palindrome)
    print(solution.isPalindrome(1))  # True (Single digit palindrome)
    print(solution.isPalindrome(12321))  # True (Odd-length palindrome)
    print(solution.isPalindrome(1221))  # True (Even-length palindrome)
    print(solution.isPalindrome(1001))  # True (Palindrome with zeros in between)
    print(solution.isPalindrome(1000021))  # False (Similar digits but not a palindrome)
    print(solution.isPalindrome(-101))  # False (Negative numbers are never palindromes)