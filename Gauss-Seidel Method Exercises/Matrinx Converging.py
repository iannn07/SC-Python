#Converging
import numpy as np

x1 = 0
x2 = 0
x3 = 0
treshold = 0.01
converged = False

x_old = np.array([x1, x2, x3])

n = int(input('Enter the number of iteration: '))

print('\nIteration results')
print('No\tX1\t\tX2\t\tX3')
print('----------------------------------------------')
for k in range(0,n):
    x1 = (14-3*x2+3*x3)/8
    x2 = (5+2*x1-5*x3)/(-8)
    x3 = (-8-3*x1-5*x2)/(-5)
    x = np.array([x1, x2, x3])
    
    dx = np.sqrt(np.dot(x-x_old, x-x_old))
    print("%d\t%.4f\t\t%.4f\t\t%.4f"%(k+1, x1, x2, x3))
    if dx < treshold:
        converged = True
        print("\n\t\t===SOLVED!===")
        print("Here's the result:")
        print("X1 = %.4f; X2 = %.4f; X3 = %.4f\n"%(x1, x2, x3))
        break
        
    x_old = x

if not converged:
    print("Can't be solved, please increase the iterations")