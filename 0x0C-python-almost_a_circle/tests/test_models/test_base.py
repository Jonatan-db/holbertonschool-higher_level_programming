#!/usr/bin/python3
""" Unit tests for 1) models/base.py """


from models.base import Base
import unittest


class Test_Base(unittest.TestCase):

    def setUP(self):
        pass

    def tearDown(self):
        pass

    def test_docstring(self):
        self.assertIsNotNone(Base.__doc__)

    def test_simple(self):
        bae = Base(1)
        self.assertEqual(1, bae.id)
        self.assertNotEqual(99, bae.id)
        bae = Base(99)
        self.assertEqual(bae.id, 99)

    def test_InputErrors(self):
        with self.assertRaises(AttributeError):
            self.assertIsEqual(bae(), 1)

    def test_empty(self):
        bae = Base()
        self.assertEqual(1, bae.id)
        bae = Base(None)
        self.assertEqual(2, bae.id)
        bae = Base(None)
        self.assertEqual(3, bae.id)
        bae = Base(7)
        self.assertEqual(7, bae.id)

    def test_string(self):
        bae = Base(2)
        self.assertEqual(2, bae.id)
        bae = Base("2")
        self.assertEqual('2', bae.id)

    def test_float(self):
        bae = Base(3)
        self.assertEqual(3, bae.id)
        bae = Base(3.45)
        self.assertEqual(3.45, bae.id)
        bae = Base(-4.56)
        self.assertEqual(-4.56, bae.id)

    def test_weird(self):
        bae = Base(4)
        self.assertEqual(4, bae.id)
        bae = Base([1, 2])
        self.assertEqual([1, 2], bae.id)
        bae = Base([1, "2"])
        self.assertEqual([1, '2'], bae.id)
        bae = Base([1, [1, 2]])
        self.assertEqual([1, [1, 2]], bae.id)
        bae = Base({"needle": 2})
        self.assertEqual({"needle": 2}, bae.id)
        bae = Base((1, 2))
        self.assertEqual((1, 2), bae.id)
        bae = Base(1)
        self.assertEqual(1, bae.id)
        bae = Base()
        self.assertEqual(6, bae.id)

    def test_moreErrors(self):
        # with self.assertRaises(SyntaxError):
            # bae = base ( , )
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('NaN'))
        self.assertNotEqual(float('NaN'), bae.id)
        with self.assertRaises(ValueError):
            bae = Base(float('bob'))
        with self.assertRaises(ValueError):
            bae = Base(int('poop'))
        bae = Base()
        self.assertEqual(4, bae.id)

        # testing something
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        # done with testing

        bae = Base()
        self.assertEqual(5, bae.id)

if __name__ == "__main__":
    unittest.main()
