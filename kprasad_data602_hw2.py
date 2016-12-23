#1. fill in this class
#   it will need to provide for what happens below in the
#	main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
# 	a function called showEvaluation, and an attribute carCount

class CarEvaluation:
    'A simple class that represents a car evaluation'
    #all your logic here
    
    carCount = 0
    
    def __init__(self, Brand, Price, Safety):
        self.Brand = Brand
        self.Price = Price
        self.Safety = Safety
        
        CarEvaluation.carCount += 1
        
    def showEvaluation(self):
        print "The ", self.Brand, " has a ", self.Price, " price and it's safety is rated a ", self.Safety


#    def __lt__(self, other):
#        if(self.Price == "Low"):
#            return 1
#        else:
#            if (self.Price == "High"):
#                return 0
#            else:
#                if(self.Price=="Medium" and other.Price=="High"):
#                    return 1
#                else:
#                    if(self.Price == "Medium" and other.Price=="Low"):
#                        return 0
                
            
#2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
# 	otherwise by descending price

def sortbyprice(L, order): #you fill in the rest
    sorted_list = L[:]
    for i in range(0, len(L) - 1, 1):
        for j in range(i, len(L), 1):
            if(sorted_list[i].Price == "Low"):
                pass
            else:
                if (sorted_list[i].Price == "Med" and sorted_list[j] == "High"):
                    pass
                else:
                    if(sorted_list[i].Price=="Med" and sorted_list[j].Price=="Low"):
                        sorted_list[j], sorted_list[i] = sorted_list[i], sorted_list[j]
                    else:
                        if(sorted_list[i].Price == "High"):
                            sorted_list[j], sorted_list[i] = sorted_list[i], sorted_list[j]

    brand_list = [cars.Brand for cars in sorted_list]

    if(order == "des"):
        brand_list.reverse()

    #return a value
    return brand_list
        

#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#	it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false
def searchforsafety(L, safety_rating): #you fill in the rest
    safety_list = [cars.Safety for cars in L]
    if safety_rating in safety_list:
        return 'TRUE'
    return 'FALSE'


	
# This is the main of the program.  Expected outputs are in comments after the function calls.



if __name__ == "__main__":	

#    import sys
#    this_module = sys.modules[__name__]
#    my_class = this_module.__dict__['CarEvaluation']
#    eval1 = my_class("Ford", "High", 2)
#    eval2 = my_class("GMC", "Med", 4)
#    eval3 = my_class("Toyota", "Low", 3)
#    print "Car Count = %d" % my_class.carCount # Car Count = 3
#    method="showEvaluation"
#    eval1show = getattr(eval1,method)
#    eval1show() #The Ford has a High price and it's safety is rated a 2
#    eval2show = getattr(eval2,method)
#    eval2show() #The GMC has a Med price and it's safety is rated a 4
#    eval3show = getattr(eval3,method)
#    eval3show() #The Toyota has a Low price and it's safety is rated a 3

    
   eval1 = globals()['CarEvaluation']("Ford", "High", 2)
   eval2 = globals()['CarEvaluation']("GMC", "Med", 4)
   eval3 = globals()['CarEvaluation']("Toyota", "Low", 3)
#   eval4 = CarEvaluation("Honda", "Med", 2)
#   eval5 = CarEvaluation("BMW", "High", 4)
#   eval6 = CarEvaluation("Hyundai", "Low", 3)

   print "Car Count = %d" % getattr(CarEvaluation, 'carCount') # Car Count = 3

   getattr(eval1, 'showEvaluation')() #The Ford has a High price and it's safety is rated a 2
   getattr(eval2, 'showEvaluation')() #The GMC has a Med price and it's safety is rated a 4
   getattr(eval3, 'showEvaluation')() #The Toyota has a Low price and it's safety is rated a 3

   L = [eval1, eval2, eval3]

#   L = [eval1, eval2, eval3, eval4, eval5, eval6]
#
   print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
   print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
   print searchforsafety(L, 2); #true
   print searchforsafety(L, 1); #false