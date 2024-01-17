#mro will help in determine  the order in which the method and attributes will be accessed to an object of a class 
#it will be helpful if the classes and inheritance get complex, then mro will give us the order in which the methods or attributes will be called

"""In python, method resolution order defines the order in which the base classes are searched when executing a method.
 First, the method or attribute is searched  within a class and then it follows the order we specified while inheriting.
This order is also called Linearization of a class and set of rules are called MRO(Method Resolution Order).
While inheriting from another class, the interpreter needs a way to resolve the methods that are being called via an instance.
Thus we need the method resolution order. """

class A:
    value = "A class"

    def d(self):
        return "Function inside A"

class B:
    value = "B class"
    def d(self):
        return "Function inside B"


class C:
    value ="c class"
    def d(self):
        return "Function inside C"


class D(A, B):
    value = "d class"
    def d(self):
        return "Function inside D"


class E(B, C):
    value = "e class"
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro()) #E D A B C 
print(F.value)

d = D()
print(d.value)

print(help(d))
