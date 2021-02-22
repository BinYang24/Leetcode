class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals = sorted(intervals, key=lambda x:x[1])

        end = intervals[0][1]
        n = len(intervals)
        count = 1
        for i in range(1,n):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count+=1
            else:
                pass
        return n-count
				
			
			
