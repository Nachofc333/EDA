# -*- coding: utf-8 -*-
import unittest

class DNode:
  def __init__(self,elem,next=None,prev=None ):
    self.elem = elem
    self.next = next
    self.prev = prev
    
    
class DList:
    def __init__(self):
        """creates an empty list"""
        self._head=None
        self._tail=None
        self._size=0
    
    def __len__(self):
        return self._size

    def isEmpty(self):
        """Checks if the list is empty"""
        #return self.head == None   
        return len(self)==0
  
    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used 
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt=self._head
        result='['
        while nodeIt:
            if type(nodeIt.elem)==int:
                result+= str(nodeIt.elem)+ ", "
            else:
                result+= "'"+str(nodeIt.elem)+ "', "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result

    
    def addFirst(self,e):
        """Add a new element, e, at the beginning of the list"""
        #create the new node
        newNode=DNode(e)                                   
        #the new node must point to the current head
        
        if self.isEmpty():                                
            self._tail=newNode                               
        else:
            newNode.next=self._head                          
            self._head.prev=newNode                          
        
        #update the reference of head to point the new node
        self._head=newNode                                 
        #increase the size of the list  
        self._size+=1                             
        
    

    def addLast(self,e):
        """Add a new element, e, at the end of the list"""
        #create the new node
        newNode=DNode(e)
        
        if self.isEmpty():
            self._head=newNode
        else:
            newNode.prev=self._tail
            self._tail.next=newNode
        
        #update the reference of head to point the new node
        self._tail=newNode
        #increase the size of the list  
        self._size+=1

   
   
    def removeFirst(self):
        """Returns and remove the first element of the list"""
        result=None
        if self.isEmpty():
            print("Error: list is empty")
        else:
            result=self._head.elem 
            
            self._head= self._head.next 
            if self._head==None:
                self._tail=None
            else:
                self._head.prev = None

            self._size-=1

        return result
    
    def removeLast(self):
        """Returns and remove the last element of the list"""
        result=None

        if self.isEmpty():
            print("Error: list is empty")
        else:
            result=self._tail.elem                       
            self._tail= self._tail.prev                 
            if self._tail==None:
                self._head=None
            else:
                self._tail.next = None

            self._size-=1

        return result
  
 
    def getAt(self,index):
        """return the element at the position index.
        If the index is an invalid position, the function
        will return -1"""
        result=None
        if index not in range(0,len(self)): 
            print(index,'Error getAt: index out of range')
        else:
            nodeIt=self._head
            i=0
            while nodeIt and i<index:
                nodeIt=nodeIt.next
                i+=1

            #nodeIt is at the position index
            result=nodeIt.elem

        return result

    def index(self,e):
        """returns the first position of e into the list.
        If e does not exist in the list, 
        then the function will return -1"""
        nodeIt=self._head
        index=0
        while nodeIt:
            if nodeIt.elem==e:
                return index
            nodeIt=nodeIt.next
            index+=1
            
        #print(e,' does not exist!!!')
        return -1 

    def insertAt(self,index,e):
        if index not in range(len(self)+1):
            print('Error: index out of range')
        elif index==0:
            self.addFirst(e)
        elif index==len(self): 
            self.addLast(e)
        else:
            nodeIt=self._head
            for i in range(index):
                nodeIt=nodeIt.next
            #nodeIt is the node at the index
            previous=nodeIt.prev
        
            newNode=DNode(e)
            #we have to insert the new node before nodeIt
            newNode.next=nodeIt
            newNode.prev=previous

            previous.next=newNode
            nodeIt.prev=newNode
            self._size+=1
      
      
    

    
    def removeAt(self,index):
        """This methods removes the node at the index position in the list"""
        
        #We must check that index is a right position in the list
        #Remember that the indexes in a list can range from 0 to size-1
        result=None
        if index not in range(len(self)): 
            print(index,'Error removeAt: index out of range')
        elif index==0:
            result= self.removeFirst()
        elif index==len(self)-1:
            result= self.removeLast()
        else:
            nodeIt=self._head
            for i in range(index):
                nodeIt=nodeIt.next

            #nodeIt is the node to be removed
            result=nodeIt.elem
            prevNode=nodeIt.prev
            nextNode=nodeIt.next
            
            prevNode.next=nextNode
            nextNode.prev=prevNode
            self._size-=1
        
        return result

    def GetAtRev(self, index):
        if index >= self._size:
            print("Index out of range")
            return
        current = self._tail
        for i in range(index):
            current = current.prev
        return current.elem

    def removeAll(self, e):
        current = self._head
        c = 0
        while current:
            if current.elem==e:
                self.removeAt(c)
            else:
                c += 1
            current = current.next

    def removefronttwice(self, e):
        current = self._head
        if len(self) == 0:
            return
        while current:
            if current.elem == e:
                current.prev = current.prev.prev.prev
                current.prev.next = current.prev
            current = current.next

    def removeFrontTwice(self,e):
        """Eliminates two elements behind the first occurence of e"""
        current = self._head
        prev = 0

        if len(self) == 0:
            return
        if len(self) == 1:
            return
        for i in range(self._size):
            if current.elem == e:
                prev = i
            current = current.next
        current = self._head
        for i in range(prev-3):
            current = current.next
        current.next = current.next.next.next
        current.next.prev = current
        self._size -= 2

L = DList()
for i in range(10):
    L.addFirst(i)

print(L)
L.removefronttwice(4)
print(L)


if __name__=='__main__':
    import random
    l=DList()




