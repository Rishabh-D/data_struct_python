class Node:
    def __init__(self,next=None,prev=None,data=None):
        self.next=next
        self.prev=prev
        self.data=data

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(data=new_data)
        new_node.next=self.head
        new_node.prev=None
        self.head= new_node


ll=DoublyLinkedList()
ll.push(3)
ll.push(7)
ll.push(8)

x=ll.head

while(x):
    print(x.data)
    x=x.next

        

