class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node
            return

    def reverse(self):
        prev=None
        current = self.head
        temp=None

        while(current):
            #print(current.data)
            temp=current.next
            current.next=prev
            prev=current
            current=temp

        self.head = prev    

ll= LinkedList()
ll.push(3)
ll.push(5)
ll.push(8)

x=ll.head
while(x):
    print(x.data)
    x=x.next
        
ll.reverse() #reverse the list

#print the reversed list
x=ll.head
while(x):
    print(x.data)
    x=x.next
    
    
