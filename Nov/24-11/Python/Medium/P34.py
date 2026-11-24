class Solution:
    def searchRange(self, nums, target):
        def first(nums,target):
            l,r=0,len(nums)-1
            first=-1
            while l<=r:
                mid=l+(r-l)//2
                
                if nums[mid]==target:
                    first = mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return first
        def second(nums,target):
            l,r=0,len(nums)-1
            second=-1
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    second=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return second
        return [first(nums,target),second(nums,target)]