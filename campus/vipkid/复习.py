class Solution:
    def func(self, costs_values, total_time):
        '''
        示例是错的
        '''
        costs, values = zip(*costs_values)
        
        if min(costs) > total_time:
            return 0
        
        n_cost = len(costs)
        dp = [[0 for i in range(total_time+1)] for i in range(n_cost+1)]
        for i in range(1, n_cost+1):
            for t in range(1, total_time+1):
                if costs[i-1] > t:
                    dp[i][t] = dp[i-1][t]
                else:
                    dp[i][t] = max(dp[i-1][t], values[i-1]+dp[i-1][t-costs[i-1]-1])
        return max(item for row in dp for item in row)
                    

while True:
    sol = Solution()

    T = int(input())
    nm = [list(map(int, input().split())) for _ in range(T)]
    # n 表示每个人的知识点数量, 已经用于读取 CV
    # m 表示每个人可用的准备时间
    n, m = zip(*nm)
    # C 表示复习所需时间
    # V 表示复习收益
    CV = [[list(map(int, input().split())) for _ in range(nn)] for nn in n]
    # print(T)
    # print(nm, n, m)
    # print(len(CV))
    # print(len(m))
    
    result = [sol.func(cv, total_time) for cv, total_time in zip(CV, m)]
    for item in result:
        print(item)

'''
3
1 2
3 2
2 2

2 2

2 3
3 6
4 6

3 3
3 4



3
1 2
3 2
2 2
2 2
2 3
3 6
4 6
3 3
3 4
'''