class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        #negative:
        if x < 0:
            # remove the negative sign by starting at index one, step through the string of numbers backwards. Then, multiply by negative 1
            result = int(str(x)[1:][::-1]) * -1
        else:
        #positive/zero
           # same as negative but start at index zero,
            result = int(str(x)[::-1])
          # bounds check
        if result > (2 ** 31) - 1 or result < (2 ** 31) * -1:
            return 0
        return result
