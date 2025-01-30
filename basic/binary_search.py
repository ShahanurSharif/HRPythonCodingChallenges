'''
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_index = 0
        low_value = nums[low_index]
        high_index = len(nums) - 1
        high_value = nums[high_index]
        mid_index = len(nums) // 2
        mid_value = nums[mid_index]

        while low_value<high_value:
            print([low_index, low_value], [mid_index, mid_value], [high_index, high_value])
            mid_index = low_index + (low_index - high_index) // 2
            if mid_value == target:
                return nums.index(target)
            elif mid_value < target:
                low_index = mid_index + 1
                low_value = nums[low_index]
            else:
                high_index = mid_index - 1
                high_value = nums[mid_index - 1]

            if high_index == low_index:
                return -1


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums, target))

