class Node:
    previous = None
    next = []           # da sinistra a destra
    value = []
    def __init__(self, value, previuos, next):
        self.value = value
        self.previous = previuos
        self.next = next

    def addNext(self, next):
        self.next.append(next)

    def setNext(self, next):
        self.next = next
    def getPrevious(self):
        return self.previous
    def getNext(self):
        return self.next
    def getValues(self):
        return self.value
    def getValue(self, index):
        return self.value[index]
    def getNextByIndex(self, index):
        if(index > len(self.next)): return -1
        else : return self.next[index]
