# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:06:49 2022

@author: ishernanz
"""
import unittest
from parcial280 import MyBST


class Test(unittest.TestCase):

    mark=0

    def setUp(self):
        self.T0,self.T1,self.T2,self.T3,self.T4,self.T5,self.T6,self.T7,self.T8,self.T9=MyBST(),MyBST(),MyBST(),MyBST(),MyBST(),MyBST(),MyBST(),MyBST(),MyBST(),MyBST()
        L1=[51,30,68,19,60,70,8,22,69]
        L2=[70,30,73,14,34,76,11,16,60,87,44,81,35,47,39]
        L3=[49,28,59,21,33,74,1,30,42,61,88,11]
        L4=[80,64,86,50,72,92,14,56,9,25,17,33,31,28]
        L5=[52,51,67,38,79,31,69,86,88,96]
        L6=[41,20,65,11,29,50,91,52,72,99]
        L7=[15,6,23,4,7,71,5,50]
                
        for i in L1:    
            self.T1.insert(i)
                
        for i in L2:    
            self.T2.insert(i)
        
        for i in L3:
            self.T3.insert(i)
            
        for i in L4:
            self.T4.insert(i)
        
        for i in L5:
            self.T5.insert(i)
            
        for i in L6:
            self.T6.insert(i)
            
        for i in L7:
            self.T7.insert(i)
            
    def test1_emptyTree(self):  
        #T0: empty tree
        self.assertEqual([],self.T0.get_odd_siblings(),'FAIL: should be an empty list for an empty tree')
        
        print('test1_emptyTree was OK!!!: ')
        Test.mark+=0.25
        
    def test1_1stExample(self):  
        #T1: no nodes to print
        self.assertEqual([],self.T1.get_odd_siblings(),'FAIL: should be an empty list for this tree')
        
        print('test1_1st Example was OK!!!: ')
        Test.mark+=0.75   
    
    def test2_2ndExample(self):  
        #T2: 2nd example
        self.assertEqual([47,35,30,16],self.T2.get_odd_siblings(),'FAIL: expected and result lists not equal')
        
        print('test2_2ndExample was OK!!!: ')
        Test.mark+=1.5 
        
    def test3_3rdExample(self):  
        #T3: 3rd example
        self.assertEqual([88,33,28,21],self.T3.get_odd_siblings(),'FAIL: expected and result lists not equal')
        
        print('test3_3rdExample was OK!!!: ')
        Test.mark+=1.5 
        
    def test4_4thExample(self):  
        #T4: 4th example
        self.assertEqual([33,25,17,9],self.T4.get_odd_siblings(),'FAIL: expected and result lists not equal')
        
        print('test4_4thExample was OK!!!: ')
        Test.mark+=1.5
    def test5_5thExample(self):  
        #T5: 5th example
        self.assertEqual([86,67,51],self.T5.get_odd_siblings(),'FAIL: expected and result lists not equal')
        
        print('test5_5thExample was OK!!!: ')
        Test.mark+=1.5 
        
    def test6_6thExample(self):  
        #T6: 6th example
        self.assertEqual([72,50,29,20,11],self.T6.get_odd_siblings(),'FAIL: expected and result lists not equal')
        
        print('test6_6thExample was OK!!!: ')
        Test.mark+=1.5
        
    def test7_7thExample(self):  
        #T7: 7th example
        self.assertEqual([6,4],self.T7.get_odd_siblings(),'FAIL: expected and result lists not equal')
        
        print('test7_7thExample was OK!!!: ')
        Test.mark+=1.5    
        
    def test_showmark(self):
        print('Total mark is ', Test.mark)    
        
if __name__ == '__main__':
    unittest.main()
    