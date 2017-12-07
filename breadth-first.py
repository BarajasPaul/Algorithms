#!/bin/python3.6
"""breadth-first search"""

from collections import deque

GRAPH = {"you": ["bob", "claire", "alice"],
         "bob":  ["anuj", "peggy"],
         "claire": ["thom", "jonny"],
         "alice": ["peggy"],
         "anuj": [], "thom": [],
         "jonny": [], "peggy": []}

def person_is_seller(name):
    """get seller"""
    return name[-1] == "m"

def search(name):
    """search for the seller person"""
    search_queue = deque()
    search_queue += GRAPH[name]
    searched = []
    while search_queue:
        print(search_queue)
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
            else:
                search_queue += GRAPH[person]
                searched.append(person)
    return True

print(search("you"))
