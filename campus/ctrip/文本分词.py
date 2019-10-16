#!/usr/bin/env python  
# coding=utf-8

class Solution:

    def word_split(self, sentence, vocab):

        n = len(sentence)
        memo = [False for _ in range(n+1)]  # 多一个表示没有找到单词的情况, 对应最后一个位置
        memo[0] = True
        for i in range(1, n+1):
            for w in vocab:
                # memo 表示 s[0:i-len(w)] 没问题, 可以表示成字典中单词的某种组合
                # w==s[i-len(w):i], 将边界进一步推进到 s[0:i]
                if i >= len(w) and memo[i-len(w)] and w == sentence[i-len(w):i]:
                    memo[i] = True
        return 'YES' if memo[-1] else 'NO'


sol = Solution()
while 1:
    vocab = input().split(',')
    sentence = input()
    # print(vocab, sentence)
    res = sol.word_split(sentence, vocab)
    print(res)