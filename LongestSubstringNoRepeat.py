class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to hold seen letters
        seen = {}
        # leftmost value of the sliding window
        left = 0
        #greatest length of string
        greatestLen = 0

        # loop through each letter in the string, and its index
        for right, letter in enumerate(s):
            #check to see if the letter is a duplicate, then check to see if it's in the "window" of the substring
            if letter in seen and seen[letter] >= left:
                #if so, move the leftmost value of the window to be right after the duplicate was first seen.
                left = seen[letter] + 1

            # add the index of the letter to the set
            seen[letter] = right
            #calculate the greatest length using max() with current greatest length and calculated length of current substring
            greatestLen = max(greatestLen, right - left + 1)

        return greatestLen
