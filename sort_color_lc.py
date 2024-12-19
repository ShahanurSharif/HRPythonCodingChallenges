from typing import List





class Solution:

    def merge_sort(self, left_arr, right_arr):
        sorted_arr = []
        i=j=0
        print('value', left_arr, len(left_arr), right_arr, len(right_arr))
        # while i < len(left_arr) and j < len(right_arr):
        #     if left_arr[i] < right_arr[j]:
        #         sorted_arr.append(left_arr[i])

        return [0]

    def sort_color_recursive(self, nums: List[int]):
        length = len(nums)
        if length > 1:
            mid = length // 2
            print('recursion', nums)
            left_arr = self.sort_color_recursive(nums[:mid])
            right_arr = self.sort_color_recursive(nums[mid:])

            return self.merge_sort(left_arr, right_arr)
            # return [0]


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(nums)
        sorted_nums = self.sort_color_recursive(nums)
        nums[:] = sorted_nums


solution = Solution()

# Define the nums list
nums = [0, 2, 4, 1, 0, 8, 8, 9, 1000, 4, 5, 0]

# Call the sortColors method with nums
solution.sortColors(nums)
# print(nums)