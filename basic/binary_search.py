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
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        low_index = 0
        high_index = len(nums) - 1

        while low_index<=high_index:
            # print([low_index, low_value], [mid_index, mid_value], [high_index, high_value])
            mid_index = low_index + (high_index - low_index) // 2
            mid_value = nums[mid_index]
            if mid_value == target:
                return mid_index
            elif mid_value < target:
                low_index = mid_index + 1
            else:
                high_index = mid_index - 1

        return -1


if __name__ == '__main__':
    nums = [5]
    target = 5
    print(Solution().search(nums, target))

