class Solution:
    def combinationSum2(self, candidates, target):
        # Sorting is really helpful, so we can avoid overcounting easily
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider
        # it as a solution, and stop there
        if target == 0:
            result.append(path)
            return

        for i in range(start, len(nums)):
            # Skip duplicates at the same recursive depth to avoid duplicate combinations
            if i > start and nums[i] == nums[i - 1]:
                continue

            # Pruning: since nums is sorted and positive, no later numbers can fit
            if nums[i] > target:
                break

            # Advance start to i + 1 because each element can only be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])
