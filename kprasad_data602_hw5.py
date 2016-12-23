# Kishore Prasad
# Data 602 - HW Assignment 5

import Tkinter
import tkFileDialog
import pandas

root = Tkinter.Tk()
root.withdraw()


# read the data file from a file prompt
filename = tkFileDialog.askopenfilename(parent=root)
body_brain = pandas.read_csv(filename, names = ['Animal', 'Body', 'Brain'], header=0)

#Sum of the respective columns and other calculations
brain_sum = body_brain['Brain'].sum()
body_sum = body_brain['Body'].sum()
brain_body_sum = sum(body_brain['Body'] * body_brain['Brain']) 
brain_sq_sum = sum(body_brain['Brain'] * body_brain['Brain']) 

num_rows = len(body_brain)

X = ((num_rows*brain_body_sum)-(brain_sum*body_sum))/((num_rows*brain_sq_sum)-(brain_sum*brain_sum))
Y = ((body_sum*brain_sq_sum)-(brain_sum*brain_body_sum))/(num_rows*(brain_sq_sum)-(brain_sum*brain_sum))

#leverage known formulas for slope/intercept in simple linear regression
print "The slope of the least squares fit line is : %s \n" %(str(X))
print "The intercept of the least squares fit line is : %s \n" %(str(Y))
print "The Formula is: Body = %s * Brain + (%s)" %(str(round(X,4)),str(round(Y,4)))


import numpy as np
from scipy.optimize import curve_fit
# Creating a function to model and create data
def func(x, a, b):
    return a * x + b
# Generating clean data

x = np.linspace(0, 10, 62)
y = func(x, body_brain['Brain'], body_brain['Body'].sum())
# Adding noise to the data
yn = y + 0.9 * np.random.normal(size=len(x))
# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)
# popt returns the best fit values for parameters of
# the given model (func).
print(popt)