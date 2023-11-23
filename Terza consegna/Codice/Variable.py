import random


class Variable:
    name = None
    domain = []


    def __init__(self, name, domain:list):
        self.name = name
        self.domain = domain
        self.value = None
        self.n = 0
    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def nextValue(self):
        if self.n == -1:
            self.n = 3
        if self.value == None:
            self.value = self.domain[self.n]
            self.n -= 1
        else: 
            self.value = self.domain[self.n]
            self.n = self.n - 1
    