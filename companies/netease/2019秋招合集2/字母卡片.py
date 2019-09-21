import sys

# 100% passed

def get_m_cards(alphabet, m):
    counter = {}
    for c in alphabet:
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    sorted_counter = sorted(counter.values(), reverse=True)

    result = 0
    for v in sorted_counter:
        if m - v >= 0:
            result += v * v
            m -= v
        else:
            result += m * m
            break
    return result


if __name__ == "__main__":

    for line in sys.stdin:
        n, m = map(int, line.strip().split())
        alphabet = sys.stdin.readline().strip()

        result = get_m_cards(alphabet, m)
        print(result)