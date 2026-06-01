class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # quick checks
        if(len(s)) == 1 or len(s) == 2 or numRows == 1:
            return s
        #result string to store answer
        result = ""
        
        #loop through each row
        for r in range(numRows):
            # formula for incrementing (distance between each jump)
            incr = 2 * (numRows - 1)
            #start at r, go till out of bounds, increment by the incr value.
            for i in range(r, len(s), incr):
                # add each character from index i to the result (works for first/last row)
                result += s[i]
                #since middle rows have extra values, need to check if we are in a middle row and that we are in bounds.
                if(r > 0 and r < numRows - 1 and i + incr - 2*r < len(s)):
                    # if we are in a middle row, we also get the extra character.
                    result += s[i + incr - 2 * r]
        return result
