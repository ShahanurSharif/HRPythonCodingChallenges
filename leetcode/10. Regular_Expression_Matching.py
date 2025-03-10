'''
10. Regular Expression Matching
Hard
Topics
Companies
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass

if __name__ == '__main__':
    solution = Solution()
    assert solution.isMatch("aa", "a") == False  # Single character 'a' doesn't match "aa"
    assert solution.isMatch("aa", "a*") == True  # '*' matches zero or more 'a'
    assert solution.isMatch("ab", ".*") == True  # '.*' matches any characters
    assert solution.isMatch("aab", "c*a*b") == True  # 'c*' disappears, 'a*' matches "aa"
    assert solution.isMatch("mississippi", "mis*is*p*.") == False  # Pattern doesn't match full string
    assert solution.isMatch("abc", "a.c") == True  # '.' matches any single character
    assert solution.isMatch("aaa", "a*a") == True  # '*' can extend 'a' to match "aaa"
    assert solution.isMatch("aaa", "ab*a*c*a") == True  # Complex pattern matching "aaa"
    assert solution.isMatch("abcd", "d*") == False  # 'd*' matches zero or more 'd', but doesn't fit "abcd"
    assert solution.isMatch("", ".*") == True  # '.*' can match an empty string
    assert solution.isMatch("a", "ab*") == True  # 'b*' can be zero, so "a" matches "ab*"
    assert solution.isMatch("bbbba", ".*a*a") == True  # Complex pattern successfully matches