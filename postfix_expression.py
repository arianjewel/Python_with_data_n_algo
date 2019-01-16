class Stack:
    """docstring for Stack."""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def is_empty(self):
        if self.items == []:
            return True
        return False

def infix_to_postfix(expression):
    precedence = {"/": 2, "*": 2, "-": 1, "+": 1}

    operators = Stack()
    postfix = []

    for item in expression:
        if item.isdigit():
            postfix.append(item)

        elif item in "*/-+":
            while operators.is_empty() is False:
                op = operators.pop()
                if precedence[op] >= precedence[item]:
                    postfix.append(op)

                else:
                    operators.push(op)
                    break

            operators.push(item)

    while operators.is_empty() is False:
        op = operators.pop()
        postfix.append(op)

    return " ".join(postfix)



def do_operation(operand1, operand2, operator):
    return eval(operand1 + operator + operand2)




#for one digit operands only
'''
def postfix_evulate(expression):
    operands = []
    operators = "*/-+"

    for char in expression:
        if char.isdigit():
            operands.append(char)

        elif char in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()

            result = do_operation(operand1, operand2, char)

            operands.append(str(result))

    result = operands.pop()

    return result
'''



#two or more digitt operands
def postfix_evulate(expression):
    operands = []
    operators = ["*", "/", "-", "+"]

    expression_list = expression.split(",")

    for item in expression_list:
        if item in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = do_operation(operand1, operand2, item)

            operands.append(str(result))

        else:
            operands.append(item)

    result = operands.pop()

    return result


if __name__ == '__main__':
    expression = "1 + 2 + 3 * 4 - 5"
    postfix_exp = infix_to_postfix(expression)
    print(postfix_exp)
    result = postfix_evulate(postfix_exp)
    print(result)
