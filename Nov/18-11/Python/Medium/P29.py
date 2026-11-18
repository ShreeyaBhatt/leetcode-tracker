class Solution:
    def divide(self, a, b):
        # Handle 32-bit overflow edge case directly
        if a == -2147483648 and b == -1:
            return 2147483647

        sig = (a < 0) == (b < 0)
        a, b, res = abs(a), abs(b), 0

        while a >= b:
            x = 0
            while a >= (b << (x + 1)):
                x += 1
            res += 1 << x
            a -= b << x

        ans = res if sig else -res
        return max(-2147483648, min(ans, 2147483647))
