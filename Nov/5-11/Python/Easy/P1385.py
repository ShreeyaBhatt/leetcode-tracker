class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        cnt = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                cnt += 1
        return cnt