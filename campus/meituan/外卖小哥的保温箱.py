# n = int(input())

# As = list(map(int, input().split()))
# Bs = list(map(int, input().split()))


def sort_box(box1, box2):
    if box1[0] < box2[0]:
        return True
    elif box1[0] == box2[0]:
        if box1[1] > box2[1]:
            return True
    else:
        return False

def how_many_and_how_much_time(As, Bs):

    Cs = [b-a for a, b in zip(As, Bs)]
    sum_A = sum(As)
    BCs = [(b, c) for b, c in zip(Bs, Cs)]
    sorted_B = sorted(BCs, key=lambda bc: (bc[0], bc[1]), reverse=True)
    # print(sorted_B)
    selected_indexes = []
    volume = 0
    for i, (b, c) in enumerate(sorted_B):
        volume += b
        idx = BCs.index((b, c))
        # print(BCs, (b, c), idx)
        if idx in selected_indexes:
            # print('B', idx)
            # print('B', BCs[idx+1:])
            idx = idx+1+BCs[idx+1:].index((b, c))
            # print('A', idx)
        selected_indexes.append(idx)
        if volume >= sum_A:
            break
    # print(selected_indexes)
    k = len(selected_indexes)
    t = sum([a for i, a in enumerate(As) if i not in selected_indexes])
    return k, t


if __name__ == "__main__":
    print(how_many_and_how_much_time([3, 4, 2, 3], [4, 13, 13, 5]))
    print(how_many_and_how_much_time([3, 3, 4, 3], [4, 13, 6, 5]))
