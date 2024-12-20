from typing import List

class Solution:
    def merge_sort(self, left_arr, right_arr):
        pass

    def sort_color_recursive(self, nums: List[int]):
        length = len(nums)
        if length <= 1:
            return nums
        
        mid = length // 2

        left_arr = self.sort_color_recursive(nums[:mid])
        right_arr = self.sort_color_recursive(nums[mid:])

        sorted_arr = []
        i=j=0
        while i<len(left_arr) and j<(right_arr):
            if left_arr[i] < right_arr[j]:
                sorted_arr.append(left_arr[i])
                i+=1
            else:
                sorted_arr.append(right_arr[j])
                j+=1

        print(left_arr[i:], right_arr[j:])


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = self.sort_color_recursive(nums)
        nums[:] = sorted_nums

solution = Solution()

# Define the nums list
nums = [0, 2, 4, 1, 0, 8, 8, 9, 1000, 4, 5, 0]

# Call the sortColors method with nums
solution.sortColors(nums)
print(nums)