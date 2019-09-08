def predict_winner(nums, start, end, memo):
    if start == end:
        return nums[start]
    
    # if memo[start][end] is not None:
    #     return memo[start][end]

    a = nums[start] - predict_winner(nums, start+1, end, memo)
    b = nums[end] - predict_winner(nums, start, end-1, memo)
    return max([a, b])
    # memo = max([a, b])
    # return memo[start][end]


N = int(input())
candies = [int(input()) for _ in range(N)]
sum_candies = sum(candies)

memo = [[None] * len(candies)] * len(candies)

# win_scores = {}
win_scores = []
for i, c in enumerate(candies):
    rest_candies = candies[i+1:]+candies[:i]
    win_scores.append(abs(c-predict_winner(rest_candies, 0, len(rest_candies)-1, None)))
    # win_scores[str(c)] = abs(c-predict_winner(rest_candies, 0, len(rest_candies)-1, None))

print(max(win_scores))
# print(win_scores)