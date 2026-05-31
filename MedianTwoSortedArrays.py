class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #binary search problem
        totalLen = len(nums1) + len(nums2)
        halfLen = totalLen // 2

        if len(nums1) < len(nums2): 
            A,B = nums1, nums2 
        else:
            A,B = nums2, nums1
        
        l = 0
        r = len(A) - 1
        while True:
            # calculate the middle num for smaller array
            midA = (l+r) // 2
            # calculate middle num for larger array. account for offset for midA and midB starting at 0
            midB = halfLen - midA - 2
            
            # last value in A's left partition
            leftA = A[midA] if midA >= 0 else float("-inf")

            # first value in A's right partition
            rightA = A[midA+1] if midA + 1 < len(A) else float("inf")

            # last value in B's left partition
            leftB = B[midB] if midB >= 0 else float("-inf")

            # first value in B's right partition
            rightB = B[midB+1] if midB + 1 < len(B) else float("inf")

            #If the last value we take in the smaller partion is less than the number next to the last value taken in the larger partition and the largest number taken from the larger partition is less than the number next to the largest value in the smaller partition, then we have divided these partitions properly. If not, then we did not partition the left and right partitions properly and we need to adjust the values with binary search.
            if leftA <= rightB and leftB <= rightA:
                if totalLen % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                return min(rightA, rightB)
            # if the last value we take from the smaller partition is greater than the value next to the middle value of the larger position, then we adjust the values taken from the smaller partition by reducing the midpoint by one, effectively reducing the amount of values taken from the smaller partition by 1.
            elif leftA > rightB:
                r = midA - 1
            # otherwise, the opposite is happening, where the last value we take from the larger partition is greater than the value next to the largest value taken from the smaller partition. So, we increase the amount of values taken from the smaller partition by 1
            else:
                l = midA + 1
