import re

class ScriptInterpreter:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expression):
        tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)|[a-zA-Z_]\w*|==|!=|<=|>=|<|>|and|or|not', expression)
        operator_stack = []
        operand_stack = []

        for token in tokens:
            if token.isdigit():
                operand_stack.append(int(token))
            elif token in self.variables:
                operand_stack.append(self.variables[token])
            elif token in ['+', '-', '*', '/', '==', '!=', '<=', '>=', '<', '>', 'and', 'or', 'not']:
                while (operator_stack and
                       self.precedence(operator_stack[-1]) >= self.precedence(token)):
                    self.apply_operation(operator_stack.pop(), operand_stack)
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack[-1] != '(':
                    self.apply_operation(operator_stack.pop(), operand_stack)
                operator_stack.pop()

        while operator_stack:
            self.apply_operation(operator_stack.pop(), operand_stack)

        if operand_stack:
            return operand_stack[0]  # Return the result if the operand stack is not empty
        else:
            return None  # Return None if the operand stack is empty

    def precedence(self, op):
        if op in ['+', '-']:
            return 1
        elif op in ['*', '/']:
            return 2
        elif op in ['==', '!=', '<=', '>=', '<', '>', 'and', 'or', 'not']:
            return 3
        else:
            return 0

    def precedence(self, op):
        if op in ['+', '-']:
            return 1
        elif op in ['*', '/']:
            return 2
        elif op in ['==', '!=', '<=', '>=', '<', '>', 'and', 'or', 'not']:
            return 3
        else:
            return 0

    def apply_operation(self, op, operand_stack):
        if op == 'and':
            operand_stack.append(operand_stack.pop() and operand_stack.pop())
        elif op == 'or':
            operand_stack.append(operand_stack.pop() or operand_stack.pop())
        elif op == 'not':
            operand_stack.append(not operand_stack.pop())
        else:
            b = operand_stack.pop()
            a = operand_stack.pop()
            if op == '+':
                operand_stack.append(a + b)
            elif op == '-':
                operand_stack.append(a - b)
            elif op == '*':
                operand_stack.append(a * b)
            elif op == '/':
                if b==0:
                   print("You can't divide by 0")
                else:
                    operand_stack.append(a / b)
            elif op == '==':
                operand_stack.append(a == b)
            elif op == '!=':
                operand_stack.append(a != b)
            elif op == '<=':
                operand_stack.append(a <= b)
            elif op == '>=':
                operand_stack.append(a >= b)
            elif op == '<':
                operand_stack.append(a < b)
            elif op == '>':
                operand_stack.append(a > b)

    def interpret(self, code):
        lines = code.split('\n')
        output = []
        for line in lines:
            if line.startswith('IF'):
                parts = re.split(r'\sTHEN\s|\sELSE\s', line.strip())
                condition = parts[0]
                expr_if = parts[1]
                expr_else = parts[2]

                if self.evaluate_expression(condition):
                    result = self.evaluate_expression(expr_if)
                    output.append(result)
                else:
                    result = self.evaluate_expression(expr_else)
                    output.append(result)
            elif '=' in line:
                length = 0
                seperated_line = line.split('=')
                for num in seperated_line:
                    if not num.isdigit():
                        break
                    length += 1
                if length == 2:
                    num1, num2 = line.split('=')
                    return int(num1) == int(num2)
                else:
                    var_name, expr = line.split('=')
                    var_name = var_name.strip()
                    expr = expr.strip()
                    self.variables[var_name] = self.evaluate_expression(expr)
                    if line.strip():  # Only evaluate non-empty lines
                        result = self.evaluate_expression(line.strip())
                        output.append(result)
                return output
            elif '>' in line:
                length = 0
                seperated_line = line.split('>')
                for num in seperated_line:
                    if not num.isdigit():
                        break
                    length += 1
                if length == 2:
                    num1, num2 = line.split('>')
                    return int(num1) > int(num2)

            elif '<' in line:
                length = 0
                seperated_line = line.split('<')
                for num in seperated_line:
                    if not num.isdigit():
                        break
                    length += 1
                if length == 2:
                    num1, num2 = line.split('<')
                    return int(num1) < int(num2)
            else:
                result = interpreter.evaluate_expression(line)
                return result





if __name__ == "__main__":
    interpreter = ScriptInterpreter()
    while True:
        code = input(">> ")
        if code == "exit":
            break
        output = interpreter.interpret(code)
        if type(output)== bool:
            print(output)
        else:
            if type(output) == int:
                print(output)

            else:
                for result in output:
                    print(result)
