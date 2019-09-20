#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 20%

def max_happy(games, k):
    sorted_games_1 = sorted(games, key=lambda t: (t[0], t[1]), reverse=True)
    sorted_games_2 = sorted(games, key=lambda t: (t[1], t[0]), reverse=True)

    # print(sorted_games_1, sorted_games_2)
    selected_games_1 = sorted_games_1[:k]
    selected_games_2 = sorted_games_2[:k]

    result = max([
        sum([g[0] for g in selected_games_1]) * min([g[1] for g in selected_games_1]),
        sum([g[0] for g in selected_games_2]) * min([g[1] for g in selected_games_2])
    ])
    # print(1, sum([g[0] for g in selected_games_1]) * min([g[1] for g in selected_games_1]))
    # print(2, sum([g[0] for g in selected_games_2]) * min([g[1] for g in selected_games_2]))
    return result
    



import sys
if __name__ == "__main__":
    # 读取第一行的n
    n, k = map(int, sys.stdin.readline().strip().split())
    
    games = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        games.append((x, y))
    print(max_happy(games, k))