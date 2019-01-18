from sourceCode import myCompare
import unittest
import random
import string
class UnitTest(unittest.TestCase):
    "单元测试类"
    def test_case1(self):
        "test.txt文件中，每一行通过\t分割，第一个为字符串1，第二个为字符串2，第三个为期望的结果"
        with open('test.txt','r',encoding='UTF-8') as cin:
            for line in cin:
                line = line[:-1]#去掉输入文件中的换行符
                temp = line.split("\t")
                if len(temp) > 1:
                    self.assertEqual(myCompare(temp[0], temp[1]), int(temp[2]))

    def test_case2(self):
        "生成若干随机字符串并进行比较，考察是否有异常输出"
        str_a = ''.join(random.sample(string.printable, random.randint(0, 30)))
        str_b = ''.join(random.sample(string.printable, random.randint(0, 30)))
        print(str_a)
        print(str_b)
        self.assertIn(myCompare(str_a, str_b), [0, 1, -1, -2])
if __name__ == '__main__':
    #执行单元测试主程序
    unittest.main()