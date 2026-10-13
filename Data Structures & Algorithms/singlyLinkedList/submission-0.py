class node: 
    def __init__(self, data: int, next: "node or Null" = None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        if self.head == None: 
            return -1

        i = 0
        curr = self.head
        while i < index and curr != None: 
            curr = curr.next
            i += 1

        if curr == None: 
            return -1
        else: 
            return curr.data
            
    def insertHead(self, val: int) -> None:
        new = node(val)
        new.next = self.head
        self.head = new
        

    def insertTail(self, val: int) -> None:
        if self.head == None: 
            self.head = node(val)
            return 
        
        curr = self.head
        while curr.next != None: 
            curr = curr.next
        curr.next = node(val)

    def remove(self, index: int) -> bool:
        check = self.get(index)
        if check == -1: 
            return False

        if index == 0: 
            self.head = self.head.next
            return True

        prev = None
        curr = self.head
        i = 0
        while i < index: 
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next

        return True
        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head 
        while curr != None: 
            arr.append(curr.data)
            curr = curr.next
        return arr

        










        
