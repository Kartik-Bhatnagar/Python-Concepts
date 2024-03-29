#Abstract method is used to hide the implementation details (in the base class)
#2) To enforce the abstract method , so that the methdod is compulsorly implemted by the derived class

from abc import ABC, abstractmethod

class BaseClass(ABC):
    #this is the base class , it can have concerte functions or a abstract function
    # a base class should have atleast one function with  @abstractmethod in order to call it a abstract class
    def concrete_fxn(self):
        print("this is a regular function, it is not necessary for the derived class to implement this function")

    @abstractmethod
    def abs_function(self):
        pass #we can't define this function logic here and it can be defined only at the derived class 
        #so in this way we can do ABSTRACTION, we hide the implemntation logic

class DerivedClass1(BaseClass):
    #we need to inherit the base class(with abstract method) in order to make child class 
    def d_func1(self):
        print("this is the function inside the child class")

    def abs_function(self):
        print("This function is derived from the parent class Base class and it is compoulasry to define this function here")

        print("the implementation of the function is defined here")
        
class DerivedClass2(BaseClass):
    #this is second base class
    def d_func2(self):
        print("this is the function inside the child class")
        
    def base_func(self):
        super().concrete_fxn()#using the base class function    
        print("the above was the function derived from the Parent( abstract class)")

    def abs_function(self):
        print("this function is in DerivedClass2")

        print("its logic can be different from the other dervied classes functions")        

print("We can't create a direct object of the Base class (which has abstract method ), we can create object only of the Derived/Child class")
#b1 = BaseClass() #this will throw an error
#b1.concrete_fxn()#we can't access the abstract class mehtods or attributes
d1 = DerivedClass1()
d1.abs_function()

d2 = DerivedClass2()
d2.d_func2()
d2.base_func()

