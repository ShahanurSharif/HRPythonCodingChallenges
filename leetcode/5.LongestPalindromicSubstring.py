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
    def is_palindrome(self, st: str) -> bool:
        return st == st[::-1]


    def make_palindrome(self, s, right, val):

        new_str = s[val[s[right]]['indices'][0]: right + 1]
        if self.is_palindrome(new_str):
            val[s[right]]['indices'].append(right)
            val[s[right]]['total'] = val[s[right]]['indices'][-1] - val[s[right]]['indices'][0] + 1
        else:
            remove_indexes = []
            for i in range(len(val[s[right]]['indices'])):
                if s[right] == s[val[s[right]]['indices'][i]]:
                    if self.is_palindrome(s[val[s[right]]['indices'][i]: right + 1]):
                        if val[s[right]]['total'] < len(s[val[s[right]]['indices'][i]: right + 1]):
                            remove_indexes.append(i)
                            val[s[right]]['indices'].append(right)
            # print(remove_indexes[-1])
            if remove_indexes:
                val[s[right]]['indices'] = val[s[right]]['indices'][remove_indexes[-1]:]
                val[s[right]]['total'] = val[s[right]]['indices'][-1] - val[s[right]]['indices'][0]
            print(val, new_str)
        return val

    def longestPalindrome(self, s: str) -> str:
        # print(s[1:3])
        if len(s) <= 1:
            return s
        value = dict()

        highest_value = [0, 1, 0]
        for i in range(len(s)):
            if s[i] in value:
                value = self.make_palindrome(s, i, value)
            else:
                value[s[i]]={'indices': [i], 'total': 1}

            if value[s[i]]['total'] > highest_value[-1]:
                highest_value = [value[s[i]]['indices'][0], value[s[i]]['indices'][-1], value[s[i]]['total']]

        return s[highest_value[0]:highest_value[-2]+1]


if __name__ == '__main__':
    testcases = [
        # Basic cases
        ("aacabdkacaa", "aca"),  # Provided test case

        # Edge cases
        # ("a", "a"),  # Single character string
        # ("aa", "aa"),  # Two identical characters
        # ("ab", "a"),  # Two different characters
        #
        # Palindromes of different lengths
        # ("racecar", "racecar"),  # Entire string is a palindrome
        # ("babad", "bab"),  # Multiple valid outputs ("aba" also valid)
        # ("cbbd", "bb"),  # Even length palindrome
        #
        # # Longest palindrome at edges
        # ("abcracecar", "racecar"),  # Palindrome at the end
        # ("racecarxyz", "racecar"),  # Palindrome at the beginning
        #
        # # All identical characters
        # ("aaaaaa", "aaaaaa"),  # Entire string is palindrome
        #
        # # No palindromes longer than 1
        # ("abcdefg", "a"),  # All unique characters
        #
        # # Mixed cases
        # ("abacdfgdcaba", "aba"),  # Multiple small palindromes
        # ("bananas", "anana"),  # Odd-length palindrome
        #
        # # Special characters and digits
        # ("1234321abc", "1234321"),  # Numeric palindrome
        # ("a1b2b1a", "a1b2b1a"),  # Mixed characters palindrome
        #
        # # Large input case
        # ("a" * 1000, "a" * 1000),  # Stress test (all identical)

    ]

    solution = Solution()
    for testcase in testcases:
        # pass
        value = solution.longestPalindrome(testcase[0])
        print(value)
        try:
            assert value == testcase[1]
        except AssertionError as e:
            print(f'Assertion failed at the {str(e)} line')
            exit(1)
