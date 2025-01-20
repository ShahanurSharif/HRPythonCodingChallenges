from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            print([i, num], complement, num_to_index)
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))