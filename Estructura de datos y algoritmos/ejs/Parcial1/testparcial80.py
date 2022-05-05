# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:06:49 2022

@author: ishernanz
"""
import unittest
from parcial80 import MyDList


class Test(unittest.TestCase):

    mark=0

    def setUp(self):
        self.S0,self.S1=MyDList(),MyDList()
        
    def test1_emptyList(self):  
        #S0: empty list
        self.assertEqual(None,self.S0.removeBehindTwice(5),'FAIL: should be none for an empty list')
        
        print('test1_emptyList was OK!!!: ', None)
        Test.mark+=0.25
        
    def test2_1elemList(self): 
        #S0: list with one element
        self.S0.append(5)
        expected=self.S0
        self.S0.removeBehindTwice(5)
        result=self.S0
        self.assertEqual(len(expected),len(result),'FAIL: expected list and result list have different lenghts')
        self.assertEqual(expected._head,result._head,'expected list and result list have different heads')
        self.assertEqual(expected._tail,result._tail,'expected list and result list have different tails')
        self.assertEqual(str(expected),str(result),'FAIL: expected list and result are not equal')
        
        print('test2_1elemList was OK!!!: ', result)
        Test.mark+=0.75
        
    def test3_2elemList(self):
        #S0: list with two elements (before) S0=[5,7]
        self.S0.append(7)
        #S1: list with two elements (after e=5) S1=[7]
        self.S1.append(7)
        expected=self.S1
        self.S0.removeBehindTwice(5)
        result=self.S0
        self.assertEqual(len(expected),len(result),'FAIL: expected list and result list have different lenghts')
        self.assertEqual(expected._head.elem,result._head.elem,'expected list and result list have different heads')
        self.assertEqual(expected._tail.elem,result._tail.elem,'expected list and result list have different tails')
        self.assertEqual(str(expected),str(result),'FAIL: expected list and result are not equal')
        
        print('test3_2elemList was OK!!!: ', result)
        Test.mark+=1        
        
    def test4_3elemList(self):
        #S0: list with three elements (before) S0=[7,4,5]
        self.S0.append(7)
        self.S0.append(4)
        self.S0.append(5)
        #S1: list with three elements (after e=7) S1=[7]
        self.S1=MyDList()
        self.S1.append(7)
        expected=self.S1
        self.S0.removeBehindTwice(7)
        result=self.S0
        self.assertEqual(len(expected),len(result),'FAIL: expected list and result list have different lenghts')
        self.assertEqual(expected._head.elem,result._head.elem,'expected list and result list have different heads')
        self.assertEqual(expected._tail.elem,result._tail.elem,'expected list and result list have different tails')
        self.assertEqual(str(expected),str(result),'FAIL: expected list and result are not equal')
        
        print('test4_3elemList was OK!!!: ', result)
        Test.mark+=1  
     
    def test5_nelemList_e_middle(self):
        #S0: list with many elements (before) S0=[5,7,4,8,9,2,1,4,3]
        self.S0.append(5)
        self.S0.append(7)
        self.S0.append(4)
        self.S0.append(8)
        self.S0.append(9)
        self.S0.append(2)
        self.S0.append(1)
        self.S0.append(4)
        self.S0.append(3)
        #S1: list with many elements (after e=9) S1=[5,7,4,8,9,4,3]
        self.S1.append(5)
        self.S1.append(7)
        self.S1.append(4)
        self.S1.append(8)
        self.S1.append(9)
        self.S1.append(4)
        self.S1.append(3)
        expected=self.S1
        self.S0.removeBehindTwice(9)
        result=self.S0
        self.assertEqual(len(expected),len(result),'FAIL: expected list and result list have different lenghts')
        self.assertEqual(expected._head.elem,result._head.elem,'expected list and result list have different heads')
        self.assertEqual(expected._tail.elem,result._tail.elem,'expected list and result list have different tails')
        self.assertEqual(str(expected),str(result),'FAIL: expected list and result are not equal')
        
        print('test5_nelemList_e_middle was OK!!!: ', result)
        Test.mark+=2
      
    def test6_nelemList_e_firstpos(self): 
        #S0: list with many elements (before) S0=[5,7,9,2,1,4,3]
        self.S0.append(5)
        self.S0.append(7)
        self.S0.append(9)
        self.S0.append(2)
        self.S0.append(1)
        self.S0.append(4)
        self.S0.append(3)
        #S1: list with many elements (after e=5) S1=[5,2,1,4,3]
        self.S1.append(5)
        self.S1.append(2)
        self.S1.append(1)
        self.S1.append(4)
        self.S1.append(3)
        expected=self.S1
        self.S0.removeBehindTwice(5)
        result=self.S0
        self.assertEqual(len(expected),len(result),'FAIL: expected list and result list have different lenghts')
        self.assertEqual(expected._head.elem,result._head.elem,'expected list and result list have different heads')
        self.assertEqual(expected._tail.elem,result._tail.elem,'expected list and result list have different tails')
        self.assertEqual(str(expected),str(result),'FAIL: expected list and result are not equal')
        
        print('test6_nelemList_e_lastpos was OK!!!: ', result)
        Test.mark+=2 
            
    def test7_nelemList_e_twice(self): 
        #S0: list with many elements (before) S0=[5,7,3,5,1,4,3]
        self.S0.append(5)
        self.S0.append(7)
        self.S0.append(3)
        self.S0.append(5)
        self.S0.append(1)
        self.S0.append(4)
        self.S0.append(3)
        #S1: list with many elements (after e=5) S1=[5,5,1,4,3]
        self.S1.append(5)
        self.S1.append(5)
        self.S1.append(1)
        self.S1.append(4)
        self.S1.append(3)
        expected=self.S1
        self.S0.removeBehindTwice(5)
        result=self.S0
        self.assertEqual(len(expected),len(result),'FAIL: expected list and result list have different lenghts')
        self.assertEqual(expected._head.elem,result._head.elem,'expected list and result list have different heads')
        self.assertEqual(expected._tail.elem,result._tail.elem,'expected list and result list have different tails')
        self.assertEqual(str(expected),str(result),'FAIL: expected list and result are not equal')
        
        print('test7_nelemList_e_twice was OK!!!: ', result)
        Test.mark+=2
        
    def test8_e_notinList(self): 
        #S0: list with many elements (before) S0=[5,7,3,2,1,4,3]
        #S0: list with many elements (after e=8) S0=[5,7,3,2,1,4,3]
        self.S0.append(5)
        self.S0.append(7)
        self.S0.append(3)
        self.S0.append(2)
        self.S0.append(1)
        self.S0.append(4)
        self.S0.append(3)
        expected=self.S0
        self.S0.removeBehindTwice(8)
        result=self.S0
        self.assertEqual(len(expected),len(result),'FAIL: expected list and result list have different lenghts')
        self.assertEqual(expected._head.elem,result._head.elem,'expected list and result list have different heads')
        self.assertEqual(expected._tail.elem,result._tail.elem,'expected list and result list have different tails')
        self.assertEqual(str(expected),str(result),'FAIL: expected list and result are not equal')
        print('test8_e_notinList was OK!!!: ', result)
        Test.mark+=1
        
    def test_showmark(self):
        print('Total mark is ', Test.mark)    
        
if __name__ == '__main__':
    unittest.main()