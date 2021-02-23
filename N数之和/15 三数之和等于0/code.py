class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        last = None
        if len(nums) <= 2:
            return []
        
        else:
            nums.sort()
            for i in range(len(nums)-2):
                last = None
                if i>0 and nums[i] == nums[i-1]:
                    continue
                else:
                    L = i + 1
                    R = len(nums)-1
                    while R>L:
                        if nums[i] + nums[L] + nums[R] > 0:
                            R-=1 
                                                  
                        elif nums[i] + nums[L] + nums[R] < 0:
                            L+=1
                        else:
                            if last != nums[L]:
                                last = nums[L]
                                l.append([nums[i],nums[L],nums[R]])
                            elif nums[L] == last:
                                pass
                            L+=1
                            R-=1
        return l
