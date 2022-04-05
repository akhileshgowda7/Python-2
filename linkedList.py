class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None
    def get_length(self):
        count = 0
        itr = self.head
        while(itr):
            count+=1
            itr=itr.next
        return count

    def insert_beginning(self, data):

        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

    def insert_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        itr = self.head
        while(itr.next):
            itr = itr.next

        itr.next = Node(data,None)


        itr = self.head
        llstr = ''

        while (itr):
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)

    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while(itr):
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1




if __name__ == '__main__':
    l1 = linked_list()
    l1.insert_beginning(6)
    l1.insert_beginning(5)
    l1.insert_beginning(8)
    l1.insert_beginning(9)
    l1.remove_at(1)

    l1.insert_end(34)
    l1.print()
