class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def top_down(i, j):
            # if it's in the cache already, return the cached result
            if(i, j) in cache: return cache[(i,j)]
            #if j and i have reached the end of the strings, then we have found that they match
            if j >= len(p) and i >= len(s): return True
            #if j is out of bounds, then s cannot match p, so return galse
            if j >= len(p): return False

            #flag to check for matching pair
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            #check for *
            if (j + 1) < len(p) and p[j+1] == "*":
                # make decision for which branch to follow by recursively calling function, whichever is true gets stored in cache
                cache[(i,j)] = (top_down(i, j + 2) or (match and top_down(i+1, j)))
                return cache[(i,j)]
            #check for match with no *
            if match:
                # store result in cache
                cache[(i,j)] = top_down(i+1, j+1)
                return cache[(i,j)]
            #otherwise, did not match, return False
            cache[(i,j)] = False
            return False

        return top_down(0,0)
