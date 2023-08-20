#!/usr/bin/env python3

def greet_programmer():
    print(f"Hello, programmer!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default("Sunny")

def add(num1, num2):
    sum = (num1 + num2)
    print(sum)
    return sum
add(1,2)

def halve(number):
    half= number / 2
    return half

halve(4)
