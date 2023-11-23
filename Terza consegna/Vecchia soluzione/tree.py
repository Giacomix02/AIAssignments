from Node import Node
from Variable import Variable
from Constraint import validate

stack = []
def search(variabili:list[Variable]):
    # creo il nodo padre
    root = Node(variabili, None, [])    # padre con dentro tutte le variabili
    stack.append(root)

