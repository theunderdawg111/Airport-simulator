import queues2.py
import random
obj1 = queues2()

def land(landing):
    print("Flight ID ",landing.dequeue ,"is landing")

def takeoff(takingOff):
    print("Flight ID ",takingOff.dequeue,"is taking off")
    
def random_():
    num=random.randint(1, 10)
    return num

def generateFlightID(s,len):
    alpha=('A','B','C','D','E','F','G','H','I','J','K','L','M','N')
    num_=(1,2,3,4,5,6,7,8,9,0)
    k=0
    for i in range(0,len/2):
        s[k]=random.choice(alpha)
        k=k+1
    for i in range(0,len/2):
        s[k]=random.choice(num_)
        k=k+1
    s[len]=0

def refill(queue):
    generateFlightID(s, 5) 
    print('Refilling \n')
    for i in range(random_() % 50):
        enqueue(s,queue)
        generateFlightID(s, 5)
    printList(queue)

def refillU(queue):
    generateFlightID(s, 5) 
    print('Refilling \n')
    for i in range(random_() % 5):
        enqueue(s,queue)
        generateFlightID(s, 5)
    printList(queue)
    
#--------------------------------------------------------------------   


if __name__=='__main__':
    counterTakeoff=0
    counterLanding=0
    interval=1
    takeoffQueue= queues2.flight()
    landingQueue=queues2.flight()
    
    print("This is an Airport Simulator. It uses 2 Queues implemented in Linked List. \n")
    print("It demonstrates how a system can effectively control air traffic.\n")
    print("In this implementation we assume that there is one runway on a heavy traffic airport.\nThe goal is to see how queues can help to organise the incoming and outgoing flights")
    print("\n \n \n")
    c=0
    c=int(input("Press 1 to start \n"))
    while(c==1 or c==2):
        if(c==1):
            if(queues2.getCount(takeoffQueue)<=2):
                print("Warning: Refilling Take Off due to low flight count \n")
                refillU(takeoffQueue)
            if(queues2.getCount(landingQueue)<=2):
                print("Warning: Refilling Landing  due to low flight count \n")
                refillU(landingQueue)
            print("Time Interval is %d\n", interval)
            scoreLanding = float(0.45 * queues2.getCount(landingQueue))
            scoreTakeoff = float(0.55 * queues2.getCount(takeoffQueue))
            selection=0
            
            if(scoreLanding<scoreTakeoff):
                selection=1
            if selection==1:
                print("Flight Taking Off: ", queues2.dequeue(takeoffQueue.next))
                queues2.printList(takeoffQueue)
                counterTakeoff=counterTakeoff+1
            else:
                print("Flight Landing: ", queues2.dequeue(landingQueue.next))
                queues2.printList(landingQueue)
                counterLanding=counterLanding+1
            c=int(input("Press 1 to continue...\n Press 2 to refill...\n"))
            interval=interval+1;
            print("\n \n ")
        elif (c==2):
            refillU(takeoffQueue)
            refillU(landingQueue)
            c=int(input("Press 1 to continue...\n"))
        else:
            break
    
    
    
    
    
    
    