from Node import Node
from Variable import Variable
from Constraint import validate
from tree import search
import constraintGraph as renderGraph


variabiliString = ["A","B","C","D","E"]
domain = [1,2,3,4]

variabili: list[Variable] = []

if __name__ == "__main__":
    for var in variabiliString:
         variabili.append(Variable(var,domain))

    search(variabili)
    renderGraph()