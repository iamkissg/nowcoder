import sys
from array import array

# 60

class Solution:
    def __init__(self, k):
        self.k = k
        # self.mask = [1] * k
        # self.len_mask = len(self.mask)

        # self.memo = {}

    # def find_max_score(self, scores, is_awake):
    #     may_get = []
    #     for i in range(0, len(scores)-self.len_mask+1, 1):
    #         to_be_masked_out = is_awake[i: i+self.len_mask]
    #         if all(to_be_masked_out):
    #             continue
    #         tmp_awake = tuple(is_awake[:i] + self.mask + is_awake[i+self.len_mask:])
    #         if tmp_awake not in self.memo:
    #             this_score = sum([s for s, w in zip(scores, tmp_awake) if w])
    #             self.memo[tmp_awake] = this_score
    #         may_get.append(self.memo[tmp_awake])
    #         # may_get.append(sum([s for s, w in zip(scores, tmp_awake) if w]))
    #     return max(may_get)

    def find_max_score(self, scores, is_awake):
        # missing_scores = []
        # for i in range(0, len(scores)-self.len_mask+1):
        #     if all(is_awake[i:i+self.len_mask]):
        #         continue
        #     missing_scores.append(sum([
        #         s for s, w in zip(scores[i:i+self.len_mask], is_awake[i:i+self.len_mask]) if not w
        #     ]))
        # return max(missing_scores) + sum([s for s, w in zip(scores, is_awake) if w])
        p1, p2 = 1, self.k+1
        max_missing_score = sum([s for s, w in zip(scores[:self.k], is_awake[:self.k]) if not w])
        cur_missing_score = sum([s for s, w in zip(scores[:self.k], is_awake[:self.k]) if not w])
        while p2 < len(scores):
            cur_missing_score -= scores[p1-1] if not is_awake[p1-1] else 0
            cur_missing_score += scores[p2] if not is_awake[p2] else 0
            if cur_missing_score > max_missing_score:
                max_missing_score = cur_missing_score
            p1 += 1
            p2 += 1
        return max_missing_score + sum([s for s, w in zip(scores, is_awake) if w])




if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())

    scores = list(map(int, sys.stdin.readline().strip().split()))
    is_awake = list(map(int, sys.stdin.readline().strip().split()))
    sol = Solution(k)
    print(sol.find_max_score(scores, is_awake))
    