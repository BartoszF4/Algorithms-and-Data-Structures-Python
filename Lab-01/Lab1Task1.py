class Stack:
    def __init__(self, size, data_type):
        self.max_size = size
        self.data_type = data_type
        self.array = [None] * size
        self.top_index = -1

    def push(self, item):
        if self.top_index >= self.max_size - 1:
            raise OverflowError("Stack Overflow")
        self.top_index += 1
        self.array[self.top_index] = item

    def pop(self):
        if self.isempty():
            raise IndexError("Stack Underflow")
        popped_item = self.array[self.top_index]
        self.array[self.top_index] = None
        self.top_index -= 1
        return popped_item

    def isempty(self):
        return self.top_index == -1

    def top(self):
        if self.isempty():
            return None
        return self.array[self.top_index]


def precedence(op):
    if op in ('+', '-'):
        return 2
    elif op in ('*', '/'):
        return 1
    return 0


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def infix_to_postfix(expression):
    tokens = expression.split()
    stack = Stack(len(tokens), str)
    postfix = []

    for token in tokens:
        if is_number(token):
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.isempty() and stack.top() != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while (not stack.isempty() and stack.top() != '(' and
                   precedence(stack.top()) >= precedence(token)):
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.isempty():
        postfix.append(stack.pop())
    return " ".join(postfix)


def evaluate_postfix(postfix_expr):
    tokens = postfix_expr.split()
    stack = Stack(len(tokens), float)

    for token in tokens:
        if is_number(token):
            stack.push(float(token))
        else:
            val2 = stack.pop()
            val1 = stack.pop()

            if token == '+':
                stack.push(val1 + val2)
            elif token == '-':
                stack.push(val1 - val2)
            elif token == '*':
                stack.push(val1 * val2)
            elif token == '/':
                if val2 == 0:
                    raise ValueError("Division by zero")
                else:
                    stack.push(val1 / val2)

    return stack.pop()


if __name__ == "__main__":
    expr1 = "( 3 * 6 + 2 ) + ( 14 / 3 + 4 )"
    expr2 = "17 * ( 2 + 3 ) + 4 + ( 8 * 5 )"

    print("Exercise 1")
    postfix1 = infix_to_postfix(expr1)
    print(f"Infix: {expr1}")
    print(f"Postfix: {postfix1}")
    print(f"Result: {evaluate_postfix(postfix1)}\n")

    postfix2 = infix_to_postfix(expr2)
    print(f"Infix: {expr2}")
    print(f"Postfix: {postfix2}")
    print(f"Result: {evaluate_postfix(postfix2)}")