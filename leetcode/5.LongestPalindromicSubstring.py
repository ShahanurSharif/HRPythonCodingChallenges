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
    def is_palindrome(self, st: str) -> bool:
        # print(st)
        return st == st[::-1]

    def longestPalindrome(self, s: str) -> str:
        # print(s[1:3])
        if len(s) <= 1:
            return s
        value = dict()
        highest_value = [0, 1, 0]
        for right in range(len(s)):
            if s[right] in value:
                value[s[right]][1] = right + 1
                value[s[right]][2] = value[s[right]][1] - value[s[right]][0]
            else:
                value[s[right]] = [right, right + 1, right + 1 - right]
            # print(value[s[right]][2], highest_value[2])
            if value[s[right]][2] > highest_value[2]:
                if self.is_palindrome(s[value[s[right]][0]:value[s[right]][1]]):
                    print(right, value[s[right]])
                    highest_value = value[s[right]]
        #
        print(highest_value, value)
        return s[highest_value[0]:highest_value[1]]


if __name__ == '__main__':
    testcases = [
        # Basic cases
        ("aacabdkacaa", "aca")

    ]
    solution = Solution()
    for testcase in testcases:
        value = solution.longestPalindrome(testcase[0])
        print(value)
        assert value == testcase[1]
