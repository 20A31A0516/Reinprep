"""
#language translation
from translate import Translator
a=Translator(to_lang="Telugu")
b=a.translate("night")
print(b)
c=Translator(from_lang="telugu",to_lang="english")
d=c.translate("NENU")
print(d)
e=Translator(from_lang="english",to_lang="hindi")
f=e.translate("meher")
print(f)
"""


"""
method overlloading --- same fuc name but different signatures ,signatures are nothing but paremeters or arguments

"""


"""
class a:
    def m1(self,x,y,z):
        print(x*y*z)
class b(a):
    def m1(self,x,y):
        print(x*y)        
obj=b()
obj.m1(10,20,30)        
"""



"""
class animal:
    def speak(self):
        print("conveying something")
class dog(animal):
    def speak(self):
        print("bow bow")
class cat(animal):
    def speak(self):
       print("meow")
class cow(animal):
    def speak(self):
        print("mooo")
obj1=dog()
obj2=cat()
obj3=cow()
obj1.speak()      #method overriding"""




#abstraction
from abc import ABC,abstractmethod     #abc==abstract class  ABC==aBSTRACT BASE CLASS
class student(ABC):
    def write_exam(self):
        pass
class a(student):
    def write_exam(self):
        pass                   # writing body of function in diff class



#abstraction,abstract class ,abstasrt methods   ABC
#example of abstarction
#what is the use of abstract class
"""
class Area(ABC):
     @abstractmethod                              #annotations
     def calculate_area(self):
         print("calculating area")
class Square(Area):
    pass                                           # error in this case
class Rectangle(Area):
     pass     
obj=Square()
obj.calculate_area() 
"""



"""
class Area(ABC):
     @abstractmethod                              #annotations
     def calculate_area(self):
         pass
class Square(Area):
     def calculate_area(self):
         print("in square method")
class Rectangle(Area):
     pass     
obj=Square()
obj.calculate_area() 
        
 """ 



"""
class A(ABC):       # class a is abstarct class 
    @abstractmethod
    def f1(self):
        pass
    @abstractmethod      #defining abstract method
    def f2(self):
        pass       # no body in absract class
class B(A): #class B is child class of A and it should have body of functions defined in abstract class  
    def  f1(self):
        print("function1")
    def f1(self):
        print("f1-2")
    def f2(self):
        pass
obj=B()
obj.f1()    
obj.f2()
"""

"""

#shift operator
print(1<<2)              #16 8 4 2 1
                         #0 0 0 0 1        ---after left shift
                         #0 0 1 0 0----4
print(7<<3)      #shifting bitwise of 7 leftside 3 positions     
print(1>>2)  
print(11<<3)             #left shift multiply 11*2=22*2=44*2=88==answer
print(11>>3)             #11/2=5/2=2/2=1===answer


"""
#tic tac toe game program

