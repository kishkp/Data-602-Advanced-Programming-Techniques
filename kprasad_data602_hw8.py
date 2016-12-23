# Kishore Prasad
# Data 602 - HW Assignment 8

import scipy.misc as misc
import scipy.ndimage as ndimage
import pymorph
import pylab

# for circles.png
img_source = misc.imread('./circles.png')
img_trans = ndimage.gaussian_filter(img_source, 8)
img_thres = img_trans > img_trans.mean()
pylab.imshow(img_thres)
img_distance = ndimage.distance_transform_edt(img_thres)
found, n_found = ndimage.label(img_distance)
img_center_mass = ndimage.measurements.center_of_mass(img_distance, found, xrange(1, n_found+1))
print 'Circles.png -  Objects found : %d \n' %(n_found) 
print 'Circles.png -  Center of Mass: %s \n' %(img_center_mass) 

# using pymorph for images since we are not getting 5 objects for this
peaks = pymorph.regmax(img_trans)
found, n_found = ndimage.label(peaks)
img_center_mass = ndimage.measurements.center_of_mass(img_distance, found, xrange(1, n_found+1))
print 'Pymorph Circles.png -  Objects found : %d \n' %(n_found) 
print 'Pymorph Circles.png -  Center of Mass: %s \n' %(img_center_mass) 

# for objects.png
img_source = misc.imread('./objects.png')
img_trans = ndimage.gaussian_filter(img_source, 3)
img_thres = img_trans > img_trans.mean()
pylab.imshow(img_thres)
img_distance = ndimage.distance_transform_edt(img_thres)
found, n_found = ndimage.label(img_distance)
img_center_mass = ndimage.measurements.center_of_mass(img_distance, found, xrange(1, n_found+1))
print 'Objects.png -  Objects found : %d \n' %(n_found) 
print 'Objects.png -  Center of Mass: %s \n' %(img_center_mass) 

# for peppers.png
img_source = misc.imread('./peppers.png')
img_trans = ndimage.gaussian_filter(img_source, 2.5)
img_thres = img_trans > img_trans.mean()
pylab.imshow(img_thres)
img_distance = ndimage.distance_transform_edt(img_thres)
found, n_found = ndimage.label(img_distance)
img_center_mass = ndimage.measurements.center_of_mass(img_distance, found, xrange(1, n_found+1))
print 'Peppers.png -  Objects found : %d \n' %(n_found) 
print 'Peppers.png -  Center of Mass: %s \n' %(img_center_mass) 
