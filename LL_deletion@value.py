class Node:
    
    def __init__(self,data):

        self.data=data
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None

    #first we make a function that inserts value to start of the list
    def push (self,new_data):
        #we make a instance of node
        new_node = Node(new_data)

        #we make this new_node point to node where head is pointing
        new_node.next = self.head

        #now make head point to new_node
        self.head = new_node

    def delete_value(self,value):
        #if Linked list is empty, print "list empty"
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            #check if first node itself contains the value
            look = self.head
            #print(look.data)
            if look.data == value:
                print("first node contains the value")
                next_ = look.next
                self.head = next_
                return

            else:
                while(look.next is not None):
                    
                    
                    
                    if look.data == value:
                        break

                    prev = look 
                    look=look.next
                print("captured the node.. now deleting")
                prev.next = look.next
                look.next = None
                return
                    
                    
                        

                    
                

ll=LinkedList()
ll.push(3)
ll.push(7)
ll.push(8)

x=ll.head

while(x):
    print(x.data)
    x=x.next

ll.delete_value(3)
ll.delete_value(7)
ll.delete_value(8)

x=ll.head

while(x):
    print(x.data)
    x=x.next            
                    
                
        
        
        
        

        
        
