# -*- coding:utf-8 -*-

"""ACCEPT"""

class GrayCode:
    def getGray(self, n):
        # write code here
        graycode = ['0', '1']
        
        def pad_graycode(graycode, n):
            if n == 1:
                return graycode
            else:
                pad_0 = ['0' + gc for gc in graycode]
                pad_1 = ['1' + gc for gc in graycode[::-1]]
                graycode = pad_0 + pad_1
                return pad_graycode(graycode, n-1)

        return pad_graycode(graycode, n)

if __name__ == "__main__":
    GC = GrayCode()

    print(GC.getGray(4))