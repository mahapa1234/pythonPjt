#encoding: utf-8

import unittest
import random


class  TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        # 初始化一个递增序列
        self.seq = range(10)

    def runTest(self):
        # 从序列seq中随机选取一个元素
        element = random.choice(self.seq)
        # 验证元素确实属于列表中
        self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

if __name__ == '__main__':
    unittest.main()
