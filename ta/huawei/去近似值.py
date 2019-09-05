import sys

for line in sys.stdin:
    num = float(line.strip())

    i = int(num)  # 整数部分
    f = num - i   # 小数部分

    print(i + 1 if f * 10 >= 5 else i)