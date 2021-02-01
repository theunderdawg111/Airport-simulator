from queue import Queue
takeOffQueue = Queue()
landingQueue = Queue()
from random import random

print("This is an Airport Simulator. It uses 2 Queues implemented in Linked List. \n")
landCounter = 0
takeoffCounter = 0
print("Landing")
landingQueue.init()
print("Take Off")
takeOffQueue.init()

while True:
    
    if landingQueue.getCount()<=2:
        landingQueue.refill()
    if takeOffQueue.getCount()<=2:
        takeOffQueue.refill()
    
    if random() < 0.5:
        #Land
        print("Flight Landing: ", landingQueue.deQueueFlight())
        landingQueue.printQueue()
        landCounter +=1
        
    else:
        #Take Off
        print("Flight Taking Off: ", takeOffQueue.deQueueFlight())
        takeOffQueue.printQueue()
        takeoffCounter +=1
    c=input("Continue? \n")
    if c == 2:
        break
