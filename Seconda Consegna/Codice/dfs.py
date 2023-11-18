# codice per la dfs
from collections import deque
import matplotlib.pyplot as plt
from graphPlot import Graph


def dfs(rettangoli, start, end):
    stack = deque()
    stack.append(rettangoli[3][2])
    while (stack.__len__() != 0):  # finchè lo stack non è vuoto
        rect = stack.popleft()  # estrae un elemento dallo stack
        rect.set_visitato(True)  # setta il rettangolo come visitato
        Graph().colora(rect)
        if rect._tipo == 2:  # se il rettangolo è quello di arrivo fermati
            break
        x = rect.coordinate()[0] - 1
        y = rect.coordinate()[1] - 1

        if y != 0:  # se non sei al bordo inferiore
            next = rettangoli[x][y - 1]  # prendi il rettangolo in basso
            if not next._ostacolo and not next._visitato:
                stack.appendleft(next)

        if x != 7:  # se non sei al bordo destro
            next = rettangoli[x + 1][y]  # prendi il rettangolo a destra
            if not next._ostacolo and not next._visitato:
                stack.appendleft(next)

        if x != 0:  # se non sei al bordo sinistro
            next = rettangoli[x - 1][y]  # prendi il rettangolo a sinistra
            if not next._ostacolo and not next._visitato:
                stack.appendleft(next)

        if y != 7:  # se non sei al bordo superiore
            next = rettangoli[x][y + 1]  # prendi il rettangolo in alto
            if not (next._ostacolo or next._visitato):
                stack.appendleft(next)

        plt.pause(0.5)
