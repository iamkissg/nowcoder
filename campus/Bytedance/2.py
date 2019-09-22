#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。

class Solution:

    def give_up(self, questions, rest_time):

        result = [0]
        p1, p2 = 0, 0

        answered = []
        # TODO: 放弃最前面一道 还是当前窗口中最耗时的一道
        while p2 < len(questions):
            tmp = 0
            if questions[p2] > rest_time:
                # 放弃最前面N道
                # while rest_time < questions[p2]:
                #     p1 += 1
                #     tmp += 1
                #     rest_time += questions[p1]

                while rest_time < questions[p2]:
                    rest_time += answered.pop(answered.index(max(answered)))
                    tmp += 1
            answered.append(questions[p2])
            result.append(result[-1]+tmp)
            rest_time -= questions[p2]
            p2 += 1
        return result[1:]
                    


import sys
if __name__ == "__main__":
    # 读取第一行的n
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().strip().split())
        arr = list(map(int, sys.stdin.readline().strip().split()))

        sol = Solution()
        print(' '.join(map(str, sol.give_up(arr,m))))

    