import sys
import re
from string import ascii_letters

"""ACCEPT"""

Uppers = list(ascii_letters[-26:])
Lowers = list(ascii_letters[:26])

u2l = {u:l for u, l in zip(Uppers, Lowers)}
l2u = {l:u for u, l in zip(Uppers, Lowers)}

continuous_relations = {''.join([t1, t2]) for t1, t2 in zip(Uppers[:-1], Uppers[1:])}

# print(u2l)
# print(l2u)

def remove_non_pair_letters(us, ls):
    for t in us:
        if u2l[t] not in ls:
            while t in us:
                us.remove(t)
    for t in ls:
        if l2u[t] not in us:
            while t in ls:
                ls.remove(t)
    
    return us, ls

for line in sys.stdin:
    s = line.strip()
    
    # remove non-alphabeta characters
    s = re.sub(r'[^A-Za-z]', '', s)
    # print('Len s', len(s))
    
    # seperate upper letters and lower letters
    us = [t for t in s if t in Uppers]
    ls = [t for t in s if t in Lowers]
    
    # print('Before removing non-pair letters', len(us), us)
    # print('Before removing non-pair letters', len(ls), ls)

    # remove non-pair letters
    us, ls = remove_non_pair_letters(us, ls)
    if not (us and ls):
        print('Not Found')
        continue
    
    # print('After removing non-pair letters', len(us), us)
    # print('After removing non-pair letters', len(ls), ls)

    # sort letters
    us_asc = sorted(us)
    ls_asc = sorted(ls)

    # print('After sorting 000000000 letters', len(us_asc), us_asc)
    # print('After sorting 000000000 letters', len(ls_asc), ls_asc)

    snakes = []
    while us_asc and ls_asc:
        csus = sorted(set(us_asc))
        snake = [csus[0]]
        longest_snake = [csus[0]]
        for t in csus[1:]:
            # not continuous
            if ''.join([snake[-1], t]) not in continuous_relations:
                if len(snake) > len(longest_snake):
                    longest_snake = snake
                snake = [t]
            # continuous letters
            else:
                snake.append(t)
        else:
            if len(snake) > len(longest_snake):
                longest_snake = snake
        snakes.append(''.join([''.join([t, u2l[t]]) for t in longest_snake]))
        for t in longest_snake:
            # print(t)
            us_asc.remove(t)
            ls_asc.remove(u2l[t])
            us_asc, ls_asc = remove_non_pair_letters(us_asc, ls_asc)
        # print('Longest snake', longest_snake)
        # print('US ASC', us_asc)
        # print('LS ASC', ls_asc)
        # print(snakes)
    snakes = sorted(snakes, key=lambda t: t[0] or len(t))
    for snk in snakes:
        print(snk)
    # sorted snakes
    

