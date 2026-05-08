class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = []
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue 
            for b in range(a+1, len(nums) -2):
                if b - 1 != a and nums[b] == nums[b-1]:
                    continue 

                goal = target - (nums[a] + nums[b])
                c = b + 1
                d = len(nums) -1 
                while c < d:
                    if nums[c] + nums[d] == goal:
                        quads.append([ nums[a], nums[b], nums[c], nums[d] ])
                        c += 1
                        d -= 1

                        while c < len(nums) and nums[c] == nums[c-1]:
                            c += 1
                        
                        while d > -1 and nums[d] == nums[d+1]:
                            d -= 1
                        
                    elif  nums[c] + nums[d] > goal:
                        d -= 1
                    else:
                        c += 1 
        
        return quads