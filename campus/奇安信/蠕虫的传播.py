import sys
from queue import deque

'''
88%
'''

class Solution:
    def func(self, initials, neighbors):
        removed = {node: self.M(initials[:i]+initials[i+1:], neighbors) for i, node in enumerate(initials)}
        return sorted(removed.items(), key=lambda x: (x[1], x[0]))
        
        
    def M(self, initials, neighbors):

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
    neighbors = {i: [j for j, v in enumerate(d) if i!=j if v] for i, d in enumerate(mat)}

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