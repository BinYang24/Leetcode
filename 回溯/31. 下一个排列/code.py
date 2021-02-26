class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return nums
        tag = False
        i = len(nums) - 1
        while i>=1 and nums[i-1] >= nums[i]:
            i-=1
        # print(nums[::-1])
        if i == 0:
            # return nums[::-1]
            nums = nums.reverse()
            # print(nums)
        else:
            # i is (4 8 7 5 3) 8
            for m in range(i+1, len(nums)):
                if nums[m] <= nums[i-1]:
                    tag = True
                    break
            if tag:
                change = m-1
            else:
                change = len(nums)-1
            temp = nums[change]
            nums[change] = nums[i-1]
            nums[i-1] = temp

            L = i
            R = len(nums) - 1
            while L<R:
                temp = nums[L]
                nums[L] = nums[R]
                nums[R] = temp
                L+=1
                R-=1
