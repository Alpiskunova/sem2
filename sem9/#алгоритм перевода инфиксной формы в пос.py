#алгоритм перевода инфиксной формы в постфиксную

in_expr = list(input()) # вход
op_stack = [] # стэк 
out_expr = [] #выход
ops = {'-': 0, '+': 1, '/': 2, '*':3} #расставили приоритеты
print(ops['-'])

for x in in_expr:
    if x in ops.keys(): #проверим, оператор ли это
            while len(op_stack) != 0 and  op_stack[-1] != '(' and ops[x] <= ops[op_stack[-1]]:
                out_expr.append(op_stack.pop())
            op_stack.append(x)
            
    elif x == '(':
        op_stack.append(x)
    elif x == ')':
        while op_stack[-1] != '(':
            out_expr.append(op_stack.pop())
        op_stack.pop() 
    else:
        out_expr.append(x)
        
while len(op_stack) != 0:
        out_expr.append(op_stack.pop())
            
print(*out_expr)
