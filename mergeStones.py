from typing import List

from django.template.defaultfilters import length


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        lowest = sum(stones[:k])
        lowest_index = 0
        # list the consecutive smallest sum
        for i in range(k, len(stones)):
            start = i - 1
            end = i - 1 + k
            # print(i-1, k+i, stones[start:end])
            sum_chunk = sum(stones[start:end])
            if sum_chunk < lowest:
                lowest = sum_chunk
                lowest_index = start


        if len(stones)==1:
            return stones[0]
        else:
            stones[lowest_index] = lowest
            stones.pop(lowest_index-1+k)
            self.mergeStones(stones, k)



mergeStone = Solution()
stones = [3, 2, 4, 1]
k = 2
value = mergeStone.mergeStones(stones, k)
print(stones[0])
