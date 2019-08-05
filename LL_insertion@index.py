class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        # size will hold the length of the libked list
        self.size=0


    #inseting a node at particular index n (n=0,1,2,,,)
    def insert_at(self,value,n):
        length = n
        new_node=Node(value)
        loc = self.head
        #if n = 0, then insertion is at the very beginning
        if n == 0:
            #print("n=0")
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return


        
        while(length-1):
            #print("for",n)
            try:
                loc=loc.next
            except:
                print("list is not "+str(n)+" size long. It is only "+str(self.size)+" in length")
                return
            length-=1

        # if loc.next is None then loc is pointing to a node which is last and
        #user wants to add a node after it
        #this is basically a case of insertion at end (LL_insertion@end.py)

        if loc.next is None:
            loc.next=new_node
            self.size += 1
            return
        
        #loc points to the node that is to be replaced and new_node is inserted
        #in its location. this node which is pointed by loc is shfted to one location right
        new_node.next = loc.next
        loc.next = new_node
        self.size += 1
                
            
            
ll=LinkedList()       
ll.insert_at(6,0)
ll.insert_at(3,0)
ll.insert_at(5,1)
ll.insert_at(7,2)
ll.insert_at(2,2)
ll.insert_at(10,3)
ll.insert_at(8,9)


x=ll.head

while(x):
    print(x.data)
    x=x.next
