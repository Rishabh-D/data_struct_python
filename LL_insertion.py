class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    #inserting element at the start of LL

    def push(self,new_data):
        #first make a new node (data,next)
        new_node = Node(new_data)
        

        #since we are inserting this node at very begining, we will make (next) part of
        #new_node point to node where head was pointing
        new_node.next = self.head

        #now head must point to this new_node
        self.head=new_node
        #print(self.head)


ll=LinkedList()
ll.push(3)
ll.push(7)
ll.push(8)

x=ll.head

while(x):
    print(x.data)
    x=x.next
