#  *,  *,  *,  *,  *,
#  6,  7,  8,  *, 10,
# 11, 12,  *, 14, 15,
# 16,  *, 18, 19, 20,
#  *,  *,  *,  *,  *,

#p * a
#a P l
#y * i

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = []
        # rows = [[] for _ in range(numRows)]
        # print(rows)
        for i, char in enumerate(s):
            print(i, char, i % numRows)
            # ans[i % numRows].append(char)
        # for i in range(len(s)):
        #     print(i)




if __name__ == '__main__':
    s = Solution()
    testcases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5, "AGMSYBFHLNRTXZCEIKOQUWDJPV")
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