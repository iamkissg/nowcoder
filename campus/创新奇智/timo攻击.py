import sys

class Solution:
    def get_poisonious_time(self, attack_times, last_time):
        t = set()
        for at in attack_times:
            t.update(range(at, at+last_time))
        return len(t)


if __name__ == "__main__":
    sol = Solution()
    attack_times, last_time = input().split(',')
    attack_times = list(map(int, attack_times.strip().split()))
    last_time = int(last_time.strip())
    print(sol.get_poisonious_time(attack_times, last_time))