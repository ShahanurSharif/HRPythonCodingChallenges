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
        # print(st)
        return st == st[::-1]

    # aacabdkacaa
    # {'a': [0, 1, 1]}
    def make_palindrome(self, s, right, val: List) -> List[int]:
        print(
            s,
            right,
            val[s[right]],
            s[val[s[right]][0]: right+1]
        )
        new_str = s[val[s[right]][0]: right+1]
        new_len = len(new_str)
        if self.is_palindrome(new_str):
            val[s[right]][1] = right+1
            val[s[right]][2] = val[s[right]][1] - val[s[right]][0]
        else:
            for i in range(len(new_str)):
                pass
            # move left

            # aacabdkacaa
        # new_str = s[value[s[right]][0]: right+1]
        # print(new_str)
        # new_str_len = len(new_str)
        # if self.is_palindrome(new_str):
        #     val[s[right]].append(right + 1)
        #     val[s[right]].append(val[s[right]][-2] - val[s[right]][0])
        #     return val
        # else:
        #     for left in new_str:
        #         if not self.is_palindrome(new_str[left:new_str_len-1]):
        #             val[s[right]].pop(left)
        #             val[s[right]].append(right + 1)
        #             val[s[right]].append(val[s[right]][-2] - val[s[right]][0])
        # return val
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
                value[s[i]] = [i, i + 1, i + 1 - i]
            # print(value[s[i]][2], highest_value[2])
            if value[s[i]][2] > highest_value[2]:
                highest_value = value[s[i]]
        #
        # print(highest_value, value)
        return s[highest_value[0]:highest_value[1]]


if __name__ == '__main__':
    testcases = [
        # Basic cases
        ("aacabdkacaa", "aca")

    ]
    arr=[1, 2, 3, 4, 5, 6]
    arr.insert(len(arr) - 1, 's')
    print(arr)
    # print(testcase[0])
    solution = Solution()
    for testcase in testcases:
        pass
        # value = solution.longestPalindrome(testcase[0])
        # print(value)
        # assert value == testcase[1]
