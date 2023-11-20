# codice per la dfs
from collections import deque
import matplotlib.pyplot as plt
from graphPlot import Graph


def dfs(rettangoli, start, end, graph: Graph):
    stack = []
    stack.append(rettangoli[3][2])
    while (stack.__len__() != 0):  # finchè lo stack non è vuoto
        rect = stack.pop()  # estrae un elemento dallo stack
        rect.set_visitato(True)  # setta il rettangolo come visitato
        graph.colora(rect)
        if rect.is_tipo() == 2:  # se il rettangolo è quello di arrivo fermati
            break
        x = rect.coordinate()[0] - 1 # shift delle coordinate di 1 per permettere l'uso nella matrice
        y = rect.coordinate()[1] - 1

        if y != 0:  # se non sei al bordo inferiore
            next = rettangoli[x][y - 1]  # prendi il rettangolo in basso
            if not next.is_ostacolo() and not next.is_visitato():
                stack.append(next)
                next.set_individuato(True) # setta il rettangolo come individuato (è nella frangia)
                graph.colora(next)

        if x != 7:  # se non sei al bordo destro
            next = rettangoli[x + 1][y]  # prendi il rettangolo a destra
            if not next.is_ostacolo() and not next.is_visitato():
                stack.append(next)
                next.set_individuato(True) # setta il rettangolo come individuato (è nella frangia)
                graph.colora(next)

        if x != 0:  # se non sei al bordo sinistro
            next = rettangoli[x - 1][y]  # prendi il rettangolo a sinistra
            if not next.is_ostacolo() and not next.is_visitato():
                stack.append(next)
                next.set_individuato(True) # setta il rettangolo come individuato (è nella frangia)
                graph.colora(next)

        if y != 7:  # se non sei al bordo superiore
            next = rettangoli[x][y + 1]  # prendi il rettangolo in alto
            if not (next.is_ostacolo() or next.is_visitato()):
                stack.append(next)
                next.set_individuato(True) # setta il rettangolo come individuato (è nella frangia)
                graph.colora(next)

        plt.pause(0.5) # pausa per permettere la visualizzazione
