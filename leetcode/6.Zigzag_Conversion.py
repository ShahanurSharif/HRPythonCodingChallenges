#  *,  *,  *,  *,  *,
#  6,  7,  8,  *, 10,
# 11, 12,  *, 14, 15,
# 16,  *, 18, 19, 20,
#  *,  *,  *,  *,  *,
from heapq import merge

from numpy.ma.extras import row_stack
from pyautogui import printInfo


#p-0 * a
#a-1 P l
#y-2 * i
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        for i, char in enumerate(s):
            print(i, char, i % numRows)
            ans[i % numRows].append(char)

        print(ans)

        # merge_string = "".join(["".join(row) for row in ans])

        # return merge_string

if __name__ == '__main__':
    s = Solution()
    testcases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5, "AGMSYBFHLNRTXZCEIKOQUWDJPV")
        # ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        # ("A", 1, "A"),
        # ("", 1),
        # ("AB", 1),
        # ("ABCD", 2),
        # ("ABCDE", 4),
        # ("ABCDEFGHIJKLMNO", 5),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 6),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 7),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1000),
    ]
    for testcase in testcases:
        value = s.convert(testcase[0], testcase[1])
        print(value)