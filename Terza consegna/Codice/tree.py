from Node import Node
from Variable import Variable
from Constraint import validate
from copy import deepcopy

def search(variabili:list[Variable]): # A:0 B:1 C:2 D:3 E:4
    stack = []
    solutions = []
    stack.append(copyVariabiliList(variabili)) # padre con dentro tutte le variabili
    while (len(stack)!=0):
        current:list[Variable] = stack.pop()
        n = 0
        while current[n].getValue() != None:
                n += 1
        n-=1
        
        current[n].nextValue()
        evaluations = [validate(variabili[0], variabili[3], "ht"), validate(variabili[3], variabili[4], "ht"), validate(variabili[2], variabili[0], "ne"), validate(variabili[2], variabili[4], "ht"), validate(variabili[2], variabili[3], "ne"), validate(variabili[1], variabili[0], "he"), validate(variabili[1], variabili[2], "ne"), validate(variabili[2], variabili[3], "ne1")]
        if not -1 in evaluations:
            if 0 in evaluations:
                result = "fail"
                
            else:
                solutions.append(current)
                result = "solution"
        else:
            result = "not evaluable"
        tab = ""
        for m in range(n):
            tab = tab + "\t"
        print(tab, "A=", current[0].getValue(), " B=", current[1].getValue(), " C=", current[2].getValue(), " D=", current[3].getValue(), " E=", current[4].getValue(), " result=", result)
        if result == "solution" or result == "fail":
            continue

        current[n].nextValue()
        stack.append(copyVariabiliList(current))

        current[n].nextValue()
        stack.append(copyVariabiliList(current))

        current[n].nextValue()
        stack.append(copyVariabiliList(current))

        current[n].nextValue()
        stack.append(copyVariabiliList(current))  

def copyVariabiliList(variabili:list[Variable]):
    newVariabili:list[Variable] = []
    for var in variabili:
        newVariabili.append(deepcopy(var))
    return newVariabili




