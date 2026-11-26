class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            #base case
            if total == target:
                result.append(list(current))
                return
            
            #prune (also a base case)
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result