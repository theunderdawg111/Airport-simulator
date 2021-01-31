class flight:
    def __init__(self,ID):
        self.ID=ID
        self.next=None
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False
        
    def enqueue(self,ID):
        temp=flight(ID)
        
        if self.rear is None:
          self.front=self.rear=temp
          return None
       
        self.rear.next=temp
        self.rear=self.rear.next
    
    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.front.ID
        self.front=self.front.next
        return temp
    
    def getCount(self):
        count=1
        temp=flight.next
        while(temp.next is not None):
            count=count+1
            temp=temp.next
        return count
    
    def printList(self):
        print("------------------------\n")
        printval = self.front
        while printval is not None:
            
            print ("Plane ID ", printval.dataval)
            printval = printval.next.front
        print ("Plane ID ", printval.dataval)
        print("------------------------\n")
    
        