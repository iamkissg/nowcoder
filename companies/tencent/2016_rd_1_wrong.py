# -*- coding:utf-8 -*-

"""BAD_IDEA"""

class GrayCode:

    def getGray(self, n):
        # write code here
        graycode = ['0'*n]
        
        def change_one_pos(gc):
            last_code = list(gc[-1])
            for i in range(1, n+1):
                new_code = last_code[:]
                new_code[-i] = '0' if new_code[-i] == '1' else '1'
                if ''.join(new_code) in gc:
                    if i != n:
                        continue
                    else:
                        return gc
                else:
                    return change_one_pos(gc + [''.join(new_code)])
                    
        
        return change_one_pos(graycode)

if __name__ == "__main__":
    GC = GrayCode()

    print(GC.getGray(4))