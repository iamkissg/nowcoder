import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    points = []
    for _ in range(N):
        pt = map(int, sys.stdin.readline().strip().split())
        points.append(tuple(pt))

    x_max = max(pt[0] for pt in points)
    y_max = max(pt[1] for pt in points)

