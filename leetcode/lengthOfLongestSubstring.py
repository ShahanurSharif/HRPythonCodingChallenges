'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''
#   a b c a b c b b
#   0 1 2 3 4 5 6 7
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        find_value = s[:1]
        remaining_value = s[1:]
        for i in range(len(remaining_value)):
            if find_value in remaining_value:
                next_index = remaining_value.index(find_value)
                remaining_value = remaining_value[next_index:]
                find_value = remaining_value[i]
                i += next_index
                print(remaining_value, find_value, next_index, i)
                if next_index > count:
                    count = next_index + 1


        # for i in range(len(str_value)):
        #     str_value = s[i:]
        #     print(str_value, s[i])
        #     if s[i] in str_value:
        #         duplicate_index = str_value.index(str_value)
        #     else:
        #         duplicate_index = 0
        #     #
        #     if duplicate_index + 1 > count:
        #         count = duplicate_index + 1
        #         i = duplicate_index
        #
        # return count







if __name__ == '__main__':
    solution = Solution()
    value = solution.lengthOfLongestSubstring("abcabcbb")