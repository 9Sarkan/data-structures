class Node:
    def __init__(self, Data):
        self.data = Data
        self.next = None

    @property
    def Data(self):
        return self.data

    @property
    def Next(self):
        return self.next

    @property
    def Data(self, data):
        self.data = data

    @property
    def Next(self, neext):
        self.next = neext


class UnorderedList:
    def __init__(self):
        self.head = None

    @property
    def isEmpty(self):
        return None == self.head

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    @property
    def size(self):
        current = self.head
        count = 0
        while None != current:
            count = count + 1
            current = current.next
        return count
    
    def search(self, data):
        current = self.head
        found = False
        while None != current.next:
                if current.data == data:
                    found = True
                    break
                else:
                    current = current.next
        else:
            if current.data == data:
                found = True
        return found

    def remove(self, data):
        if not self.search(data):
            return -1
        else:
            current = self.head
            prev = None
            while True:
                if current.data == data:
                    break
                else:
                    prev = current
                    current = current.next
    
            if None == prev:
                self.head = current.next
            else:
                prev.next = current.next

    def show_list(self):
        current = self.head
        lst = []
        while None != current:
            lst.append(current.data)
            current = current.next
        return lst
