class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        thinking logically, you could look through each combination of numbers until you find the answer, 
        though the time that would take would be abysmal (O(n^2)). A better solution would be to use a dict
        to hold the index of that specific number
        '''

        #first, create a dict to save index
        seenNum = {}

        #now, loop through the array
        for idx, num in enumerate(nums):
            #calculate the complement
            complement = target - num
            #if the complement is in the set, then return the idx of complement and num.
            if complement in seenNum:
                return [seenNum[complement], idx]
            #otherwise, create an entry in the dict with num as the index, set the index of the num within the original list as the value.
            seenNum[num] = idx
        #after looping through, if no pair exists, return false.
        return False
    
