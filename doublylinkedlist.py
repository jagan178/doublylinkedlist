class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self,head,temp):
        self.head=None
        self.temp=None
    def create(self):
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            data = int(input("\nEnter the list elements:"))
            newnode = Node(data)
            newnode.prev=None
            newnode.next=None
            if self.head == None:
                self.head = newnode
                self.temp = newnode
            else:
                self.temp.next=newnode
                newnode.prev=self.temp
                self.temp=self.temp.next
    def display(self):
        self.temp = self.head
        print("Display the elements int the list:")
        while self.temp != None:
            print(self.temp.data, end = ' ')
            self.temp = self.temp.next
    def insertatfront(self):
        self.temp = self.head
        newnode = Node(int(input("\nenter the element to insert at front: ")))
        newnode.next = self.head
        newnode.prev=None
        self.head.prev = newnode
        self.head=newnode
    def insertatend(self):
        self.temp = self.head
        newnode = Node(int(input("\nenter the element: ")))
        while self.temp.next != None:
            self.temp = self.temp.next
            self.temp.next = newnode
            newnode.prev = self.temp
            newnode.next = None
    def insertatmiddle(self):
        newnode = Node(int(input("\nenter the element to insert at middle: ")))
        pos = int(input("\nEnter the position:"))
        i = 1
        self.temp=self.head
        while i < pos:
            self.temp = self.temp.next
            i = i + 1
        newnode.next = self.temp.next
        newnode.prev=self.temp
        self.temp.next = newnode
        newnode.next.prev = newnode
    def deleteatfront(self):
        self.temp = self.head
        self.head = self.head.next
        self.head.prev=None
        del self.temp
    def deleteatend(self):
        self.temp = self.head
        nextnode = None
        while self.temp.next != None:
            nextnode = self.temp
            self.temp = self.temp.next
        nextnode.next = None
        self.temp.prev=None
        del self.temp
    def deleteatmiddle(self):
        self.temp = self.head
        pos = int(input("\nEnter the position:"))
        i = 1
        while i < pos:
            self.temp = self.temp.next
            i = i + 1
        self.temp.prev.next = self.temp.next
        self.temp.next.prev = self.temp.prev
        self.temp.next = self.temp.prev = None
        del self.temp
    def count(self):
        self.temp = self.head
        count = 0
        while self.temp != None:
            count += 1
            self.temp = self.temp.next
        print(count)
    def search(self):
        item = int(input("Enter an element to search:"))
        self.temp = self.head
        while self.temp:
            if self.temp.data == item:
                print(f"{item} is there")
                return
            self.temp = self.temp.next
        print(f"{item} is not there")
obj=Linkedlist(None,None)
obj.create()
obj.insertatfront()
obj.insertatend()
obj.insertatmiddle()
obj.deleteatfront()
obj.deleteatend()
obj.deleteatmiddle()
obj.display()

        
