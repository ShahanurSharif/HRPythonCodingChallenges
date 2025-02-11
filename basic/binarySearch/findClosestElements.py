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
|1-3| = 2
|2-3| = 1
|3-3| = 0
|4-3| = 1
|5-3| = 2
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1
|1-(-1)| = 2
|1-(-1)| = 2
|2-(-1)| = 3
|3-(-1)| = 4
|4-(-1)| = 5
|5-(-1)| = 6
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
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        return []


if __name__ == '__main__':
    testcases = [
        [[1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]],
        # [[1, 1, 2, 3, 4, 5], 4, -1, [1, 1, 2, 3]],
        # [[1, 2, 3, 4, 5, 6, 7, 8], 3, 10, [6, 7, 8]],
        # [[10, 20, 30, 40, 50], 5, 25, [10, 20, 30, 40, 50]],
        # [[5], 1, 5, [5]],
        # [[1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 6, [4, 5, 6, 7]],
        # [[-10, -5, 0, 5, 10], 3, -3, [-5, 0, 5]],
        # [[1, 3, 5, 7, 9], 2, 5, [3, 5]],
        # [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8, 5, [2, 3, 4, 5, 6, 7, 8, 9]],
    ]

    solution = Solution()
    for testcase in testcases:
        result = solution.findClosestElements(testcase[0], testcase[1], testcase[2])
        print(result)
        # assert result == testcase[3]
