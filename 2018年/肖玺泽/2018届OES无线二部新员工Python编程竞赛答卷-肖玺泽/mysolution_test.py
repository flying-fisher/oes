# -*- coding: utf-8 -*-

import unittest
from mysolution import Solution


class TestSolution(unittest.TestCase):

    # # 测试两字符串合法性判断功能
    # def test_isvalid(self):
    #     solution = Solution()
    #     self.assertFalse(solution.isvalid('111',''))
    #     self.assertFalse(solution.isvalid('','111aaa'))
    #     self.assertFalse(solution.isvalid('123*','aaa'))
    #     self.assertTrue(solution.isvalid('12A3abc','123aB5CD45'))
    #
    # # 测试数字子串比较功能
    # def test_cmpnumber(self):
    #     solution = Solution()
    #     self.assertEquals(solution.cmpnumber('123','456'), -1)
    #     self.assertEquals(solution.cmpnumber('123', '123'), 0)
    #     self.assertEquals(solution.cmpnumber('456', '123'), 1)
    #     self.assertEquals(solution.cmpnumber('123', '0123'), -1)
    #     self.assertEquals(solution.cmpnumber('0123', '123'), 1)
    #
    # # 测试字母子串比较功能
    # def test_cmpletter(self):
    #     solution = Solution()
    #     self.assertEquals(solution.cmpletter('abc', 'def'), cmp('abc', 'def'))
    #     self.assertEquals(solution.cmpletter('abc', 'ABC'), cmp('abc', 'ABC'))
    #
    #
    # # 测试子串比较功能
    # def test_cmpsubstr(self):
    #     solution = Solution()
    #     self.assertEquals(solution.cmpsubstr('123', '456'), -1)
    #     self.assertEquals(solution.cmpsubstr('123', '123'), 0)
    #     self.assertEquals(solution.cmpsubstr('456', '123'), 1)
    #     self.assertEquals(solution.cmpsubstr('123', '0123'), -1)
    #     self.assertEquals(solution.cmpsubstr('0123', '123'), 1)
    #     self.assertEquals(solution.cmpsubstr('123', 'abc'), -1)
    #     self.assertEquals(solution.cmpsubstr('abc', '123'), 1)
    #     self.assertEquals(solution.cmpsubstr('abc', 'Bac'), cmp('abc','Bac'))

    # 检查空字符串
    def test_001(self):
        solution = Solution()
        self.assertEquals(solution.cmpstr('', '123abc'), -2)
        self.assertEquals(solution.cmpstr('123abc', ''), -2)
        self.assertEquals(solution.cmpstr('', ''), -2)

    # 检查非法字符
    def test_002(self):
        solution = Solution()
        self.assertEquals(solution.cmpstr('123@abc', '123abc'), -2)
        self.assertEquals(solution.cmpstr('123abc','123@abc'), -2)
        self.assertEquals(solution.cmpstr(r'123\abc','123哈abc'), -2)

    # 检查数字字符串的比较
    def test_003(self):
        solution = Solution()
        self.assertEquals(solution.cmpstr('123', '456'), -1)
        self.assertEquals(solution.cmpstr('456', '123'), 1)
        self.assertEquals(solution.cmpstr('123', '0123'), -1)
        self.assertEquals(solution.cmpstr('0123', '123'), 1)
        self.assertEquals(solution.cmpstr('123', '123'), 0)

    # 检查字母字符串的比较
    def test_004(self):
        solution = Solution()
        self.assertEquals(solution.cmpstr('abc', 'ABC'), cmp('abc', 'ABC'))
        self.assertEquals(solution.cmpstr('abc', 'def'), cmp('abc', 'def'))

    # 检查数字字符串与字母字符串的比较
    def test_005(self):
        solution = Solution()
        self.assertEquals(solution.cmpstr('123', 'abc'), -1)
        self.assertEquals(solution.cmpstr('abc', '123'), 1)

    # 检查包含数字与字母字符串的比较
    def test_006(self):
        solution = Solution()
        # 左一子串不等时
        self.assertEquals(solution.cmpstr('123abc', 'abc123'), -1)
        self.assertEquals(solution.cmpstr('abc123', '123abc'), 1)
        # 左一子串相等时
        self.assertEquals(solution.cmpstr('123', '123abc'), -1)
        self.assertEquals(solution.cmpstr('123abc', '123'), 1)
        self.assertEquals(solution.cmpstr('123abc', '123abc'), 0)
        self.assertEquals(solution.cmpstr('B1', 'B01'), -1)
        self.assertEquals(solution.cmpstr('B01', 'B2'), -1)
        self.assertEquals(solution.cmpstr('B2', 'B11'), -1)