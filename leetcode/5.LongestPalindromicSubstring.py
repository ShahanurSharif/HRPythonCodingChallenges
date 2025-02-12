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
        # print(s[1:3])
        if len(s) <= 1:
            return s
        value = dict()
        for i in range(len(s)):
            if s[i] in value:
                value[s[i]][1] = i+1
                value[s[i]][2] = value[s[i]][1] - value[s[i]][0]
            else:
                value[s[i]] = [i,i+1, i + 1 - i ]

        sorted_data = dict(sorted(value.items(), key=lambda x: (-x[1][-1], x[1][0])))
        first_item = list(sorted_data.keys())[0]
        return s[sorted_data[first_item][0]:sorted_data[first_item][1]]


if __name__ == '__main__':
    testcases = [
        # Basic cases
        ("babad", "bab"),  # "aba" is also a valid answer
        ("cbbd", "bb"),

        # Single character
        ("a", "a"),
        ("z", "z"),

        # Two identical characters
        ("aa", "aa"),
        ("bb", "bb"),

        # Palindromic entire string
        ("racecar", "racecar"),
        ("abba", "abba"),

        # Mixed cases with a long palindrome in the middle
        ("abcdefghgfedcba", "abcdefghgfedcba"),
        ("forgeeksskeegfor", "geeksskeeg"),

        # Edge cases
        ("", ""),  # Empty string
        ("abcd", "a"),  # Any single character is a valid palindrome
        ("abccba", "abccba"),  # Even-length palindrome
        ("abcba", "abcba"),  # Odd-length palindrome

        # Long input
        ("a" * 1000, "a" * 1000),  # All characters are the same, entire string is a palindrome
    ]
    solution = Solution()
    for testcase in testcases:
        value = solution.longestPalindrome(testcase[0])
        print(value)
        assert value == testcase[1]