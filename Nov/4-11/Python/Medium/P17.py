class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phoneDict = ["", "", "abc", "def", "ghi",
                     "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combinations = []
        combination = []

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
                return

            phoneStr = phoneDict[int(digits[index])]
            for ch in phoneStr:
                combination.append(ch)
                backtrack(index + 1)
                combination.pop()

        backtrack(0)
        return combinations