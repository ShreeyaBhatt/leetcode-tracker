class Solution:
    def canAliceWin(self, n):
        take, k = 10, 0
        while n >= take:
            n -= take
            take -= 1
            k += 1
        return k % 2 == 1