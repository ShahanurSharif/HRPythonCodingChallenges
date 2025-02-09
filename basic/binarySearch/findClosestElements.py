'''
Find K Closest Elements

Solution
Given a sorted integer array arr, two integers k and x,
return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]



Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''

from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        return arr


if __name__ == '__main__':
    testcases = [
        # Test Case 1: Basic case
        [[1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]],

        # Test Case 2: x is smaller than all elements
        [[1, 1, 2, 3, 4, 5], 4, -1, [1, 1, 2, 3]],

        # Test Case 3: x is larger than all elements
        [[1, 2, 3, 4, 5, 6, 7, 8], 3, 10, [6, 7, 8]],

        # Test Case 4: k is equal to array length
        [[10, 20, 30, 40, 50], 5, 25, [10, 20, 30, 40, 50]],

        # Test Case 5: Only one element in the array
        [[5], 1, 5, [5]],

        # Test Case 6: x is exactly one of the elements
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 6, [4, 5, 6, 7]],

        # Test Case 7: Array contains negative numbers
        [[-10, -5, 0, 5, 10], 3, -3, [-5, 0, 5]],

        # Test Case 8: x is exactly in the middle of the array
        [[1, 3, 5, 7, 9], 2, 5, [3, 5]],

        # Test Case 9: Large k value
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8, 5, [2, 3, 4, 5, 6, 7, 8, 9]],
    ]

    solution = Solution()
    for testcase in testcases:
        result = solution.findClosestElements(testcase[0], testcase[1], testcase[2])
        print(result)
        # assert result == testcase[3]
