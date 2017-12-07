#!/bin/python3.6
"""Dijkstra's algorithm"""

GRAPH = {"start": {"a": 6, "b": 2},
         "a": {"fin": 1},
         "b": {"a": 3, "fin": 5},
         "fin": {}}

COSTS = {"a": 6, "b": 2, "fin": float("inf")}

PARENTS = {"a": "start", "b": "start", "fin": None}

processed = []

def find_lowest_cost_node(cost):
    "Get lowest cost node"
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in COSTS:
        cost = COSTS[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    print(lowest_cost)
    return lowest_cost_node

NODE = find_lowest_cost_node(COSTS)
print(NODE)
while NODE is not None:
    cost = COSTS[NODE]
    neighbors = GRAPH[NODE]
    for neighbor in neighbors.keys():
        new_cost = cost + neighbors[neighbor]
        if COSTS[neighbor] > new_cost:
            COSTS[neighbor] = new_cost
            PARENTS[neighbor] = NODE
    processed.append(NODE)
    NODE = find_lowest_cost_node(COSTS)

print(COSTS)
