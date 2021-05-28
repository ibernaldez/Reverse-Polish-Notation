"""
Reverse Polish Notation
http://www-stone.ch.cam.ac.uk/documentation/rrf/rpn.html
Full Stack
"""

def input2():
    new_stack = []
    RPN_input = input("Enter RPN Stack: ")
    for i in RPN_input:
        try:
            i = int(i)
            new_stack.append(i)
        except ValueError:
            new_stack.append(i)
    return new_stack

def helper_function(stack, item, first, second, x):
    stack.remove(item)
    stack.remove(first)
    stack.remove(second)
    stack.insert(0, x)
    return stack

def main():

    stack = input2()

    for i in range(len(stack)):
        for item in stack:
            if item == "+":
                x = stack[0] + stack[1]
                helper_function(stack, item, stack[0], stack[1], x)
                print(stack)
            if item == "/":
                x = stack[0] / stack[1]
                helper_function(stack, item, stack[0], stack[1], x)
                print(stack)
            if item == "-":
                x = stack[0] - stack[1]
                helper_function(stack, item, stack[0], stack[1], x)
                print(stack)
            if item == "*":
                x = stack[0] * stack[1]
                helper_function(stack, item, stack[0], stack[1], x)
                print(stack)
main()
