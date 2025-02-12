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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        value = dict()
        for i in range(len(s)):
            if s[i] in value and value[s[i]]>0:
                value[s[i]] = i+1
            else:
                value[s[i]] = 1


if __name__ == '__main__':
    testcases = [
        # Basic cases
        ("babad", "bab"),  # "aba" is also a valid answer
        # ("cbbd", "bb"),

        # Single character
        # ("a", "a"),
        # ("z", "z"),

        # Two identical characters
        # ("aa", "aa"),
        # ("bb", "bb"),

        # Palindromic entire string
        # ("racecar", "racecar"),
        # ("abba", "abba"),

        # Mixed cases with a long palindrome in the middle
        # ("abcdefghgfedcba", "abcdefghgfedcba"),
        # ("forgeeksskeegfor", "geeksskeeg"),

        # Edge cases
        # ("", ""),  # Empty string
        # ("abcd", "a"),  # Any single character is a valid palindrome
        # ("abccba", "abccba"),  # Even-length palindrome
        # ("abcba", "abcba"),  # Odd-length palindrome

        # Long input
        # ("a" * 1000, "a" * 1000),  # All characters are the same, entire string is a palindrome
    ]
    solution = Solution()
    for testcase in testcases:
        value = solution.longestPalindrome(testcase[0])
        print(value)
        # assert value == testcase[1]