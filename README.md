# Optimization-problem
In this study I implemented various techniques for finding extrema values. These methods are: 1) Gradient descent method, 2) Random Search method. These two methods were compared according to their computational cost. It was found that method of Gradient Descent is faster if implemented using optimal learning rate.

## Introduction

There are several methods for finding optimal values for the functions. Golden section method is used for one-dimensional unconstrained functions. In this assignment it was especially useful for finding the value of alpha - optimal learning rate with respect to x. However, for the multi-dimensional functions it is better to use Gradient descent method or random search method. However, it is assumed that the second method is not that fast as the first one.

## Methods

First, I defined a given function f and its x,y - gradients. In order to see an approximate values at which a local extrema occures, I demonstrated a plot of the function. From this plot it is clear that there is no local maxima and the following steps should be directed to local minima.

![image](https://github.com/leilaakisheva/Optimization-problem/assets/128895782/a84213b8-6598-4e7d-abd9-6c194ecebcf2)


## Results
-1.0 1.5 -1.25 num. of iterations = 176


value of the optimal learning rate:  0.25581104862019466


Minimum found at x = -1.0000475168831424 , y = 1.4999762415584288 , f(x,y) = -1.2499999926619743


### Values computed by the Gradient Descent method: 
x_min = -1.0000009371566865 y_min = 1.4999994208053147 f(x,y) = -1.2499999999968225 number of iterations = 121


### Values computed by the Random Search method: 
x_min = -1.0000594423941576 y_min = 1.4999702788029212 f(x,y) = -1.2499999885164557


Total time for implementing Gradient Descent method with the optimal value of learning rate: 0.00028613100221264176


Total time for implementing Random Search method with the fixed number of iterations n=10000: 0.2012208179985464


Ratio of the cost of Rand. Search to Gradient Descent:  0.8509290775743975

As it can be seen the ratio of the Rand. Search method cost to the Gradient descent cost is not very large. However, it is still essential. Moreover, as it can be seen compilation time for the random search method is 100x larger than total compilation time for the gradient descent method.

## Conclusion
Two methods for finding optimal values were compared in this assignment. It was demonstrated that the gradient descent method is faster and has less computational cost. This can be explained by the number of iterations made per code implementation. For the random search it was fixed n=100000, for the gradient descent method it was depending on the optimal value of learning rate (however, rarely exceeding n=200).
