class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:

    def __init__(self):
        self.head=None

    #insering node at the end of LL (LL : Linked List)
    def append(self,new_data):
         #first make a new node (data,next)
         new_node = Node(new_data)

         #check if LL is empty
         #if yes, then make new node as head
         if self.head is None:
             self.head = new_node
             return

         #itirate through the list to find the last node
         #the last node is the onw that has nect pointer to none
         last = self.head
         while(last.next):
             last = last.next

             

         #  now "last" is pointing to last node
         last.next = new_node


#append
ll=LinkedList()
ll.append(3)
ll.append(4)
ll.append(5)

#display
x=ll.head

while(x):
    print(x.data)
    x=x.next
        
        
