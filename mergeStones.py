from typing import List

from django.template.defaultfilters import length

total = 0

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        global total
        lowest = sum(stones[:k])
        lowest_index = 0
        for i in range(1, len(stones) - 1 ):
            start = i
            end = i + k
            if len(stones) - end < 0:
                break

            sum_chunk = sum(stones[start:end])
            if sum_chunk < lowest:
                lowest = sum_chunk
                lowest_index = start
                # total = lowest
        #         # print('lowest',lowest)
        #
        #
        if len(stones)==1:
            # print('hello 1', total, stones, stones[0])
            return total
        else:
            stones[lowest_index] = lowest
            del stones[lowest_index+1:lowest_index+k]
            total += lowest
            return self.mergeStones(stones, k)


stones = [3, 5, 1, 2, 6]
value = Solution().mergeStones(stones, 3)
print('final', value, stones)
