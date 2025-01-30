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
        low = nums[0]
        high = len(nums) - 1
        mid = len(nums) // 2

        while low <= high:
            print(low, high)
            if nums[mid] == target:
                return nums.index(target)

            if nums[mid] < target:
                low = nums[mid + 1]
            else:
                high = nums[mid - 1]

            mid = mid // 2

            if high == low:
                return -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums, target))

