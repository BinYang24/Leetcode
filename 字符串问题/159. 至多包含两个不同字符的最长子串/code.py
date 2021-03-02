class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return len(s)
        
        left = 0
        right = 1
        last_s = 0
        Number = 1
        re = -1
        start_index = left
        while right<=n-1:
            if s[right] in s[start_index: right]:
                if s[right]!=s[last_s]:
                    last_s = right
            else:
                if Number < 2:
                    Number += 1
                    last_s = right
                else:
                    if right-start_index >re:
                        re = right-start_index
                    start_index = last_s
                    last_s = right
                    Number+=1 
            right+=1
        if right - start_index > re:
            re = right-start_index
            
        return re
