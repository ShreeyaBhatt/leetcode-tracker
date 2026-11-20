class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums)-1

        while start <= end:
            # Calculate value for mid
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            
            # Check if left part is sorted
            if nums[mid] >= nums[start]:
                # Checks if the target falls within the sorted left part
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1   # Move left
                else:
                    start = mid + 1 # Move right
            
            # Right part is sorted
            else:
                # Checks if the target falls within the sorted right part
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1 # Move right
                else:
                    end = mid - 1   # Move left
        
        return -1