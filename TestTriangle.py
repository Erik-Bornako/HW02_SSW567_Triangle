# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 is a Isoceles triangle')

    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 is a Isoceles triangle')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(8,10,12),'Scalene','8,10,12 is a Scalene triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(10,12,8),'Scalene','10,12,8 is a Scalene triangle')
    
    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(100,1,2),'NotATriangle','100,1,2 is not a triangle')
    
    def testInvaildInputA(self): 
        self.assertEqual(classifyTriangle('hello',1,2),'InvalidInput','hello,1,2 is invalid')

    def testInvaildInputB(self):
        self.assertEqual(classifyTriangle(300,400,500),'InvalidInput','300,400,500 is invalid')

    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

