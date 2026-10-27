class Solution:
    def createGrid(self, m, n):
        return ["." * n] + ["#" * (n - 1) + "."] * (m - 1)