import sys
import re

print("Welcome to RPN")
print("To Signal the end of stack input, type 'Calc'")

def stack_input():
    stdin_stack = []
    manual_stdin_stack = []
    for line in sys.stdin:
        stdin_stack.append(line.strip())
        print(stdin_stack)
        if 'Calc' == line.rstrip():
            stdin_stack.remove("Calc")
            print(stdin_stack)
            if len(stdin_stack) > 1:
                s = ""
                s = s.join(stdin_stack)
                manual_stdin_stack.append(s)
                print(manual_stdin_stack)
                return manual_stdin_stack
            return stdin_stack
    return stdin_stack

def helper_function(stack, item, first, second, operator):
    stack.remove(item)
    stack.remove(first)
    stack.remove(second)
    stack.insert(0, operator)

def main():
    stack = []
    new_stack = []
    stack = stack_input()
    for scalar in range(len(stack)):
        sub_stack = stack[scalar]
        for scalar in sub_stack:
            try:
                scalar = int(scalar)
                new_stack.append(scalar)
            except ValueError:
                new_stack.append(scalar)
        new_stack = process_instructions(new_stack)
        new_stack.clear()

def process_instructions(new_stacker):
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
