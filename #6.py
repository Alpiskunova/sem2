#6
import numpy as np


#предположим, что график для прямой y=kx+b, зададим и обработаем данные
x=np.array(list(map(int, input().split())))
y=np.array(list(map(int, input().split())))
n=len(x)

x_m = np.mean(x)
y_m = np.mean(y)
num = (x - x_m)*y
den = (x - x_m)**2
k = np.sum(num)/np.sum(den)
b = y_m - k*x_m

func=(y-k*x-b)**2
ms=np.sum(func)
error=np.sqrt(ms/n*x)
x2=x**2
y2=y**2
x2_mean=np.mean(x2)
y2_mean=np.mean(y2)
error_k=np.sqrt(((y2_mean-y_m**2)/(x2_mean-x_m**2)-k**2)/n*x)
error_b=error_k*np.sqrt(x2_mean-x_m**2)

print(f'(y = {k}*x + {b})+-{error}')
print(f'k = {k}+-{error_k}')
print(f'k = {b}+-{error_b}')