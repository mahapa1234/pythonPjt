# encoding: utf-8

import unittest


class mmyclass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b


class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "---- setUpClass\n"

    @classmethod
    def tearDownClass(cls):
        print "---- tearDownClass\n"

    def setUp(self):
        self.a = 3
        self.b = 1
        print "-- setUP"

    def tearDown(self):
        print "-- tearDown"

    def testsum(self):
        self.assertEqual(mmyclass.sum(self.a, self.b), 4, 'test sum fail')

    def testsub(self):
        self.assertEqual(mmyclass.sub(self.a,self.b), 2, 'test sub fail')


if __name__ == '__main__':
    unittest.main()

