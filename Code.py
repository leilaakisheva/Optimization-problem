import numpy as np
import random
import matplotlib.pyplot as plt
import math
import timeit

"""###**Introduction**
There are several methods for finding optimal values for the functions. Golden section method is used for one-dimensional unconstrained functions. In this assignment it was especially useful for finding the value of alpha - optimal learning rate with respect to x. However, for the multi-dimensional functions it is better to use Gradient descent method or random search method. However, it is assumed that the second method is not that fast as the first one.

###**Methods**
First, I defined a given function f and its x,y - gradients. In order to see an approximate values at which a local extrema occures, I demonstrated a plot of the function. From this plot it is clear that there is no local maxima and the following steps should be directed to local minima.
"""

def f(x,y):
  return x-y+2*x*x+2*x*y+y*y
def gradient(symbol, x, y):
    if symbol=='x':
        return 1+4*x+2*y
    if symbol=='y':
        return -1+2*x+2*y

y=np.linspace(-5, 5, 100)
x=np.linspace(-5, 5, 100)
X = np.zeros((100, 100))
Y = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        X[i,j] = x[i]
        Y[i,j] = y[j]
z=f(X,Y)
#3D plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, z, cmap="viridis")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.show()

def gradient_descent(a, tol):
  x = 100*random.random() #Defining initial values of x, y
  y = 100*random.random()
  n=0
  # Initialize x and y with a random value between 0 and 1
  for i in range(1000):
        grad_x=gradient('x', x, y)
        grad_y=gradient('y', x, y)
        x_new=x-a*grad_x #formula of gradient descent
        y_new=y-a*grad_y
        if abs(f(x_new, y_new)-f(x, y))<tol:
            break
        x, y=x_new, y_new
        n=n+1 #calculating number of iterations
  return x, y, f(x, y), n
x_min, y_min, f_min, n = gradient_descent(0.1, 1e-12)
print(round(x_min, 3), round(y_min, 3), round(f_min, 3), "num. of iterations =", n)

#Calculating the optimal learing rate
def golden_section(x_l, x_u, tol): #Finding the minimum of the function f(x) over the interval [x_l, x_u] using golden section method
    R=((5**0.5)-1)/2
    x1=x_l+(1-R)*(x_u-x_l) #Defining x1, x2
    x2=x_l+R*(x_u-x_l)
    f1=gradient_descent(x1, tol) #Defining the values of the gradient descent method using the values of x1, x2
    f2=gradient_descent(x2, tol)
    while abs(x_u-x_l)>tol:
        if f1<f2:
            x_u=x2
            x2=x1
            f2=f1
            x1=x_l+(1-R)*(x_u-x_l)
            f1=gradient_descent(x1,tol)
        else:
            x_l=x1
            x1=x2
            f1=f2
            x2=x_l+R*(x_u-x_l)
            f2=gradient_descent(x2,tol)
    return (x_l+x_u)/2
alpha_opt=golden_section(-0.5,0.5,1e-12)
print("value of the optimal learning rate:", alpha_opt)

def rand_search(x_l, x_u, y_l, y_u, imax): #Defining the random search method
    x=100*np.random.uniform(x_l, x_u)
    y=100*np.random.uniform(y_l, y_u)
    r=np.random.uniform(0,1,imax)
    f_best=f(x, y)
    for i in range(imax):
        x_curr=x_l+(x_u-x_l)*r[i] #Defining current value of x and y
        y_curr=y_l+(y_u-y_l)*r[i]
        f_curr=f(x_curr, y_curr) #finding the current value of the f(x,y) for the above values of x,y
        if f_curr<f_best: #since we should find the minima, current value of the function should be less than previous
            x=x_curr #Redefining the value of x and y
            y=y_curr
            f_best=f_curr #now the best fit of the function is current value of the function for which condition is fulfilled
    return x, y, f_best
x_min, y_min, f_min= rand_search(-2, 2, 1, 3, imax=100000)
print("Minimum found at x =", x_min, ", y =", y_min, ", f(x,y) =", f_min)

start_time = timeit.default_timer()
x_min1, y_min1, f_min1, n = gradient_descent(alpha_opt, 1e-12)
total_time1 = timeit.default_timer() - start_time
print("Values computed by the Gradient Descent method: \nx_min =", x_min1,"y_min =", y_min1,"f(x,y) =", f_min1,"number of iterations =", n)
start_time = timeit.default_timer()
x_min2, y_min2, f_min2 = rand_search(-2, 2, 1, 3, 100000)
total_time2 = timeit.default_timer() - start_time

print("Values computed by the Random Search method: \nx_min =", x_min2,"y_min =", y_min2,"f(x,y) =", f_min2)
cost1=total_time1/n
cost2=total_time2/100000

print("Total time for implementing Gradient Descent method with the optimal value of learning rate:", total_time1)
print("Total time for implementing Random Search method with the fixed number of iterations n=100000:", total_time2)

ratio=cost2/cost1
print("Ratio of the cost of Rand. Search to Gradient Descent: ", ratio)

"""###**Results**
As it can be seen the ratio of the Rand. Search method cost to the Gradient descent cost is not very large. However, it is still essential. Moreover, as it can be seen compilation time for the random search method is 100x larger than total compilation time for the gradient descent method.
###**Conclusion**
Two methods for finding optimal values were compared in this assignment. It was demonstrated that the gradient descent method is faster and has less computational cost. This can be explained by the number of iterations made per code implementation. For the random search it was fixed n=100000, for the gradient descent method it was depending on the optimal value of learning rate (however, rarely exceeding n=200).
"""
