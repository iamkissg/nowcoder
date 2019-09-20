#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 100%

def find_worst_max(A, B):
    # A.sort()

    # if max(B) <= 0: 
    #     return A[1] * max(B)
    # else:
    #     max_A = max(A)
    #     A.remove(max_A)
    #     return max(B) * max(A)

    result = []
    for a in A:
        result.append(max([a*b for b in B]))
    result.sort()
    return result[-2]



import sys
if __name__ == "__main__":
    # 读取第一行的n
    n, m = map(int, sys.stdin.readline().strip().split())

    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))

    print(find_worst_max(A, B))