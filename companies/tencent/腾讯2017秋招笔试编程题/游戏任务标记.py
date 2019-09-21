# __author__ = 'iamkissg'
# __date__ = 20190920


# 100% passed


def is_valid(i):
    return 1 <= i <= 1024


id_1, id_2 = map(int, input().split())

if not is_valid(id_1) or not is_valid(id_2):
    print(-1)
else:
    print(1 if id_1 == id_2 else 0)