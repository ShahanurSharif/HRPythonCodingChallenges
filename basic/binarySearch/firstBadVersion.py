'''
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether
version is bad. Implement a function to find the first bad version.
You should minimize the number of calls to the API.


Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1


Constraints:

1 <= bad <= n <= 231 - 1
'''
from soupsieve.util import lower


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(value):
    if value >= 3:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n

        while low <= high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low


if __name__ == '__main__':
    s = Solution()
    print(s.firstBadVersion(10))
'''
1 => false, 
2 => false, 
3 => true, 
4 => true, 
5 => true, 
6 => true, 
7 => true, 
8 => true, 
9 => true,
10 => true,

'''
