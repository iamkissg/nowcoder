# 子串问题, 可用滑动窗口方法解决. 此处, 从后往前, 找到空格即可.


line = input()

if not ' ' in line:
    print(len(line))
else:
    i = len(line) - 1
    while line[i] != ' ':
        i -= 1
    print(len(line) - i - 1)