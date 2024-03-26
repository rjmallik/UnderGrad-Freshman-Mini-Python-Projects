from stack import Stack
from tree import *

def infix_to_postfix(infix):
    order = {"^":4, "*":3, "/": 3, "+":2, "-":2, "(":1 }
    s = Stack()
    postfix = list()
    inputStr = infix
    operators = "+-*/^()"
    current = ""
    outputList = []

    for item in inputStr:
        if item not in operators: 
            current += item
        else:
            if current != "": 
                outputList.append(current)
                current = ""
            outputList.append(item)

    if len(current) > 0:
        outputList.append(current)
    
    for item in outputList:
        if isFloat(item):
            postfix.append(item)
        elif item == "(":
            s.push(item)
        elif item == ")":
            topStack = s.pop()
            while topStack != "(":
                postfix.append(topStack)
                topStack = s.pop()
        else: 
            while (not s.isEmpty()) and (order[item] <= order[s.peek()]):
                postfix.append(s.pop())

            s.push(item)
        
    while not s.isEmpty():
        postfix.append(s.pop())

    return " ".join(postfix)
            
            
def isFloat(n):
    try: 
        float(n)
        return True
    except ValueError:
        return False
        

def calculate(infix):
    postfix = infix_to_postfix(infix).split()
    tree = ExpTree.make_tree(postfix)
    return ExpTree.evaluate(tree)



if __name__ == '__main__':
    print("Welcome to Calculator Program!")
    while True:
        infix = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
        if infix == "quit" or infix == "q":
            break
        print(calculate(infix), sep= '\n')
    print("Goodbye!")
    
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0