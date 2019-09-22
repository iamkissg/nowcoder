#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

class Solution:

    def distance(self, lines):
        n_O = lines.count('O')
        length = len(lines)
        
        where_O = [lines.index('O')]
        for i in range(n_O-1):
            where_O.append(lines.index('O', where_O[-1]+1, length))
        
        
        lines = lines[:lines.find('O')][::-1]+lines+lines[lines.rfind('O')+1:]

        aaa = lines.split('O')
        result = [0] * length
        for i, c in enumerate(lines):
            if c == 'O':
                continue
            else:
                if len(where_O) > 1 and abs(i-where_O[0])>=abs(i-where_O[1]):
                    where_O.pop(0)
                # result.append(abs(i-where_O[0]))
                result[i] = i-where_O[0]
        return map(abs, result)


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    lines = sys.stdin.readline().strip()
    sol = Solution()
    print(' '.join(map(str, sol.distance(lines))))