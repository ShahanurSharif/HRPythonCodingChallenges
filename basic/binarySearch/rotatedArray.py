'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_index = 0
        last_index = len(nums) - 1
        while first_index <= last_index:
            middle_index = (first_index + last_index) // 2
            # print(middle_index)
            if nums[middle_index] == target:
                return middle_index
            elif nums[first_index] == target:
                return first_index
            elif nums[last_index] == target:
                return last_index
            elif target < nums[first_index]:
                first_index = middle_index + 1
            else:
                last_index = middle_index - 1

        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3]

    target = 3
    print(solution.search(nums, target))