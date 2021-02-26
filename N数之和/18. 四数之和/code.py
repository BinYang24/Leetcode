class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        def search(onesolution, i, target):
            if target == 0 and len(onesolution) == 4:
                output.append(onesolution)
                return
            elif i>len(nums)-1 or len(onesolution) >4:
                return
            if target - (nums[i]+(3-len(onesolution))*nums[-1])>0:
                search(onesolution, i+1, target)
            elif target - (nums[i]*(4-len(onesolution))) < 0:
                return 
            else:
                search(onesolution, i+1, target)
                search(onesolution+[nums[i]], i+1, target-nums[i])
        if len(nums) <=3:
            return []
        else:
            search([], 0, target)
            output1 = []
            output2 = []
            for t in output:
                if set(t) not in output1:
                    output1.append(set(t))
                    output2.append(t)
            return output2
