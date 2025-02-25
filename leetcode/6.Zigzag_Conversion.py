from pygments.style import ansicolors


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = []
        # ans.append(['*']*numRows)
        # print(ans)
        for i in range(len(s)):
            for j in range(numRows):
                ans.append([j])


        print(ans)

            # PAYPALISHIRING
        # value = [
        #     ['p', 'p'],
        #     ['a'],
        #     ['y']
        # ]


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ("PAYPALISHIRING", 3),
        # ("PAYPALISHIRING", 4),
        # ("A", 1),
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