from typing import List

from django.template.defaultfilters import length

class Solution:
    def mergeStones(self, stones: List[int], k: int, total=0) -> int:
        str_order_sum = sum(stones[:k])
        reverse_order = stones[len(stones)-k+1:len(stones)]
        reverse_order.append(stones[0])
        reverse_order_sum = sum(reverse_order)

        lowest_index = 0
        for i in range(1, len(stones) - 1 ):
            start = i
            end = i + k
            if len(stones) - end < 0:
                break

            straigth_sum = sum(stones[start:end])
            print('hello', stones[start::-(i+k)])
            # start_to_end =
            sum_chunk = sum(stones[start:end])
            if sum_chunk < lowest:
                lowest = sum_chunk
                lowest_index = start

        if len(stones)==1:
            # print('hello 1', total, stones, stones[0])
            return total
        else:
            stones[lowest_index] = lowest
            del stones[lowest_index+1:lowest_index+k]
            total += lowest
            return self.mergeStones(stones, k, total)


stones = [6,4,4,6,1]
print(stones[len(stones)-3+1:len(stones)])
# k=2
# value = Solution().mergeStones(stones, k)
# print('final', value)
