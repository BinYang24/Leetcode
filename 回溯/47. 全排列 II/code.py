class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n<=0:
            return nums
        self.visited = []
        results = []
        def find(path, visitednum):
            if len(path) == n:
                results.append(path.copy())
            for i in range(n):
                if i not in self.visited:
                    self.visited.append(i)
                    if nums[i] not in visitednum:
                        visitednum.append(nums[i])
                        path.append(nums[i])
                        find(path, [])
                        path.pop()
                    self.visited.pop()
        find([], [])
        return results
