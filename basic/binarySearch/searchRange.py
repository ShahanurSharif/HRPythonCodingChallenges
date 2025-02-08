'''
Search for a Range

Solution
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
# [5, 7, 7, 8, 8, 10]

from typing import List


class Solution:
    def findBound(self, isFirst: bool) -> int:
        bound = -1
        return bound

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findBound(True)
        last = self.findBound(False)

        return [first, last]


if __name__ == '__main__':
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),  # Target 8 appears at indices 3 and 4
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),  # Target 6 is not in the array
        ([], 0, [-1, -1]),  # Empty array, target not found
        ([1], 1, [0, 0]),  # Single element, target found at index 0
        ([1, 1, 1, 1, 1], 1, [0, 4]),  # All elements are the target
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [4, 4]),  # Target at a single index
        ([2, 4, 4, 4, 6, 6, 7, 8, 8, 10], 4, [1, 3]),  # Multiple occurrences of the target
        ([1, 3, 3, 5, 5, 5, 7, 9], 5, [3, 5]),  # Target appears in the middle
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, [-1, -1]),  # Target not in the array
        ([5, 5, 5, 5, 5, 5, 5], 5, [0, 6]),  # All elements are the same as the target
    ]

    for nums, target, expected in test_cases:
        sol = Solution()
        actual = sol.searchRange(nums, target)
        print(actual, expected)
        # assert actual == expected