class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort() 
        for idx, val in enumerate(nums):
            if val > 0:
                break
            if idx > 0 and val == nums[idx - 1]:
                continue
            l,r = idx+1, len(nums)-1
            while l < r:
                threesum = val + nums[l] + nums[r]
                if(threesum > 0):
                    r -= 1
                if(threesum < 0):
                    l += 1
                elif threesum == 0:
                    result.append([val,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return result
