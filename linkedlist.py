class Node:
    def __init__(self, data):
        self.data = data
        self.then = None

class LinkedList:
    def __init__(self, *datas):
        self.init = None
        if datas:
            self.datas = datas
            self.__Append()
        else:
            pass

    def __len__(self, element=None, n=1):
        if element is None:
            element = self.init
        if element:
            if element.then is None:
                return n
            else:
                return self.__len__(element.then, n+1)
        else:
            return 0

    def __iter__(self):
        if self.init is None:
            yield
        element = self.init
        while element is not None:
            yield element.data
            element = element.then

    def GetIndexOfItem(self, data) -> bool:
        if self.init is None:
            return
        n = self.init
        num = 0
        while n is not None:
            if n.data == data:
                return (num)
            n = n.then
            num += 1
            
    def __GetItemByIndex(self, index):
        if self.init is None or index > self.__len__():
            raise IndexError('Index out of range')

        current_node : Node = self.init
        while index > 0:
            current_node = current_node.then
            index -= 1
        return current_node.data      

    def __getitem__(self,index):
        return self.__GetItemByIndex(index)

    def __setitem__ (self, __name: int, __value ) -> None:
        self.ChangeElementByIndex(__name, __value)

    def Traverse(self, element=None):
        if element is None:
            element = self.init
            print("<", end=" ")
        if element:
            if element.then is None:
                print(f"{element.data} >")
                return
            else:
                print(f"{element.data}, ", end="")
            self.Traverse(element.then)
        else:
            print(">")
    
    # < 1, 2, 3 >

    def TraversalPointer(self, element=None):
        # box = u"\u24AD"
        box = u"\u25AD"
        if element is None:
            element = self.init
        if element:
            if element.then is None:
                print(f"{element.data}{box}->None")
                return
            else:
                print(f"{element.data}{box}->",end="")
            self.TraversalPointer(element.then)
        else:
            print("No element")

    # 1[]-> 2[]-> dst... None

    def InsertAtFront(self, item):
        Element = Node(item)
        Element.then = self.init
        self.init = Element
    
    def InsertAtEnd(self, item, element=None):
        if self.init is None:
            self.init = Node(item)
            return
        if element is None:
            element = self.init
        if element.then is None:
            element.then = Node(item)
        else:
            self.InsertAtEnd(item, element.then)
        # return element

    def InsertAtIndex(self, idx, item, element=None, n=0):
        if idx == 0:
            self.InsertAtFront(item)
            return
        if idx == self.__len__():
            self.InsertAtEnd(item)
            return
        if element is None:
            element = self.init
        if idx < self.__len__():
            if idx - 1 == n:
                newelement = Node(item)
                newelement.then = element.then
                element.then = newelement
            else:
                self.InsertAtIndex(idx, item, element.then, n+1)
            # return element
        else:
            raise IndexError('Index out of range') 

    def InsertAtPos(self, pos, item, element=None, n=1):
        if pos == 1:
            self.InsertAtFront(item)
            return
        if element is None:
            element = self.init
        if pos < self.__len__()+1:
            if pos - 1 == n:
                newelement = Node(item)
                newelement.then = element.then # d, e, f
                element.then = newelement
            else:
                self.InsertAtPos(pos, item, element.then, n+1)
            # return element
        else:
            print('Position out of range')  

    def DeleteAtFront(self):
        if self.init is None:
            print("List has no element")
            return
        self.init = self.init.then

    def DeleteAtEnd(self, element=None):
        if self.init is None:
            print("List has no element")
            return
        if element is None:
            element = self.init
        if element:
            if element.then.then is None:
                element.then = None
            else:
                self.DeleteAtEnd(element.then)
        else:
            print('No element')
        # return element

    def DeleteAtIndex(self, idx, element=None, n=0):
        if idx == 0:
            self.DeleteAtFront()
            return
        if idx == self.__len__()-1:
            self.DeleteAtEnd()
            return

        if element is None:
            element = self.init
        if idx < self.__len__()-1:
            if idx == n:
                element.data = element.then.data
                element.then = element.then.then
            else:
                self.DeleteAtIndex(idx, element.then, n+1)
        else:
            raise IndexError('Index out of range')

    def DeleteAtPos(self, pos, element=None, n=1):
        if pos == 1:
            self.DeleteAtFront()
            return
        if pos == self.__len__():
            self.DeleteAtEnd()
            return

        if element is None:
            element = self.init
        if pos < self.__len__():
            if pos - 1 == n:
                # element.then = element.then.then
                current = element.then.then
                element.then = current
                element = None
                # current.then.then = element
            else:
                self.DeleteAtIndex(pos, element.then, n+1)
        else:
            print('Position out of range')

    def DeleteElement(self, item, element=None):
        if item == self.init.data:
            self.DeleteAtFront()
            return
            
        if element is None:
            element = self.init

        if item == element.data:
            if element.then is not None:
                element.data = element.then.data
                element.then = element.then.then
            else:
                self.DeleteAtEnd()
        else:
            self.DeleteElement(item, element.then)

    def ChangeElementByIndex(self, idx, data, element=None, n=0):
        if idx == 0:
            self.DeleteAtFront()
            self.InsertAtFront(data)
            return
        if idx == self.__len__()-1:
            self.DeleteAtEnd()
            self.InsertAtEnd(data)
            return

        if element is None:
            element = self.init
        if idx < self.__len__()-1:
            if idx == n:
                element.data = data
            else:
                self.ChangeElementByIndex(idx, data, element.then, n+1)
        else:
            raise IndexError('Index out of range')
    
    def ChangeElementByPos(self, pos, data, element=None, n=1):
        if pos == 1:
            self.DeleteAtFront()
            self.InsertAtFront(data)
            return
        if pos == self.__len__():
            self.DeleteAtEnd()
            self.InsertAtEnd(data)
            return

        if element is None:
            element = self.init
        if pos < self.__len__():
            if pos == n:
                element.data = data
            else:
                self.ChangeElementByIndex(pos, data, element.then, n+1)

    def SearchItem(self, x) -> bool:
        if self.init is None:
            print("List has no elements")
            return
        n = self.init
        while n is not None:
            if n.data == x:
                print("Item found")
                return True
            n = n.then
        print("Item not found")
        return False

    def ExtendList(self, ll):
        n = self.init
        while n.then:
            n = n.then
        n.then = ll.init

    def SumList(self) -> int:
        if self.init is None:
            return 0
        n = self.init
        summation = 0
        while n is not None:
            summation += n.data
            n = n.then
        return summation

    def ReversePointer(self):
        prev = None
        n = self.init
        while n is not None:
            ref = n.then
            n.then = prev
            prev = n
            n = ref
        self.init = prev
    
    def InsertionSort(self, data):
        newNode = Node(data)
        if self.init is None:
            self.init = newNode
            return
        n = self.init
        while n.then is not None:
            n= n.then
        n.then = newNode

        n = self.init
        index = None
        while n is not None:    
            index = n.then
                
            while index is not None:  
                if n.data > index.data:  
                    temp = n.data
                    n.data = index.data
                    index.data = temp  
                index = index.ref
            n = n.then

    def __Append(self):
        for i in self.datas:
            self.InsertAtEnd(i)

# y = LinkedList(1,2,3,4)
# print(y.GetIndexOfItem(2))