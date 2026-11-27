class Solution:
    def summaryRanges(self, nums):
        res = []
        if len(nums) == 0:
            return res
        
        start = nums[0]
        end = 0
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) == 1:
                continue
            else:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(nums[-1]))            
        return res