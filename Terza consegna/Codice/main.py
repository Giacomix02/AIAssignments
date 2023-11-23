from matplotlib import pyplot as plt

from constraintGraph import Variable, Constraint, renderGraph
from dfs import runDfs
from cspConsistency import Con_solver
import copy

domain = [1,2,3,4]
variables = [Variable("A", domain, position=(0.35, 0.03)), Variable("B", domain, position=(0.02,0.3)), Variable("C", domain, position=(0.5, 0.93)), Variable("D", domain, position=(0.65,0.09)), Variable("E", domain, position=(1, 0.1))]
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
   csp = renderGraph(variables, constraint)      # render del constraint graph
   if (USE_DFS):
      runDfs(csp)
   if (USE_AC_WITH_DOMAIN_SPLITTING):
      solver = Con_solver(csp)
      print("\n\n********** ARC CONSISTENCY ( domanda 3 ) **********\n")
      solver.make_arc_consistent()

      nuoveVariabili = copy.deepcopy(variables)
      variablesConsistent:set = csp.variables
      n=0
      for v in variablesConsistent.keys():
         nuoveVariabili[n].domain = variablesConsistent.get(v)
         n+=1
      renderGraph(nuoveVariabili, constraint)


      print("\n\n**********  HOW SPLITTING A DOMAIN CAN BE USED TO SOLVE THIS PROBLEM ( domanda 4 ) **********\n")
      print(solver.solve_one())
