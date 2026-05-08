class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        triplets = [] 

        for a in range(len(nums)-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue 

            b = a + 1
            c = len(nums) - 1
            target = -nums[a]

            while b < c:
                if nums[b] + nums[c] == target:
                    triplets.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < len(nums) and nums[b] == nums[b-1]:
                        b += 1 
                    
                    while c > -1 and nums[c] == nums[c + 1]:
                        c -= 1
                elif nums[b] + nums[c] > target: 
                    c -= 1
                else:
                    b += 1 
        return triplets