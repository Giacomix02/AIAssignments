import random


class Variable:
    name = None
    domain = None
    value = None
    n = 0

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.value = domain[self.n]
        self.n = self.n + 1

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def nextValue(self):
        self.value = self.domain[self.n]
        self.n = self.n + 1