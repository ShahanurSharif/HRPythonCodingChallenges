'''
5. Longest Palindromic Substring
Attempted
Medium
Topics
Companies
Hint
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
3.6M
Submissions
10.3M
Acceptance Rate
35.2%
'''
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            print(left, right, s[left], s[right])
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        # racecar
        for from_right in range( len(s), 0, -1 ):
            # print(from_right)
            for start in range( len(s) - from_right + 1 ):
                # print(from_right, start+from_right, len(s), len(s) - from_right + 1)
                if check(start, start + from_right):
                    return s[start:start + from_right]
        return ""

    def longestPalindromeDp(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # print(dp)

        ans = [0, 0]
        for i in range(n):
            dp[i][i] = True

        # babad
        for i in range(n - 1):
            print(s[i], s[i + 1])
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range( 2, n ):
            for i in range(n - diff):
                print(diff, i)
                # j = i + diff

            # pass
        print(dp)


if __name__ == '__main__':
    testcases = [
        # ("abbcccbbbcaaccbababcbcabca", "bbcccbb"),
        # Basic cases
        # ("aacabdkacaa", "aca"),  # Provided test case
        #
        # # Edge cases
        # ("a", "a"),  # Single character string
        # ("aa", "aa"),  # Two identical characters
        # ("ab", "a"),  # Two different characters
        # #
        # # Palindromes of different lengths
        ("racecar", "racecar"),  # Entire string is a palindrome
        # ("babad", "bab"),  # Multiple valid outputs ("aba" also valid)
        # ("cbbd", "bb"),  # Even length palindrome
        # #
        # # # Longest palindrome at edges
        # ("abcracecar", "racecar"),  # Palindrome at the end
        # ("racecarxyz", "racecar"),  # Palindrome at the beginning
        # #
        # # # All identical characters
        # ("aaaaaa", "aaaaaa"),  # Entire string is palindrome
        # #
        # # # No palindromes longer than 1
        # ("abcdefg", "a"),  # All unique characters
        # #
        # # # Mixed cases
        # ("abacdfgdcaba", "aba"),  # Multiple small palindromes
        # ("bananas", "anana"),  # Odd-length palindrome
        # #
        # # # Special characters and digits
        # ("1234321abc", "1234321"),  # Numeric palindrome
        # ("a1b2b1a", "a1b2b1a"),  # Mixed characters palindrome
        # #
        # # # Large input case
        # ("a" * 1000, "a" * 1000),  # Stress test (all identical)

    ]

    solution = Solution()
    for testcase in testcases:
        # pass
        # value = solution.longestPalindrome(testcase[0])
        value = solution.longestPalindromeDp(testcase[0])
        print(value)
        assert value == testcase[1]
