"""
Reverse Polish Notation
http://www-stone.ch.cam.ac.uk/documentation/rrf/rpn.html
One item pushed to stack at a time
"""

operations = ["+", "-", "/", "*"]

def input1(stack):
    player_user_input = input("Enter Number or Operation: ")
    if player_user_input in operations:
        stack.append(player_user_input)
    else:
        y = int(player_user_input)
        stack.insert(0, y)
    print(stack)
    return stack

def helper_function(stack, item, first, second, x):
    stack.remove(item)
    stack.remove(first)
    stack.remove(second)
    stack.insert(0, x)
    return stack

def main():
    stack = []
    while 1:
        stack = input1(stack)
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
