from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
         if self.capacity > 0:
            self.storage.add_to_tail(item) 
            self.capacity -= 1 
            self.count = 0

         else:
            if self.capacity == 0 and self.count == 0:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.count += 1
            elif self.count == 1:
                self.storage.head.insert_after(item)
                self.storage.head.next.next.delete()
                self.count +=1
            elif self.count == 2:
                self.storage.head.next.insert_after(item)
                self.storage.head.next.next.next.delete()
                self.count +=1
            elif self.count == 3:
                self.storage.head.next.next.insert_after(item)
                self.storage.head.next.next.next.next.delete()
                self.count +=1
            elif self.count == 4:
                self.storage.head.next.next.next.insert_after(item)
                self.storage.head.next.next.next.next.next.delete()
                self.count = 0

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        
        node = self.storage.head
        if type(node.value) is int:
             list_buffer_contents.append(int(node.value))

        else:
            list_buffer_contents.append(str(node.value))

        while node.next != None:
          node = node.next
          if type(node.value) is int:
               list_buffer_contents.append(int(node.value))
          else:  
               list_buffer_contents.append(str(node.value))


        return list_buffer_contents
         
Ring = RingBuffer(5)
for i in range(50):
    Ring.append(i)
print(Ring.get())      

print(Ring.get())     

print(Ring.get())    
# Ring.append('h')
# Ring.append('i')
# Ring.append('l')
# Ring.append('a')
# Ring.append('b')
print("length: ", Ring.storage.length)


# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
