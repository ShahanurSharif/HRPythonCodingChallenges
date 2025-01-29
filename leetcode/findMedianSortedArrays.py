'''
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

4. Median of Two Sorted Arrays
Hard
Topics
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = sorted(nums1 + nums2)
        total_len = len(new_arr)

        # If the array has an even length, return the average of the two middle elements
        if total_len % 2 == 0:
            mid1 = new_arr[total_len // 2 - 1]
            mid2 = new_arr[total_len // 2]
            return (mid1 + mid2) / 2
        # If the array has an odd length, return the middle element
        else:
            return new_arr[total_len // 2]


if __name__ == '__main__':
    nums1 = [3]
    nums2 = [-2, -1]

    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
