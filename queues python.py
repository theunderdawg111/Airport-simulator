class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
          self.head=Node(data)
          self.last=self.head
        else:
          self.last.next=Node(data)
          self.last.next.prev=self.last
          self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp=self.head.data
            self.head=self.head.next
            self.head.prev=None
            return temp
    def first(self):
        return self.head.data
    def size(self):
        temp=self.head
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        return count
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def printqueue(self):
        print("queue elements are: ")
        temp=self.head
        while temp is not None:
            print(temp.data,end='->')
            temp=temp.next

if __name__=='__main__':
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.printqueue()
    print("\n First element is ",queue.first())
    print("\n Size of queue is ",queue.size())
    queue.dequeue()
    queue.dequeue()
    print("After applying dequeue() two times")
    queue.printqueue()
    print("\nqueue is empty:",queue.isEmpty())
    