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
from contextlib import nullcontext
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


    def binarySearch(self, arr: List[int], target: int, add_value=0) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if target == arr[mid]:
                return add_value + mid
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        lowest_index = self.findLowest_number_index(nums)
        pivot = nums[lowest_index]
        if target == pivot:
            return lowest_index

        left_arr = nums[:lowest_index]
        right_arr = nums[lowest_index:]
        # print(left_arr, right_arr)

        value = self.binarySearch(left_arr, target)
        print(value)
        if value == -1:
            value = self.binarySearch(right_arr, target, len(left_arr))
        else:
            value = -1
        return value



if __name__ == '__main__':
    solution = Solution()
    nums = [3, 1]

    target = 3
    print(solution.search(nums, target))