'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#TODO: incomplete

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
from django.template.defaultfilters import length


#   a b c a b c b b
#   0 1 2 3 4 5 6 7
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left
        # right
        char_map = {}
        left = 0
        max_length = 0
        # abcabcbb
        '''
        0->
        s = a
        char_map[{a:0}]
        left = 0
        max_length = 0
        right 0
        1->
        2->
        3->
        4->
        '''
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]]>=left:
                left = char_map[s[right]] + 1
                print(True)

            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
            print(right, s[right], char_map, char_map[s[right]], left, max_length)
            # print(char_map)
        return max_length

if __name__ == '__main__':
    solution = Solution()

    # print(solution.lengthOfLongestSubstring('aa'))
    # print(solution.lengthOfLongestSubstring("abcabcbb"))
    # print(solution.lengthOfLongestSubstring("bbbb"))
    value = solution.lengthOfLongestSubstring("pwwkew")
    print(value)
