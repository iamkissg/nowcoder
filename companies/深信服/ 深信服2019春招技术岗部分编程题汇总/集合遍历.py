# 20190919
# 内存超限:您的程序使用了超过限制的内存
# case通过率为20.00%

def ball_combination(num_balls, N):
    if len(num_balls) == 1:
        return [[N]]
    
    result = []
    for i in range(num_balls[0]+1):
        result.extend([[i]+bc for bc in ball_combination(num_balls[1:], N-i)])
    return result
    

K, N = map(int, input().split())

num_balls = [int(input()) for _ in range(K)]
result = [''.join(map(str, r)) for r in ball_combination(num_balls, N)]
result = sorted(result, key=lambda x: int(x))
for r in result:
    print(r)