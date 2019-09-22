#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 100%

import heapq

def give_up(questions, time):

        result = [0]
        p2 = 0

        while p2 < len(questions):
            answered = questions[:p2]
            heapq._heapify_max(answered)
            rest_time = time-sum(answered)
            tmp = 0
            if questions[p2] > rest_time:
                while rest_time < questions[p2]:
                    # cancel = answered.index(max(answered))
                    # rest_time += answered.pop(cancel)
                    rest_time += heapq._heappop_max(answered)
                    tmp += 1
            # answered.append(questions[p2])
            # result.append(result[-1]+tmp)
            result.append(tmp)
            # rest_time -= questions[p2]
            p2 += 1
        return result[1:]



import sys
if __name__ == "__main__":
    # 读取第一行的n
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().strip().split())
        arr = list(map(int, sys.stdin.readline().strip().split()))
        print(' '.join(map(str, give_up(arr,m))))

    