from constraintGraph import Variable, Constraint, renderGraph
from dfs import runDfs

domain = [1,2,3,4]
variables = [Variable("A", domain), Variable("B", domain), Variable("C", domain), Variable("D", domain), Variable("E", domain)]
constraint = []
constraint.append(Constraint([variables[0], variables[3]], lambda x, y: x > y, "A>D"))
constraint.append(Constraint([variables[3], variables[4]], lambda x, y: x > y, "D>E"))
constraint.append(Constraint([variables[2], variables[0]], lambda x, y: x != y, "C!=A"))
constraint.append(Constraint([variables[2], variables[4]], lambda x, y: x > y, "C>E"))
constraint.append(Constraint([variables[2], variables[3]], lambda x, y: x != y, "C!=D"))
constraint.append(Constraint([variables[1], variables[0]], lambda x, y: x >= y, "B>=A"))
constraint.append(Constraint([variables[1], variables[2]], lambda x, y: x != y, "B!=C"))
constraint.append(Constraint([variables[2], variables[3]], lambda x, y: x != y + 1, "C!=D+1"))


if __name__=="__main__":
   csp =  renderGraph(variables, constraint)      # render del constaint graph
   runDfs(csp)