#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 80%

import sys
from string import ascii_uppercase

mapping = {str(i): i for i in range(10)}
mapping.update({c: i for i, c in enumerate(ascii_uppercase, start=10)})
mapping_back = {i: c for c, i in mapping.items()}

def to_decimal(s, base):
    jie = 0
    result = 0
    for c in s[::-1]:
        result += mapping[c] * base ** jie
        jie += 1

    return result


def convert_decimal(n, base):
    if base == 10:
        return str(n)
        
    result = ''
    while n:
        n, mod = divmod(n, base)
        result = mapping_back[mod] + result
    return result


if __name__ == "__main__":
    # 读取第一行的n
    T = int(sys.stdin.readline().strip())
    
    for i in range(T):
        base = int(sys.stdin.readline().strip())
        a, b, opt = sys.stdin.readline().strip().split()

        if base <= 10:
            inta = int(a, base=base)
            intb = int(b, base=base)
        else:
            inta = to_decimal(a, base=base)
            intb = to_decimal(b, base=base)
        
        if opt == '+':
            result = inta+intb
        elif opt == '-':
            result = inta-intb
        elif opt == '*':
            result = inta*intb
        print(convert_decimal(result, base=base))


# 2034324
# 1100
# TJU8
# 2URVXZYVWZ