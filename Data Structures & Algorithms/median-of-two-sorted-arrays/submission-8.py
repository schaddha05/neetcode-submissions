class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A): # ensure A is always smaller of 2 arrays
            A, B = B, A
        
        l = 0 
        r = len(A) - 1

        while True:
            i = (l + r) // 2 # left partition point in A (mid of A)
            j = half - i - 2 # left partition point in B (mid of B)

            # find max of left partition and min of right partition for A and B
            ALeft = A[i] if i >= 0 else -float('inf')
            ARight = A[i+1] if (i+1) < len(A) else float('inf')
            BLeft = B[j] if j >= 0 else -float('inf')
            BRight = B[j+1] if (j+1) < len(B) else float('inf')

            # valid partition
            if ALeft <= BRight and BLeft <= ARight:
                # odd case
                if total % 2 != 0:
                    return min(ARight, BRight)
                else:
                    # even case 
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight: 
                r = i - 1
            else: 
                l = i + 1
            

        



    



        



