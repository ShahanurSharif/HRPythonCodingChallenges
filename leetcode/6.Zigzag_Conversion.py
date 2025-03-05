#  *,  *,  *,  *,  *,
#  5,  6,  7,  *,  9,
# 10, 11,  *, 13, 14,
# 15,  *, 17, 18, 19,
#  *,  *,  *,  *,  *,
from heapq import merge

from numpy.ma.extras import row_stack
from pyautogui import printInfo


#p-0 * a
#a-1 P l
#y-2 * i
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""]*numRows

        index, step = 0, 1

        for char in s:
            rows[index] += char

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step
            print(index, step, numRows - 1)

        return ''.join(rows)

if __name__ == '__main__':
    s = Solution()
    testcases = [
        # ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5, "AGMSYBFHLNRTXZCEIKOQUWDJPV")
        # ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        # ("A", 1, "A"),
        # ("", 1),
        # ("AB", 1),
        # ("ABCD", 2),
        # ("ABCDE", 4),
        # ("ABCDEFGHIJKLMNO", 5),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 6),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 7),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1000),
    ]
    for testcase in testcases:
        value = s.convert(testcase[0], testcase[1])
        print(value)