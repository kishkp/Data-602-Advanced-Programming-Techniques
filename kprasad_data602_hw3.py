# Kishore Prasad
# Data 602 - HW Assignment 3

import Tkinter
import tkFileDialog
import pandas

def loadCars():
    """ Loads all the cars from a csv file using a file dialog. 
        It prints out the rows that have issues but loads the data irrespective of whether the data is valid or not.
    """
    root = Tkinter.Tk()
    root.withdraw()
    filename = tkFileDialog.askopenfilename(parent=root)

    car_list = pandas.read_csv(filename, names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', \
    'safety', 'acceptability'], header = None)

    print "The following car entries are invalid: \n"

    L = car_list.copy()

    L['valid'] = L['buying'].isin(['low', 'med', 'high', 'vhigh']) & \
                    L['maint'].isin(['low', 'med', 'high', 'vhigh']) & \
                    L['doors'].isin(['2', '3', '4', '5more']) & \
                    L['persons'].isin(['2', '4', 'more']) & \
                    L['lug_boot'].isin(['small', 'med', 'big']) & \
                    L['safety'].isin(['low', 'med', 'high']) & \
                    L['acceptability'].isin(['unacc', 'acc', 'good', 'vgood'])
    
    print L.loc[L['valid']==False]

    return car_list

def writeCars(car_list):
    """ Writes the contents of the cars data frame into a csv file
    """
    root = Tkinter.Tk()
    root.withdraw()
    filename = tkFileDialog.asksaveasfilename(parent=root)

    try:
        car_list.to_csv(filename, index=False, columns = ['buying', 'maint', 'doors', 'persons', \
        'lug_boot', 'safety', 'acceptability'])        
        return filename
    except:
        print "Error while writing file... aborting..."

    
def getValidCars(car_list):
    """This function returns all valid cars"""

    L = car_list.copy()

    L['valid'] = L['buying'].isin(['low', 'med', 'high', 'vhigh']) & \
                    L['maint'].isin(['low', 'med', 'high', 'vhigh']) & \
                    L['doors'].isin(['2', '3', '4', '5more']) & \
                    L['persons'].isin(['2', '4', 'more']) & \
                    L['lug_boot'].isin(['small', 'med', 'big']) & \
                    L['safety'].isin(['low', 'med', 'high']) & \
                    L['acceptability'].isin(['unacc', 'acc', 'good', 'vgood'])
                    
    return L.loc[L['valid']==True]

def sortCars(car_list, var, asc, rows):
    """This function sorts the cars in ascending or descending order of the specified variable and 
        returns the top n or bottom n rows based on the sort order. If rows is zero, it returns all the rows.
        
        Usage: 
        sortCars(car_list, 'safety', False, -15 )
        sortCars(car_list, 'maint', True, 10 )
    """

    L = getValidCars(car_list)
    
    L['buying'] = pandas.Categorical(L['buying'], ['low', 'med', 'high', 'vhigh'])
    L['maint'] = pandas.Categorical(L['maint'], ['low', 'med', 'high', 'vhigh'])
    L['doors'] = pandas.Categorical(L['doors'], ['2', '3', '4', '5more'])
    L['persons'] = pandas.Categorical(L['persons'], ['2', '4', 'more'])
    L['lug_boot'] = pandas.Categorical(L['lug_boot'], ['small', 'med', 'big'])
    L['safety'] = pandas.Categorical(L['safety'], ['low', 'med', 'high'])
    L['acceptability'] = pandas.Categorical(L['acceptability'], ['unacc', 'acc', 'good', 'vgood'])

    try:

        if (rows > 0):
            return L.sort_values(var, ascending = asc).head(rows)
        else:
            if (rows < 0):
                return L.sort_values(var, ascending = asc).tail(abs(rows))
            else:
                if (rows == 0):
                    return L.sort_values(var, ascending = asc)
            

    except:
        print """ Error in parameters passed to sort function. The following are the parameters:\n
            var = Variable to be sorted by. Valid value is one of the following : 'buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'acceptability'
            asc = True or False depending on whether to sort in ascending or descending order respectively
            rows = any non-zero integer. If positive then top n rows will be returned. If negative then bottom n rows will be returned.
            
            Usage: 
            sortCars(car_list, 'safety', False, -15 )
            sortCars(car_list, 'maint', True, 10 )
        """            
        
def filterCars(car_list, var, pattern):
    """ This function filters the cars by checking if the contents of 'var' matches 'pattern'. 
        It will then return all rows that match this 'pattern'.
        
        Usage: 
        filterCars(car_list, 'buying', '^v?high$' )
    """
    L = getValidCars(car_list)   
    
    try:
        return L[L[var].str.match(pattern)]
    except:
        """ Error in parameters passed to filter function. The following are the parameters:\n
            var = Variable to be filtered by. Valid value is one of the following : 'buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'acceptability'
            pattern =  any valid python regex pattern
            
            Usage: 
            filterCars(car_list, 'buying', '^v?high$' )
        """            


if __name__ == "__main__":	
    
    cars = loadCars()

    #a. Print to the console the top 10 rows of the data sorted by 'safety' in descending order
    print "Bottom 15 Cars in descending order of Safety: \n" , sortCars(cars, 'safety', False, -15 )
    
    
    #b. Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order
    print "Top 10 Cars in ascending order of Maintenance: \n" , sortCars(cars, 'maint', True, 10 )
    
    
    #c. Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order.  Find these matches using regular expressions.
    pattern = '^v?high$'
    
    filter_buying = filterCars(cars, 'buying', pattern)
    filter_maint = filterCars(filter_buying, 'maint', pattern)
    filter_safety = filterCars(filter_maint, 'safety', pattern)
    sorted_cars = sortCars(filter_safety, 'doors', True, 0)

    # Another way to call the functions:
    # filtered_sorted_cars = sortCars(filterCars(filterCars(filterCars(cars, 'buying', pattern), 'maint', pattern), 'safety', pattern), 'doors', True, 0)
    
    print "All rows that are high or vhigh in fields \
    'buying', 'maint', and 'safety', sorted by 'doors' in ascending order", sorted_cars


    #d. Save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more.  The file path can be a hard-coded location (name it output.txt) or use a dialog box.

    filter_buying = filterCars(cars, 'buying', '^vhigh$')
    filter_maint = filterCars(filter_buying, 'maint', '^med$')
    filter_doors = filterCars(filter_maint, 'doors', '^4$')
    filter_persons = filterCars(filter_doors, 'persons', '4|more$')

    # Another way to call the functions:
    # filter_persons = filterCars(filterCars(filterCars(filterCars(cars, 'buying', '^vhigh$'), 'maint', '^med$'), 'doors', '^4$'), 'persons', '4|more$')

    print "Saved all rows that are that are: 'buying': vhigh, 'maint': med, 'doors': 4, \
            and 'persons': 4 or more. to file : ", writeCars(filter_persons)
    
