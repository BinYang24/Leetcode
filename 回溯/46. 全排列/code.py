class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if not n:
            return []
        self.visited = []
        results = []
        def back(row, path):
            if row == n:
                results.append(path.copy())
            else:
                for i in range(n):
                    if i not in self.visited:
                        self.visited.append(i)
                        path.append(nums[i])
                        back(row+1, path)
                        path.pop()
                        self.visited.pop()
        back(0, [])
        return results
