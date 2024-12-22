from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        # Check if merging to one pile is possible
        if (n - 1) % (k - 1) != 0:
            return -1

        # Prefix sum for quick range sum calculation
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]

        # dp[i][j] represents the minimum cost to merge piles from i to j into 1 pile
        dp = [[0] * n for _ in range(n)]

        # Length of the interval
        for length in range(k, n + 1):  # Start from k-length subarrays
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                # Try splitting into k piles
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])

                # Add the merge cost if reducing to 1 pile is possible
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]

        return dp[0][n - 1]


# Example usage
solution = Solution()
stones = [3, 2, 4, 1]
k = 2
print(solution.mergeStones(stones, k))  # Output: 20
