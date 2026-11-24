class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxLength(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                prod *= x
                g = self.gcd(g, x)
                l = (l * x) // self.gcd(l, x)

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans
