import sys


# def generator(arr):
#     for i in range(len(arr-1)):
#         for j in range(i, len(arr)):
#             yield j-i if arr[i]>arr[j] else 0



if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(sum([j-i if arr[i]>arr[j] else 0 for i in range(len(arr)-1) for j in range(i, len(arr))]))
    # print(sum(generator(arr)))