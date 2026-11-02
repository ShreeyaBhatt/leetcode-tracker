class Solution:
    def minMoves2(self, nums):
        l=len(nums)
        if l==1:
            return 0
        nums.sort()
        mid=nums[l//2]
        res=0
        for i in nums:
            res+=abs(i-mid)
        return res