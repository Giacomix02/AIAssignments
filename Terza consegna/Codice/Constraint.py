from enum import Enum
from Variable import Variable
#
#
# class Constraint:
#     condition = None
#     variables:list[Variable] = []
#     def __init__(self, variables,  condition):
#         self.condition = condition
#         self.variables = variables
#
#     def getCondition(self):
#         return self.condition
#
#     def toString(self):
#         print(type(self.variables[0]))
#         return self.variables[0].getName() + " " + Condition[self.condition].value + " " + self.variables[1].getName() + " ==> " + str(self.variables[0].getValue()) + " " + Condition[self.condition].value + " " + str(self.variables[1].getValue())
#
#     def evaluate(self, variablesList:list[Variable]):
#         if self.variables[0].getName() != variablesList[0].getName() and self.variables[1].getName() != variablesList[1].getName():
#             return
#         first = str(variablesList[0].getValue())
#         second = str(variablesList[1].getValue())
#         if(self.condition =="eq1"):
#             second += 1
#
#         stringToValidate = first + Condition[self.condition].value + second
#         return eval(stringToValidate)
# class Condition(Enum):
#     eq = "=="
#     ht = ">"
#     ne = "!="
#     ne1 = "!="
#     he = ">="



def validate(variabile1:Variable, variabile2:Variable, segno):
    if(variabile1.getName()=="A" and variabile2.getName()=="D" and segno == "ht"):
            return variabile1.getValue()>variabile2.getValue()
    if(variabile1.getName()=="D" and variabile2.getName()=="E" and segno == "ht"):
            return variabile1.getValue()>variabile2.getValue()
    if(variabile1.getName()=="C" and variabile2.getName()=="A" and segno == "ne"):
            return variabile1.getValue()!=variabile2.getValue()
    if(variabile1.getName()=="C" and variabile2.getName()=="E" and segno == "ht"):
            return variabile1.getValue()>variabile2.getValue()
    if(variabile1.getName()=="C" and variabile2.getName()=="D" and segno == "ne"):
            return variabile1.getValue()!=variabile2.getValue()
    if(variabile1.getName()=="B" and variabile2.getName()=="A" and segno == "he"):
            return variabile1.getValue()>=variabile2.getValue()
    if(variabile1.getName()=="B" and variabile2.getName()=="C" and segno == "ne"):
            return variabile1.getValue()!=variabile2.getValue()
    if(variabile1.getName()=="C" and variabile2.getName()=="D" and segno == "ne1"):
            return variabile1.getValue()!=variabile2.getValue()+1
    return False

