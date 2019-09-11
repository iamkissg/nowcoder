import numpy as np
import pandas as pd


def read_data():
    mnist = np.load('./mnist.npz')
    X = mnist['X']
    return X

def draw_once_able(pic):
    if np.all(pic):
        return True

    pos = set()
    for row in range(pic.shape[0]):
        for col in range(pic.shape[1]):
            if pic[row, col] == 0:
                continue

            pic[row, col] = 0
            pos.add((row, col))
            break
    
    while pos:
        cur_row, cur_col = pos.pop()
        if cur_row > 0 and cur_col > 0 and pic[cur_row-1, cur_col-1] == 255:
            pic[cur_row-1, cur_col-1] = 0; pos.add((cur_row-1, cur_col-1))
        if cur_row > 0 and pic[cur_row-1, cur_col] == 255:
            pic[cur_row-1, cur_col] = 0; pos.add((cur_row-1, cur_col))
        if cur_row > 0 and cur_col < 27 and pic[cur_row-1, cur_col+1] == 255:
            pic[cur_row-1, cur_col+1] = 0; pos.add((cur_row-1, cur_col+1))
        if cur_col > 0 and pic[cur_row, cur_col-1] == 255:
            pic[cur_row, cur_col-1] = 0; pos.add((cur_row, cur_col-1))
        if cur_col <27 and pic[cur_row, cur_col+1] == 255:
            pic[cur_row, cur_col+1] = 0; pos.add((cur_row, cur_col+1))
        if cur_row < 27 and cur_col > 0 and pic[cur_row+1, cur_col-1] == 255:
            pic[cur_row+1, cur_col-1] = 0; pos.add((cur_row+1, cur_col-1))
        if cur_row < 27 and pic[cur_row+1, cur_col] == 255:
            pic[cur_row+1, cur_col] = 0; pos.add((cur_row+1, cur_col))
        if cur_row < 27 and cur_col < 27 and pic[cur_row+1, cur_col+1] == 255:
            pic[cur_row+1, cur_col+1] = 0; pos.add((cur_row+1, cur_col+1))

    if np.any(pic):
        return False
    else:
        return True

X = read_data()
print(len([1 for x in X if draw_once_able(x)]))
