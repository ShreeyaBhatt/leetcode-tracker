class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def findGCD(self, nums):
        minimum = min(nums)
        maximum = max(nums)

        return self.gcd(minimum, maximum)