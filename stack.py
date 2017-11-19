#!/bin/python3.6

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("greeting ready to say bye...")
    bye()

def greet2(name):
    print("How are you, " + name + "?")

def bye():
    print("ok, bye!")

greet("Paul")
