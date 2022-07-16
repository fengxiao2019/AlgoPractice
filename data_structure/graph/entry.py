from __future__ import annotations
from dataclasses import dataclass
from typing import List
import sys



@dataclass
class Entry(object):
    adj: List[int]
    known: bool
    dist: int
    path: Entry


class Graph(object):
    def __init__(self, v_count, start):
        self.v_count = v_count
        self.nodes = [Entry()] * self.v_count
        self.start = start
        self.dist_dict = dict()

        for i in range(v_count):
            self.nodes[i].known = False
            self.nodes[i].dist = sys.maxsize - 1
            self.nodes[i].path = None
        self.nodes[start].dist = 0

    def addEdge(self, v, w, cvw):
        self.nodes[v].adj.append(w)
        self.dist_dict[(v, w)] = cvw

    def _find_smallest_unkown(self):
        min_distance = sys.maxsize - 1
        node_i = None
        for i in range(self.v_count):
            if not self.nodes[i].known:
                if self.nodes[i].dist < min_distance:
                    min_distance = self.nodes[i].dist
                    node_i = i
        return node_i

    def shortest_path(self):
        while True:
            node_i = self._find_smallest_unkown()
            if not node_i:
                break
            self.nodes[node_i].known = True
            for item in self.nodes[node_i].adj:
                new_dist = self.nodes[node_i].dist + self.dist_dict[(node_i, item)]
                if new_dist < self.nodes[item].dist:
                    self.nodes[item].dist = new_dist
                    self.nodes[item].path = node_i

    def print_path(self, node_i: int):
        next_path = self.nodes[node_i].path
        if next_path is not None:
            self.print_path(next_path)
            print(" to")
        print("%d", node_i)


def init_graph():
    g = Graph(7, 0)
    g.addEdge(0, 1, 1)
    g.addEdge(0, 3, 1)
    g.addEdge(1, 4, 1)
    g.addEdge(1, 3, 1)
    g.addEdge(2, 0, 1)
    g.addEdge(2, 5, 1)
    g.addEdge(3, 2, 1)
    g.addEdge(3, 4, 1)
    g.addEdge(3, 6, 1)
    g.addEdge(3, 5, 1)
    g.addEdge(4, 6, 1)
    g.addEdge(6, 5, 1)
    g.shortest_path()
    g.print_path(3)

init_graph()