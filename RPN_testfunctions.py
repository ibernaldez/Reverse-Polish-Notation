import sys
import re
import fileinput

new_stack = []
new_stack2 = []

print("Welcome to RPN")
print("To Signal the end of stack input, type 'Calc'")

def func():
    stacky = []
    for line in sys.stdin:
        new_stack.append(line.strip())
        print(new_stack)
        if 'Calc' == line.rstrip():
            new_stack.remove("Calc")
            print(new_stack)
            if len(new_stack) > 1:
                s = ""
                s = s.join(new_stack)
                new_stack2.append(s)
                print(new_stack2)
                return new_stack2
            return new_stack
    return new_stack

def helper_function(stack, item, first, second, operator):
    stack.remove(item)
    stack.remove(first)
    stack.remove(second)
    stack.insert(0, operator)
    return stack

def main():
    stack = []
    new_stacker = []
    stack = func()
    if len(stack[0]):
        blank = True
    if blank == True:
        for i in range(len(stack)):
            sub_stack = stack[i]
            for i in sub_stack:
                try:
                    i = int(i)
                    new_stacker.append(i)
                except ValueError:
                    new_stacker.append(i)
            new_stacker = math(new_stacker)
            new_stacker.clear()
    else:
        for i in stack[0]:
            try:
                i = int(i)
                new_stacker.append(i)
            except ValueError:
                new_stacker.append(i)
        new_stacker = math(new_stacker)

def math(new_stacker):
    for i in range(len(new_stacker)):
        for item in new_stacker:
            if item == "+":
                x = new_stacker[0] + new_stacker[1]
                helper_function(new_stacker, item, new_stacker[0], new_stacker[1], x)
            if item == "/":
                x = new_stacker[0] / new_stacker[1]
                helper_function(new_stacker, item, new_stacker[0], new_stacker[1], x)
            if item == "-":
                x = new_stacker[0] - new_stacker[1]
                helper_function(new_stacker, item, new_stacker[0], new_stacker[1], x)
            if item == "*":
                x = new_stacker[0] * new_stacker[1]
                helper_function(new_stacker, item, new_stacker[0], new_stacker[1], x)
    print(new_stacker)
    return new_stacker

main()
