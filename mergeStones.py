from typing import List

from django.template.defaultfilters import length


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        length = len(stones)
        mid = length // 2
        lowest = 0
        for i in range(len(stones)-1):
            chunk_value = stones[i:i+k]
            sum_chunk = sum(chunk_value)
            sum_chunk_next = sum(stones[i+1:i+1+k])
            if sum_chunk < sum_chunk_next:
                lowest = sum_chunk

            else:
                lowest = sum_chunk_next



mergeStone = Solution()
stones = [3, 2, 4, 1]
k = 2
value = mergeStone.mergeStones(stones, k)
