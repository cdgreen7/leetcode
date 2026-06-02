class Solution:
    def isPalindrome(self, x: int) -> bool:
        numReversed = 0
        originalNum = x
        if x < 0: return False
        while x != 0:
            numReversed = numReversed * 10 + (x % 10)
            x = x // 10
        if numReversed == originalNum:
            return True
        return False
