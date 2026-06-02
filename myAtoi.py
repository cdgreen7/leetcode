class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        Not the most efficient solution, but I did it in 20ish minutes at 1am last night 
        '''
        intMax, intMin = 2 ** 31 - 1, -2 ** 31
        num = 0
        isNegative = False
        seenSign = False
        parsedNum = False

        s = s.lstrip()

        for char in s:
            if char.isdigit():
                parsedNum = True
                num = 10 * num + int(char)
            if (char == "-" or char == "+") and not seenSign and not parsedNum:
                isNegative = False if char == "+" else True
                seenSign = True
            elif not char.isdigit():
                if isNegative: 
                    num = num * -1 if (num*-1 > intMin) else intMin
                    return num
                num = num if num < intMax else intMax
                return num

        if isNegative: 
            num = num * -1 if (num*-1 > intMin) else intMin
            return num
        num = num if num < intMax else intMax
        return num
