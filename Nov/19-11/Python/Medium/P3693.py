class Solution:
    def climbStairs(self, n, costs):
        a = b = c = 0
        for i in range(n):
            a, b, c = b, c, min(a + 9, b + 4, c + 1) + costs[i]
        return c