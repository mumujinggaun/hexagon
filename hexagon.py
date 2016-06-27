# -*- coding:utf-8 -*-
# author：muweiqian 2016.6.21
import math

"""
问题描述：
    在正六边形网格中，以某网格为起点标号为1，六点钟方向顺时针连续标
    号至100000。1号网格的外圈标号为2~7，再外圈是8~19.....以此类推。
    相邻的网格距离为1，求任意给定的两标号之间的最短距离？
    
    可以计算距离时返回距离，无法计算时返回-1.
"""

def get_shortest_path_length(x, y):
    """To calculate shortest path length of two specified hexagon
    in the spiral rings hexagonal grids.
    
    :param x: an integer, number of first hexagon
    :param y: an integer, number of second hexagon
    
    :return length: an integer, the length of path, it will be -1
    when can not calculate the length.
    """
    assert isinstance(x, int)
    assert isinstance(y, int)
    
    def _get_coordinate(n):
        """get number n's coordinate (h, v) in the hexagon grids"""
        if n == 1:
            h, v = (0, 0)
        else:
            #确定标号n在第几圈上，1号是第0圈，2-7号第1圈，8-19号第2圈，依次类推
            ncicle = math.ceil(math.sqrt((n - 1) / 3) - 0.5)
            #print(ncicle)
            #n 和 n所在圈ncicle最大数的差值
            d = 3*(ncicle+1)*ncicle + 1 - n
            #print(d)
            if d <= ncicle:
                h = ncicle
                v = d - ncicle / 2
            elif d <= 3 * ncicle:
                h = 2 * ncicle - d
                v = ncicle - abs(d - 2 * ncicle) / 2
            elif d <= 4 * ncicle:
                h = - ncicle
                v = 7 / 2 * ncicle - d
            else:
                h = d - 5 * ncicle
                v = - ncicle + abs(d - 5 * ncicle) / 2
            #print(h,v)
        return (h, v)
    
    if x < 1 or x > 100000 or y < 1 or y > 100000:
        length = -1
    else:
        x_h, x_v = _get_coordinate(x)
        y_h, y_v = _get_coordinate(y)
        if abs(y_v - x_v) * 2 > abs(y_h - x_h):
            length = abs(y_v - x_v) + abs(y_h - x_h) / 2
        else:
            length = abs(y_h - x_h)
    #print(length)
    return length


####################################################
### unittest code, should be move to another module
####################################################

import unittest

class TestPathLengthFunction(unittest.TestCase):

    def test_outof_range(self):
        self.assertEqual(get_shortest_path_length(0, 1), -1)
        self.assertEqual(get_shortest_path_length(-1, 1), -1)
        self.assertEqual(get_shortest_path_length(1000001, 1), -1)
        
    def test_normal(self):
        self.assertEqual(get_shortest_path_length(1, 1), 0)
        self.assertEqual(get_shortest_path_length(100000, 100000), 0)
        self.assertEqual(get_shortest_path_length(1, 2), 1)
        self.assertEqual(get_shortest_path_length(100000, 99999), 1)
        self.assertEqual(get_shortest_path_length(1314, 1313), 1)
        self.assertEqual(get_shortest_path_length(1, 8), 2)
        self.assertEqual(get_shortest_path_length(141, 102), 2)
        self.assertEqual(get_shortest_path_length(91, 169), 2)
        self.assertEqual(get_shortest_path_length(106, 147), 3)
        self.assertEqual(get_shortest_path_length(13, 1), 2)
        self.assertEqual(get_shortest_path_length(1, 20), 3)
        self.assertEqual(get_shortest_path_length(126, 129), 3)
        self.assertEqual(get_shortest_path_length(82, 154), 3)
        self.assertEqual(get_shortest_path_length(7, 93), 5)
        self.assertEqual(get_shortest_path_length(7, 140), 7)
        self.assertEqual(get_shortest_path_length(164, 132), 10)
        self.assertEqual(get_shortest_path_length(134, 155), 14)
        self.assertEqual(get_shortest_path_length(19, 1), 2)
        self.assertEqual(get_shortest_path_length(84, 48), 7)
        self.assertEqual(get_shortest_path_length(84, 107), 9)
        self.assertEqual(get_shortest_path_length(77, 42), 8)
        self.assertEqual(get_shortest_path_length(7, 100), 6)
        self.assertEqual(get_shortest_path_length(7, 10000), 58)
        maxlength = 0
        for i in range(100000):
            for j in range(100000):
                if get_shortest_path_length(i, j) > maxlength:
                    maxlength = get_shortest_path_length(i, j)
                    print(i,j,get_shortest_path_length(i, j))
                j += 1
            i += 1

if __name__ == '__main__':
    unittest.main()
