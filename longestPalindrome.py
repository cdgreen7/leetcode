class Solution:
    def longestPalindrome(self, s: str) -> str:
        # vars to store result and result length
        result = ""
        resultLen = 0
        # loop through each letter in s
        for i in range(len(s)):
            # odd, start with left and right at the "middle" of the palindrome, work outwards
            left, right = i, i
            # check that the values are in bound and are still a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # check if the number of letters in the palindrome is greater than our greatest palindrome
                if (right - left + 1) > resultLen:
                    # change result to include all letters we have checked for this palindrome. Upadte the length of the palindrome
                    result = s[left:right+1]
                    resultLen = right - left
                #increment left and right pointers
                left = left - 1
                right = right + 1
            # even, start with left at left-middle and right at right-middle (left + 1). Work outwards from each. 
            left,right = i, i+1
            # check that the substring is within range and is still a valid palindrome.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # repeat from "odd" section
                if (right - left + 1) > resultLen:
                    result = s[left:right+1]
                    resultLen = right - left
                #increment left and right pointer
                left = left - 1
                right = right + 1

        return result
