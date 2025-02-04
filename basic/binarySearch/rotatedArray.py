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
    def findLowest_number_index(self, arr):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        return low



    def search(self, nums: List[int], target: int) -> int:
        lowest_index = self.findLowest_number_index(nums)
        pivot = nums[lowest_index]
        if target == pivot:
            return lowest_index

        if target > nums[lowest_index]:
            low = lowest_index
            high = len(nums) - 1
        else:
            low = 0
            high = lowest_index - 1

        # print(low, high)

        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1
        # if lowest_index == target:
        #     return lowest_index
        #
        # if lowest_index > target:
        #     low = lowest_index
        #     high = len(nums) - 1
        # else:
        #     high = lowest_index - 1
        #     low = 0
        #
        # while low <= high:

        # return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 8, 0, 1, 2]

    target = 1
    print(solution.search(nums, target))