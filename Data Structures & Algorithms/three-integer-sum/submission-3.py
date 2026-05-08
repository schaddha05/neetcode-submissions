class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for a in range(len(nums)-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            b = a+1
            c = len(nums) -1
            while b < c:
                curSum = nums[b] + nums[c] + nums[a]
                if curSum == 0:
                    triplets.append([nums[a],nums[b],nums[c]])
                    b+=1
                    c-=1
                    while b < c and nums[b] == nums[b-1]:
                        b+=1
                    while c > b and nums[c] == nums[c+1]:
                        c-=1
                elif curSum > 0:
                    c-=1
                else:
                    b+=1
        
        return triplets
                
                