import sys
from queue import deque

class Solution:
    def func(self, initials, neighbors):
        print(neighbors)
        removed = {node: self.M(initials[:i]+initials[i+1:], neighbors) for i, node in enumerate(initials)}
        print(removed)
        return sorted(removed.items(), key=lambda x: (x[1], x[0]))
        
        
    def M(self, initials, neighbors):
        
        n = len(neighbors)
        indegree = [sum(i in v for k, v in neighbors.items()) for i in range(n)]
        print('indegree', indegree)

        myque = deque(initials)
        visited = set()
        while myque:
            node = myque.popleft()
            visited.add(node)

            for nb in neighbors[node]:
                if nb not in visited:
                    myque.append(nb)
        return len(visited)


if __name__ == "__main__":
    sol = Solution()
    n_row = int(input())
    mat = [list(map(int, input().split())) for _ in range(n_row)]
    initials = list(map(int, input().split()))
    neighbors = {i: [j for j, v in enumerate(d) if j != i and v] for i, d in enumerate(mat)}


    # print('INPUT')
    # print(n_row)
    # for row in mat:
    #     print(row)
    # print(initials)
    # print(sol.M(initials, neighbors))
    print(sol.func(initials, neighbors)[0][0])


'''
3
1 1 0
1 1 0
0 0 1
0 1

3
1 1 1
1 1 0
1 0 1
0 1

3
1 1 1
1 1 0
1 0 1
0 2


3
1 1 0
1 1 0
0 0 1
0 2
'''