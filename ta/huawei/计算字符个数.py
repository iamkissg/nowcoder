# 同"字符串中最后一个单词的长度", 为子串问题, 可用滑动窗口方法.
# 本题更简单, 只要从从左往右滑去即可.


string = input()
char = input()

if string == '':
    print(0)
else:
    string = string.lower()
    char = char.lower()
    counter = 0
    for i, s in enumerate(string):
        if string[i] == char:
            counter += 1
    print(counter)