# agentTop.py - Top Layer
# AIFCA Python3 code Version 0.9.3 Documentation at http://aipython.org
# Download the zip file and read aipython.pdf for documentation
import random
import time

import matplotlib

from agentMiddle import Rob_middle_layer
from agents import Environment


# Artificial Intelligence: Foundations of Computational Agents http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2021.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en


class Rob_top_layer(Environment):
    def __init__(self, middle, timeout=200, locations={'mail': (-5, 10),
                                                       'o103': (50, 10), 'o109': (100, 10), 'storage': (101, 51)}):
        """middle is the middle layer
        timeout is the number of steps the middle layer goes before giving up
        locations is a loc:pos dictionary 
            where loc is a named location, and pos is an (x,y) position.
        """
        self.middle = middle
        self.timeout = timeout  # number of steps before the middle layer should give up
        self.locations = locations

    def do(self, plan):
        """carry out actions.
        actions is of the form {'visit':list_of_locations}
        It visits the locations in turn.
        """

        # Opportunistic planner
        to_do = plan['visit']
        if to_do.__len__() == 0:
            return

        while len(to_do) != 0:
            # decide la prossima posizione più vicina
            next = self.min_distance(to_do)
            print("******** PUNTO SUCCESSIVO:", next)
            position = self.locations[next]

            # va alla posizione
            arrived = self.middle.do({'go_to': position, 'timeout': self.timeout})
            self.display(1, "Arrived at", next, arrived)

            # elimina dalla lista la posizione visitata
            to_do.remove(next)
            print("******** RIMANENTI:", to_do)

    def min_distance(self, location_list):  # calcola la distanza tra la posizione attuale e la posizione successiva
        """return the nearest location in location_list
        """
        location = ''
        distance = None
        for loc in location_list:
            target = self.locations[loc]
            temp_distance: int = self.distance(target)
            if distance is None or temp_distance < distance:
                distance = temp_distance
                location = loc
        return location

    def distance(self, target):
        """ return the distance to target
        """
        target_x, target_y = target
        agent_x, agent_y = self.middle.percepts['rob_x_pos'], self.middle.percepts['rob_y_pos']
        return (target_x - agent_x) ** 2 + (target_y - agent_y) ** 2


import matplotlib.pyplot as plt


class Plot_env(object):
    def __init__(self, body, top):
        """sets up the plot
        """
        self.body = body
        plt.ion()
        plt.clf()
        plt.axes().set_aspect('equal')
        for wall in body.env.walls:  # create the walls
            ((x0, y0), (x1, y1)) = wall
            plt.plot([x0, x1], [y0, y1], "-k", linewidth=3)
        for loc in top.locations:  # create the locations
            (x, y) = top.locations[loc]
            plt.plot([x], [y], "k<")
            plt.text(x + 1.0, y + 0.5, loc)  # print the label above and to the right
        plt.plot([body.rob_x], [body.rob_y], "go")
        plt.draw()

    def plot_run(self):
        """plots the history after the agent has finished.
        This is typically only used if body.plotting==False
        """
        xs, ys = zip(*self.body.history)
        plt.plot(xs, ys, "go")

        print("***** wall history: ", self.body.wall_history)
        if len(self.body.wall_history) != 0:        # if the robot crashed
            wxs, wys = zip(*self.body.wall_history)
            plt.plot(wxs, wys, "ro")
        plt.draw()


from agentEnv import Rob_body, Rob_env

OBSTACLES = 2


def make_obstacles(n):
    """make n obstacles
    """
    obstacles = set()
    for i in range(n):
        x = random.randint(1, 90)
        y = random.randint(1, 45)
        x1 = random.randint(1, 90)
        y1 = random.randint(1, 45)
        obstacle = ((x, y), (x1, y1))
        obstacles.add(obstacle)
    print(obstacles)
    return obstacles


# env = Rob_env(
#   {
#       ((20,0),(30,20)), ((70,-5),(70,25))
#       }
# )
env = Rob_env(make_obstacles(OBSTACLES))
body = Rob_body(env)
middle = Rob_middle_layer(body)
top = Rob_top_layer(middle)

# try:
pl = Plot_env(body, top)
top.do({'visit': ['o109', 'storage', 'o103','mail']})
pl.plot_run()
# You can directly control the middle layer:
#middle.do({'go_to': (30, -10), 'timeout': 200})

# do the following to see the history of the robot:
plt.show()
plt.pause(10000)
