import sys

# 100% passed

class Solution:

    def attack(self, hp, normal_attack, buffed_atttack):
        if normal_attack * 2 >= buffed_atttack:
            result, rest = divmod(hp, normal_attack)
            return result + (1 if rest else 0)
        else:
            result, rest = divmod(hp, buffed_atttack)
            result *= 2
            if not rest:
                return result
            else:
                return result + (1 if rest <= normal_attack else 2)


if __name__ == "__main__":
    hp = int(sys.stdin.readline().strip())
    normal_attack = int(sys.stdin.readline().strip())
    buffed_attack = int(sys.stdin.readline().strip())

    sol = Solution()
    print(sol.attack(hp, normal_attack, buffed_attack))