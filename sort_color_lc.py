from typing import List
class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(nums)
        length = len(nums)
        count = [0] * (max(nums) - min(nums) + 1)
        print(count)


solution = Solution()

# Define the nums list
nums = [0, 2, 4, 1, 0, 8, 8, 9, 1000, 4, 5]

# Call the sortColors method with nums
solution.sortColors(nums)
print(nums)