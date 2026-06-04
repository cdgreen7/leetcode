class Solution:
    def romanToInt(self, s: str) -> int:
        listOfSym = {
            "M": 1000 ,
            "D": 500 ,
            "C": 100 ,
            "L": 50 ,
            "X": 10 ,
            "V": 5 ,
            "I": 1
        }
        num = 0
        for i in range(len(s)-1):
            #checks for subtractive notation
            if listOfSym[s[i]] < listOfSym[s[i+1]]:
                num-= listOfSym[s[i]]
            else:
                num += listOfSym[s[i]]
        #add last symbol
        num += listOfSym[s[-1]]
        return num
