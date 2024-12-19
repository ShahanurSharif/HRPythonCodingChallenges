from typing import List





class Solution:

    def merge_sort(self, left_arr, right_arr):
        pass

    def sort_color_recursive(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_arr = self.sort_color_recursive(nums[:mid])
            right_arr = self.sort_color_recursive(nums[mid:])

            return self.merge_sort(left_arr, right_arr)




    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(nums)
        sorted_nums = self.sort_color_recursive(nums)
        nums[:] = sorted_nums


solution = Solution()

# Define the nums list
nums = [0, 2, 4, 1, 0, 8, 8, 9, 1000, 4, 5]

# Call the sortColors method with nums
solution.sortColors(nums)
print(nums)