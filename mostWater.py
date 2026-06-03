class Solution:
    def maxArea(self, height: List[int]) -> int:
      #initialize left and right pointer
        left, right = 0, len(height) - 1
      # initialize maxWater variable
        maxWater = 0
      # loop until the pointers meet in the middle
        while left < right:
           #use the smaller of the two heights and multiply by the width between the two to find the area
            water = min(height[left], height[right]) * (right - left)
           #check if maxWater is greater than the calculated water
            maxWater = max(maxWater, water)
          #update the pointers depending on which one is taller.
            if height[left] > height[right]:
                right-= 1
            else:
                left += 1
        return maxWater
            
