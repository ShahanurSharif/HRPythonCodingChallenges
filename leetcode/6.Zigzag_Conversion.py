class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = []
        #  1,  2,  3,  4,  5,
        #  6,  7,  8,  *, 10,
        # 11, 12,  *, 14, 15,
        # 16,  *, 18, 19, 20,
        #  *,  *,  *,  *,  *,
        i=0
        while i != len(s) + 1:
            for j in range(numRows):
                i+=1



if __name__ == '__main__':
    s = Solution()
    testcases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
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