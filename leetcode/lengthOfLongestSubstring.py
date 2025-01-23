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
from django.template.defaultfilters import length


#   a b c a b c b b
#   0 1 2 3 4 5 6 7
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:  # If the string is empty, return 0
            return 0
        if len(s) == 1:  # If the string has one character, return 1
            return 1

        count = 0
        i = 0
        target_value = s[0]
        remaining_value = s
        length_remaining_value = len(remaining_value)

        while i < length_remaining_value:
            # Check if the current target character appears again in the remaining string
            if target_value in remaining_value[i + 1:]:
                location = remaining_value[i + 1:].index(target_value) + (i + 1)

                # Update the count for the length of the current substring
                count = max(count, location - i)

                # Move the target value to the next character
                i += 1
                target_value = remaining_value[i]
            else:
                # No duplicate found; count the rest of the string
                count = max(count, length_remaining_value - i)
                break

        return count


if __name__ == '__main__':
    solution = Solution()
    arr = ['aa']
    for value in arr:
        print(solution.lengthOfLongestSubstring(value))
    # print(solution.lengthOfLongestSubstring("pwwkew"))
    # print(solution.lengthOfLongestSubstring("bbbb"))
    # value = solution.lengthOfLongestSubstring_another("pwwkew")
