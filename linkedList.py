class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def setNext(self, newnext):
        self.next = newnext

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

class UnorderedList:

    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())