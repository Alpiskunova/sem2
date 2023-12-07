in_expr = list(input())

stack = [] # стэк 
ops = ['-', '+', '*', '/']
for x in in_expr:
    #print(stack)
    if x in ops:
            number1 = stack.pop()
            number2 = stack.pop()
            if number1 in ops or number2 in ops:
                print('Ввод некорректен')
            else:
                if x == '*':
                    res = int(number2)*int(number1)
                elif x == '/':
                    res = int(number2)/int(number1)
                elif x == '+':
                    res = int(number2) + int(number1)
                elif x == '-':
                     res = int(number2) - int(number1)
                stack.append(res)
    else:
        stack.append(int(x))
        
if len(stack) != 0:
    print(stack[0])
else:
    print('Error')