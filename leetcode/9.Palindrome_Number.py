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
    def isPalindromeBest(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False

        reverse_half = 0
        while x>reverse_half:
            digit = x%10
            reverse_half = reverse_half * 10 + digit
            x = x//10

        return x == reverse_half or x == reverse_half // 10


    def isPalindrome(self, x: int) -> bool:
        total_len = len(str(x))
        if total_len==0 or total_len==1:
            return True

        index = 0
        while index<total_len/2:
            last_index = total_len - index
            if str(x)[index]!=str(x)[last_index-1]:
                return False
            index+=1

        return True

    def isPalindromeAnother(self, x: int) -> bool:
        x=str(x)
        n=x[::-1]
        if x!=n:
            return False
        return True

if __name__ == '__main__':
    solution = Solution()

    # Example Test Cases
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1, True),
        (12321, True),
        (1221, True),
        (1001, True),
        (1000021, False),
        (-101, False)
    ]

    # Loop with assertions
    for num, expected in test_cases:
        # assert solution.isPalindrome(num) == expected, f"Test failed for input: {num}"
        assert solution.isPalindromeBest(num) == expected, f"Test failed for input: {num}"
        # assert solution.isPalindromeAnother(num) == expected, f"Test failed for input: {num}"

    print("All tests passed successfully! 🚀")