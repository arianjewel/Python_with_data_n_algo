'''
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

if __name__ == '__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    while s.is_empty()==False:
        s.pop()
        print(s.items)
'''







'''
def is_balanced(input_str):
    for ch in input_str:
        if ch == '(':
                l.append(ch)
        if ch == ')':
            if not l:
                return False
            l.pop()
    return not l
'''







def is_balanced(input_str):

    for ch in input_str:

        if ch == '(' or ch == '{' or ch == '[':
                l.append(ch)

        if ch == ')' or ch == '}' or ch == ']':

            if not l:
                return False

            if ch == ')':

                if '(' not in l or l[-1]!='(':
                    return False

                l.pop(-1)

            if ch == '}':

                if '{' not in l or l[-1]!='{':
                    return False

                l.pop(-1)

            if ch == ']':

                if '[' not in l or l[-1]!='[':
                    return False

                l.pop(-1)

    return not l

if __name__ == '__main__':

    l=list()

    input_str=input()

    if is_balanced(input_str):
        print(input_str,'is balanced')

    else:
        print(input_str,'is not balanced')
