def correct_word_spelling(word):
    '''错误, 间下面的解法吧'''
    if not word:
        return ''

    char_stack = word[0]
    i = 1
    while i < len(word):
        if i >= 2 and char_stack[-1] == char_stack[-2]:
            if word[i] == char_stack[-1]:
                i += 1
            else:
                char_stack += word[i]
                i += 2 if i < len(word)-1 and word[i] == word[i+1] else 1
        else:
            char_stack += word[i]
            i += 1
    return char_stack


def correct_word_spelling2(s):
    res = []
    for e in s:
        if len(res) < 2:
            res.append(e)
            continue
        if len(res) >= 2:
            if e == res[-1] and e == res[-2]:
                continue
        if len(res) >= 3:
            if e == res[-1] and res[-2] == res[-3]:
                continue
        res.append(e)
    return "".join(res)

N = int(input())

for _ in range(N):
    word = input()
    print(correct_word_spelling(word))
    print(correct_word_spelling2(word))