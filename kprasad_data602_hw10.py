# Kishore Prasad
# Data 602 - HW Assignment 9

import Tkinter
import tkFileDialog
import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
from scipy import stats, misc, ndimage

root = Tkinter.Tk()
root.withdraw()

# 1. Express the cars.data.csv data as a series of bar graphs.  The x-axis represents a feature and the y-axis is 
# the frequency in the sample.  Do this with the "buying", "maint", "safety", and "doors" fields with one plot for 
# each for a total of four.  Make each graph a subplot of a single output.  


# read cars data from a file prompt
filename = tkFileDialog.askopenfilename(parent=root)
cars = pd.read_csv(filename, names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'acceptability'], header = None)

plot_vars = [['buying', 'maint'], ['safety', 'doors']]

plot.style.use('ggplot')

# create subplots
f, axs = plot.subplots(2, 2, figsize=(8, 6))
for row in range(2):
    for col in range(2):
        plot_var = plot_vars[row][col]
        data = cars[plot_var].value_counts(sort=False)
        axs[row][col].bar(range(len(data.index)), data.values, align='center', alpha = 0.75)
        axs[row][col].set_title(plot_var.title())
        # set appropriate category labels and locations
        axs[row][col].set_xticks(range(len(data.index)))
        axs[row][col].set_xticklabels(data.index)
        axs[row][col].set_xlabel('Categories')
        axs[row][col].set_ylabel('Count')
f.subplots_adjust(hspace=0.4)
f.suptitle('Frequencies for Buying, Maintenance, Doors and Safety in Car dataset', fontsize = 16)
plot.show()


# 2. Plot your results from the linear regression in homework 5 and 7 (for any of the provided data sets). The plot should include.  
# 1) a scatter of the points in the .csv file 
# 2) a line showing the regression line (either from the calculation in homework 5 or line-fitting from homework 7).  
# 3) something on the plot that specifies the equation for the regression line.  

# read the data file from a file prompt
filename = tkFileDialog.askopenfilename(parent=root)
body_brain = pd.read_csv(filename, names = ['Animal', 'Body', 'Brain'], header=0)

brain = body_brain['Brain']
body = body_brain['Body']

# perform regression
lin_reg = stats.linregress(brain, body)

# Create Plot
x = [brain.min(), brain.max()]
y = [lin_reg.intercept + lin_reg.slope * item for item in x]

# plot points and line
plot.figure(figsize = (8,6))
plot.title('Body Weight vs. Brain Weight - Regression\n', size=16)
plot.xlabel('Brain Weight')
plot.ylabel('Body Weight')
plot.plot(brain, body, '.', alpha = 0.75)
plot.plot(x, y, ':', alpha = 0.75, lw = 1.5)
# annotate equation
plot.annotate('body = %.3f + %.3f * brain' % (lin_reg.intercept, lin_reg.slope),
             xy=(3000, lin_reg.intercept + 3000 * lin_reg.slope),
             xytext=(3000, 100)
            )
plot.show()


# 3. Create an overlay of the center points found in objects.png from homework 8.  
#    The image should be in the background and the object centers can be small circles or points at 
#    or around the center points.  

filename = tkFileDialog.askopenfilename(parent=root)
raw_image = misc.imread(filename)

image = ndimage.gaussian_filter(raw_image, 2)
threshold = image > image.mean()

#find objects
distance = ndimage.distance_transform_edt(threshold)
found, n_found = ndimage.label(distance)
cent_of_mass = ndimage.measurements.center_of_mass(distance, found, xrange(1, n_found+1))
# store coordinates of objects
x = [item[1] for item in cent_of_mass]
y = [item[0] for item in cent_of_mass]

implot = plot.imshow(raw_image)
plot.plot(x, y, 'o')
plot.title("Objects' Centers of Mass in objects.png\n", size=16)
plot.xlim(0, 585)
plot.ylim(512, 0)
plot.grid(False)
plot.show()


# 4. Plot a line graph that shows the hour by hour change in number of server requests from the HTTP in homework 9.  
#    The x-axis is the discrete hour intervals (e.g. 13:00 – 14:00) and the y-axis is the number of requests.  

# read the data file from a file prompt
filename = tkFileDialog.askopenfilename(parent=root)
http_data = pd.read_csv(filename, delimiter = " ", names = ["host","date", "request", "reply", "bytes"],  header=None)

# Generate Datetime column
http_data["date"] = pd.to_datetime("1995-08" + http_data["date"], format="%Y-%m[%d:%H:%M:%S]")
http_data = http_data[~np.isnan(http_data.reply)]

#During what hour was the server the busiest in terms of requests?  (You can do this by grouping each hour period e.g. 13:00 – 14:00. Then count the number of requests in each hour)
http_data["hour"]= http_data["date"].dt.hour

by_hour = http_data.groupby('hour').size()

# create plot
plot.figure(figsize=(8,6))
plot.plot(by_hour.index, by_hour.values)
plot.title('Requests by Hour\n', size=16)
plot.xlabel('Hour')
plot.ylabel('Requests')
plot.xlim(-1, 24)
plot.xticks(np.arange(0, 25, 4))
plot.show()

