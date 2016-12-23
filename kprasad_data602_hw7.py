# Kishore Prasad
# Data 602 - HW Assignment 5

import Tkinter
import tkFileDialog
import pandas
import numpy as np
from scipy.optimize import curve_fit
import timeit

root = Tkinter.Tk()
root.withdraw()

# read the data file from a file prompt
filename = tkFileDialog.askopenfilename(parent=root)
body_brain = pandas.read_csv(filename, names = ['Animal', 'Body', 'Brain'], header=0)

x = body_brain['Brain']
y = body_brain['Body']

def my_linreg(x, y):
    #Sum of the respective columns and other calculations
    x_sum = x.sum()
    y_sum = y.sum()
    xy_sum = sum(x * y) 
    x_sq_sum = sum(x * x) 
    num_rows = len(x)

    slope = ((num_rows*xy_sum)-(x_sum*y_sum))/((num_rows*x_sq_sum)-(x_sum*x_sum))
    intercept = ((y_sum*x_sq_sum)-(x_sum*xy_sum))/(num_rows*(x_sq_sum)-(x_sum*x_sum))
    params = (slope, intercept)    
    print "My Linear regression Output : body =  %s * brain + (%s)" %(params[0],params[1])
    return params

def linear_func(x, a, b):
    return a * x + b

def gauss_func(x,a,b,c):
    return a * np.exp(-(x-b)**2/(2*c**2))

def scipy_lin_curvefit(linear_func, x, y):
    params=curve_fit(linear_func, x, y)
    print "Scipy Linear regression Output : body =  %s * brain + (%s)" %(params[0][0],params[0][1])
    return params

def scipy_gauss_curvefit(gauss_func, x, y):
    params = curve_fit(gauss_func, x, y)
    print "Scipy Gaussian Output : body =  (%s) * exp( -(brain - (%s))**2 / (2 * %s**2) )" %(params[0][0],params[0][1], params[0][2])
    return params

setup='''
import pandas
import numpy as np
from scipy.optimize import curve_fit

body_brain = pandas.read_csv("{0}", names = ['Animal', 'Body', 'Brain'], header=0)

x = body_brain['Brain']
y = body_brain['Body']

def my_linreg(x, y):
    #Sum of the respective columns and other calculations
    x_sum = x.sum()
    y_sum = y.sum()
    xy_sum = sum(x * y) 
    x_sq_sum = sum(x * x) 
    num_rows = len(x)

    slope = ((num_rows*xy_sum)-(x_sum*y_sum))/((num_rows*x_sq_sum)-(x_sum*x_sum))
    intercept = ((y_sum*x_sq_sum)-(x_sum*xy_sum))/(num_rows*(x_sq_sum)-(x_sum*x_sum))
    
    return (slope, intercept)

def linear_func(x, a, b):
    return a * x + b

def gauss_func(x,a,b,c):
    return a * np.exp(-(x-b)**2/(2*c**2))

def scipy_lin_curvefit(linear_func, x, y):
  return curve_fit(linear_func, x, y)

def scipy_gauss_curvefit(gauss_func, x, y):
  return curve_fit(gauss_func, x, y)

'''.format(filename)


params = my_linreg(x,y)
params = scipy_lin_curvefit(linear_func, x,y)
params = scipy_gauss_curvefit(gauss_func, x,y)


# Number of times to execute the timed test
n = 100

# Execute the Sort test for smaller test subject and print the results
t1_100 = timeit.timeit("params = my_linreg(x,y)", setup=setup, number=n)
t2_100 = timeit.timeit("params = scipy_lin_curvefit(linear_func, x,y)", setup=setup, number=n)
t3_100 = timeit.timeit("params = scipy_gauss_curvefit(gauss_func, x,y)", setup=setup, number=n)

print("""
Timings for the 3 regressions executed {0} times

Using custom Linear Regression               : {1:.5f} sec
Using Scipy curve_fit for Linear Regression  : {2:.5f} sec
Using Scipy Gaussian Regression              : {3:.5f} sec

""".format(n, t1_100, t2_100, t3_100))



