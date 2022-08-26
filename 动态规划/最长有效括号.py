# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
# leetcode 32
# hard



# 题解：
# 动态规划
# dp[i] 第i个位置的有效括号序列长度 非累计长度
# 比如 ()()( dp[4] = 0
        
# if 当前位置是( dp[i] = 0;
# if 当前位置是):
#          如果i-1是(：那么dp[i] = dp[i-2] + 1 这种情况的意思是 因为i和i-1肯定能组上一组 如果i-2位置有效括号数量大于0 那么要加上i-2的数量 是整体都是有效的括号
#                                                          如果i-2位置上为0那显然前面已经断掉了 不是有效的括号了 和后面连不起来了
#                                                          如果i-2<0 的话 那就dp[i]=1
#          如果i-1是): num = i - 2 * dp[i-1] - 1  
#                     dp[i] = dp[num-1] + dp[i-1] + 1
#                     if dp[num] == (
#                     看个例子： （）（（（））） 在计算dp[6]的时候 我们没有把第一组括号计算进去 因为dp[2]是孤立的 和前面断开了
#                                             但是dp[7]出现了之后全部又连上了 所以要把第一组括号也加进去  如果num-1<0那就不必加了
                        
                        
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n

        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
            else:
                if s[i-1] == '(':
                    if i-2>=0:
                        dp[i] = dp[i-2] + 1
                    else:
                        dp[i] = 1
                elif dp[i-1] == 0:
                    pass
                else:
                    num = i - 2 * dp[i-1] - 1                       
                    if s[num] == '(' and num>=0:
                        if num >=1:
                            dp[i] = dp[i-1] + 1 + dp[num-1]
                        else:
                            dp[i] = dp[i-1] + 1
                    else:
                        dp[i] = 0
        return max(dp)*2
                   
