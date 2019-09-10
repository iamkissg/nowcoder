# -*- coding:utf-8 -*-


"""
最简单的解法是, 遍历数组, 找到最小元素, 但是没有把"非递减数组的旋转数组"这一特点利用起来.
非递减数组的旋转数组, 在最小元素之前的元素, 都比之后的元素大. 且前后两个数组都是有序的.
对于有序数组的有效搜索算法是, 二分查找, 用于快速定位最小元素所在区间.
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        
        def minInOrder(array, pos1, pos2):
            """当二分查找不可行时, 用顺序查找法"""
            result = array[pos1]
            for i in range(pos1, pos2+1):
                if result > array[i]:
                    result = array[i]
            return result
            
        if len(rotateArray) == 0:
            return 0
        else:
            pos1, pos2 = 0, len(rotateArray)-1
            mid_pos = pos1
            while rotateArray[pos2] <= rotateArray[pos1]:
                if pos1+1 == pos2:
                    mid_pos = pos2
                    break
                mid_pos = (pos1 + pos2)//2
                
                if rotateArray[pos1] == rotateArray[pos2] and rotateArray[pos1] == rotateArray[mid_pos]:
                    return minInOrder(rotateArray, pos1, pos2)
                if rotateArray[mid_pos] >= rotateArray[pos1]:
                    pos1 = mid_pos
                elif rotateArray[mid_pos] <= rotateArray[pos2]:
                    pos2 = mid_pos
                
            return rotateArray[mid_pos]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minNumberInRotateArray([6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]))