from typing import List

from django.template.defaultfilters import length


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        print(stones)
        lowest = sum(stones[:k])
        total = lowest
        lowest_index = 0
        # # [3, 5, 1, 2, 6]
        for i in range(1, len(stones) - 1 ):
            start = i
            end = i + k
            if len(stones) - end < 0:
                break
            # print(start, end, stones[start:end], stones)
        #     # print(i-1, k+i, stones[start:end])
            sum_chunk = sum(stones[start:end])
            if sum_chunk < lowest:
                lowest = sum_chunk
                lowest_index = start
                total = lowest
        #         # print('lowest',lowest)
        #
        #
        if len(stones)==1:
        #     # print('hello 1', stones, stones[0])
            return total + stones[0]
        else:
            stones[lowest_index] = lowest
            stones.pop(lowest_index+1)
            total += stones[lowest_index]
            print(stones[lowest_index])
            return self.mergeStones(stones, k)


total = 0
stones = [3, 5, 1, 2, 6]
value = Solution().mergeStones(stones, 3)
# print('final', value, stones)
