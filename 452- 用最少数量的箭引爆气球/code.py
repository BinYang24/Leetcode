class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
		if not points:
			return 0
		points = sorted(points, key = lambda x:x[1])
		
		n = len(points)
		end = points[0][1]
		shoot = 1
		
		for i in range(1, n):
			if points[i][0] > end:
				shoot +=1
				end = points[i][1]
			else:
				pass
		return shoot
		
