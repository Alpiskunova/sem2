ops = {'+':2, '-':2, '/':1, '*':1}
in_expr = '+52*2'

stack = []
out_expr = [] 
flag = False

for elem in in_expr:
    
    if elem in ops:
        while stack != [] and stack[0] in ops and ops[elem] >= ops[stack[0]]:
            
            out_expr += [stack[0]]
            stack = stack[1:]
        stack += [elem] 
    
    elif elem == '(':
        stack += [elem]
    
    elif elem == ')':
        while stack != [] and stack[0] != '(': 
            
            out_expr += [stack[0]]
            stack = stack[1:]
            
        if stack != [] and stack[0] == '(':
            stack = stack[1:]
    
    
    elif elem in '0123456789':
        
        if len(out_expr) == 0:
            out_expr += [elem]
        else:
            if out_expr[0][-1] in '0123456789' and flag: 
                out_expr[0] += elem
                
            else: 
                out_expr += [elem]
        flag = True
        
    else: 
        flag = False
    
while stack != []: 
    out_expr = [stack[0]] + out_expr
    stack = stack[1:]

print('инфиксная запись:', in_expr)
print('постфиксная запись', " ".join(reversed(out_expr)))