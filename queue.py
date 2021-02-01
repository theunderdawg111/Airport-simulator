# A linked list (LL) node 
# to store a queue entry 

from Main import generateFlightID
from random import randint, choices
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# A class to represent a queue 
# The queue, front stores the front node 
# of LL and rear stores the last node of LL 
class Queue: 
    
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
    
    def printQueue(self):
        temp = self.front;
        while temp.next != None:
            print (temp.data);
            temp = temp.next;
        print(temp.data)
    def getCount(self):
        temp = self.front;
        count = 0
        while temp.next != None:
            count+=1
            temp = temp.next;
        return count

    # Method to add an item to the queue 
    def enQueueFlight(self, item): 
        temp = Node(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def deQueueFlight(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        name = self.front.data
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
        return name
    def generateFlightID(len):
        characters = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N']
        return "".join(choices(characters , k=len))
    def refill(self):
        for _ in range(randint(0,10)):
            self.enQueueFlight(generateFlightID(6))
        return "Count: ",self.getCount()
    def init(self):
        for _ in range(randint(4,10)):
            self.enQueueFlight(generateFlightID(6))
        self.printQueue()
        
        
    