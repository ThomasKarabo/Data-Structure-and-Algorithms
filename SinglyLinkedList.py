class Node():
    def __init__(self):
        self.data = None
        self.next = None

    def getData(self):
        return self.data
    def setData(self,data):
        self.data = data

    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next
    def hasNext(self, next):
        return self.next != None


class LinkedList(Node):
    def listLength(self):
        current = self.head
        count = 0

        while current != None:
            count+=1
            current = current.getNext
        return count

    def insertHead(self,data):
        newNode = Node()
        newNode.setData(data)

        if self.listLength() == 0:
            self.head = newNode
        else:
            newNode = setNext(self, next)
            self.head = newNode

        self.count +=1


    def insertMid(self, data, pos):
        if pos > self.count or pos < 0:
            return None
        else:
            if pos ==  0:
                self.insertHead(data)
            else:
                if pos == self.count:
                    self.insertTail(data)
                else:
                    newNode = Node()
                    new.setData(data)
                    count = 0
                    current = self.head

                    while count < pos-1:
                        count+=1
                        current = current.getNext()
                    newNode.setNext(current.getNext)
                    current.setNext(newNode)
                    count+=1

    def insertTail(self,data):
        newNode = Node()
        newNode.setData(data)

        current = self.head

        while current.getNext() != None:
            current = current.getNext()
        current.setNext(newNode)
        self.count=+1

    def deleteHead(self):
        if self.count == 0:
            raise ValueError("The list is Empty!!")
        else:
            self.head = self.head.getNext()
            self.count -=1

    def deleteMid(self, node):
        if self.count == 0:
            raise ValueError("The list is Empty!!")
        else:
            pass


    def deleteTail(self):
        if self.count == 0:
            raise ValueError("The list is Empty!!")
        else:
            current = self.head
            previous = self.head
            while current.getNext() != None:
                previous = current
                current = current.getNext()

            previous.setNext(None)
            self.count -=1


node1 = Node()
node1.data = 10
node2 = Node()
node2.data = 20
node3 = Node()
node3.data = 30

print(node1.data)