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
            # print(start, end, stones[start:end], stones)
            # print(i-1, k+i, stones[start:end])
            sum_chunk = sum(stones[start:end])
            if sum_chunk < lowest:
                lowest = sum_chunk
                lowest_index = start


        if len(stones)==1:
            print('hello 1', stones, stones[0])
            return stones[0]
        else:
            stones[lowest_index] = lowest
            stones.pop(lowest_index+k-1)
            return self.mergeStones(stones, k)


value = Solution().mergeStones([3, 2, 4, 1], 2)
print(value)
