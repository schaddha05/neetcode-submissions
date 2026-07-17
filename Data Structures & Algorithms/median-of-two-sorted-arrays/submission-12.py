class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A 
        
        l = 0 
        r = len(A) - 1

        while True:
            i = (r + l) // 2 # midpoint of A (end of left partition)
            j = half - i - 2 # mid of B (end of left partition for B)

            Aleft = A[i] if i >= 0 else -float('inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else -float('inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            # correct partitioning
            if Aleft <= Bright and Bleft <= Aright:
                # odd case 
                if total % 2 != 0:
                    return min(Aright, Bright)
                else:
                    # even case
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        

        