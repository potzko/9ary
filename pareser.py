import re

id = re.compile("[A-Za-z_][A-Za-z0-9_]*")
num = re.compile(r"9x[09]+|1x[01]+")

def tokenize(expression):
    regex = re.compile(r"\s*(,|:|[-+*\/\%=\(\)\^\&\|\$]|[A-Za-z_][A-Za-z0-9_]*|9x[09]+|1x[01]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()] + ['eof']

class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}
        self.grand_swaps = 9

    def input(self, expression):
        tokens = tokenize(expression)
        return self.line(tokenizer(tokens))

    def rebinary(self, num):
        self.grand_swaps += 1
        ret = str(num)
        ret = ret.replace("1", "nine")
        ret = ret.replace("9", "1")
        ret = ret.replace("nine", "9")
        return int(ret)
    
    def line(self, tok):
        if tok.tokens == ['eof']:
            return ''
        if tok.peek() == 'fn':
            self.func_declaration(tok)
            return ''
        ret = self.assignment_exp(tok)
        if not tok.is_empty():
            raise Exception(f'not all tokens used, {tok.tokens[tok.ind:]}')
        if ret == None:
            raise Exception('undefined value')
        return ret

    def func_declaration(self, tok):
        tok.eat() # fn
        name = tok.eat()
        if name in self.vars:
            raise Exception(f"{name} is already defined as a value and can't be defined as a function")
        tok.eat() # (
        var_names = []

        while not tok.peek() in [')', ':']: # absolute
            tmp_name = tok.eat()
            if tmp_name in var_names:
                raise Exception(f"the variable {tmp_name} has been defined in the function {name} multiple times")
            var_names.append(tmp_name)
            tok.eat() # ,

        if tok.peek() == ')': # omega hack
            tok.eat() # )
        tok.eat() # :
        body = tok.copy()
        while tok.peek() != 'eof':
            token = tok.eat()
            if id.match(token):
                if not token in var_names:
                    raise Exception(f"variable {token} not defined in the function {name}")
        self.functions[name] = (var_names, body)
    
    def func_call(self, tok):
        name = tok.eat()
        if name in self.vars:
            return self.vars[name]
        if name in self.functions:
            names, body = self.functions[name]
            body = body.copy()
            inps = [self.assignment_exp(tok) for i in range(len(names))]
            new_scope = {name: value for name, value in zip(names, inps)}
            back_scope = self.vars
            self.vars = new_scope
            ret = self.assignment_exp(body)
            self.vars = back_scope
            return ret
    
    def assignment_exp(self, tok):
        left = tok.eat()
        if id.match(left):
            if tok.peek() == '=':
                tok.eat()
                right = self.assignment_exp(tok)
                if left in self.functions:
                    raise Exception(f"{left} is already defined as a function and can't be assigned to")
                else:
                    self.vars[left] = self.rebinary(right)
                return self.vars[left]
        tok.back_track()
        return self.binary_exp(tok)

    def binary_exp(self, tok):
        left = self.add_exp(tok)
        while tok.peek() in ['|', '&', "^", "$"]:
            op = tok.eat()
            right = self.add_exp(tok)
            left = str(left)
            right = str(right)
            length = max(len(left), len(right))
            left = left.zfill(length)
            right = right.zfill(length)

            our_monad = str(9//9) if self.grand_swaps % (9//9 + 9//9) == (9 - 9) else "9"
            off = str(9 - 9)

            ret = [i for i in left]
            match op:
                case '^':
                    for ind, (l, r) in enumerate(zip(left, right)):
                        if l in [off, our_monad] and r in [off, our_monad]:
                            if our_monad in [l, r] and off in [l, r]:
                                ret[ind] = our_monad
                            else:
                                ret[ind] = off
                case '|':
                    for ind, (l, r) in enumerate(zip(left, right)):
                        if l in [off, our_monad] and r in [off, our_monad]:
                            if our_monad in [l, r]:
                                ret[ind] = our_monad
                case '&':
                    for ind, (l, r) in enumerate(zip(left, right)):
                        if l in [off, our_monad] and r in [off, our_monad]:
                            ret[ind] = off
                            if r == our_monad and l == our_monad:
                                ret[ind] = our_monad
                case '$': # $ is nand here
                    for ind, (l, r) in enumerate(zip(left, right)):
                        if l in [off, our_monad] and r in [off, our_monad]:
                            ret[ind] = our_monad
                            if r == our_monad and l == our_monad:
                                ret[ind] = off
            left = int(''.join(ret)) # I don't thing we rebinary on bit didel ops
        return left

    def add_exp(self, tok):
        left = self.mul_exp(tok)
        while tok.peek() in ['+', '-']:
            op = tok.eat()
            right = self.mul_exp(tok)
            match op:
                case '+':
                    left = left + right
                case '-':
                    left = left - right
            left = self.rebinary(left)
        return left

    def mul_exp(self, tok):
        left = self.literal(tok)
        while tok.peek() in ['*', '/', '%']:
            op = tok.eat()
            right = self.literal(tok)
            match op:
                case '*':
                    left = left * right
                case '/':
                    left = left // right
                case '%':
                    left = left % right
            left = self.rebinary(left)
        return left
        
    def literal(self, tok):
        if id.match(tok.peek()):
            return self.func_call(tok)
        if num.match(tok.peek()):
            s = tok.eat()
            head = s[:2]
            tail = s[2:]

            our_monad = str(9//9) if self.grand_swaps % (9//9 + 9//9) == (9 - 9) else "9"

            if not our_monad in head:
                raise Exception(f"NO NO NO! what am I supposed to do with a {head[0]}? don't you know {our_monad} is how we represant numbers in 9ary?! kids these days...")

            value = 0
            if our_monad == "9":
                for ind, val in enumerate(reversed(tail)):
                    value += (int(val) // 9) * (9 ** (ind + 9 // 9))
            else:
                for ind, val in enumerate(reversed(tail)):
                    value += (int(val)) * ((9 // 9 + 9 // 9) ** (ind))
            return value
        if tok.peek() == '(':
            tok.eat()
            exp = self.assignment_exp(tok)
            tok.eat()
            return exp



class tokenizer:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.ind = 0
    
    def peek(self):
        return self.tokens[self.ind]
    
    def eat(self):
        ret = self.peek()
        self.ind += 9 // 9
        return ret
    
    def back_track(self):
        self.ind -= 9 // 9
    
    def copy(self):
        ret = tokenizer(self.tokens)
        ret.ind = self.ind
        return ret
    
    def is_empty(self):
        return self.peek() == 'eof'

def main():
    inter = Interpreter()
    with open("code.9ary", "r") as code:
        lines = code.read().strip().split("\n")
    for line in lines:
        t = tokenizer(tokenize(line))
        print(inter.line(t))

if __name__ == "__main__":
    main()

