from typing import List


class Solution:
    def merge_sort(self, left_arr, right_arr):
        sorted_arr = []
        i = j = 0
        while i < len(left_arr) and j < len(right_arr):
            print(left_arr, right_arr)
            if left_arr[i] < right_arr[j]:
                sorted_arr.append(left_arr[i])
                i+=1
            else:
                sorted_arr.append(right_arr[j])
                j+=1
        # print(f"sorted_arr={sorted_arr}")
        # print(f"merge_left_arr={left_arr}")
        # print(f"merge_right_arr={right_arr}")
        sorted_arr.extend(left_arr[i:])
        sorted_arr.extend(right_arr[j:])
        return sorted_arr

    def sort_color_recursive(self, nums: List[int]):
        length = len(nums)
        if length <= 1:
            return nums

        mid = length // 2

        left_arr = self.sort_color_recursive(nums[:mid])
        right_arr = self.sort_color_recursive(nums[mid:])

        return self.merge_sort(left_arr, right_arr)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = self.sort_color_recursive(nums)
        nums[:] = sorted_nums


solution = Solution()

# Define the nums list
nums = [2,0,2,1,1,0]

# Call the sortColors method with nums
solution.sortColors(nums)
print(nums)
