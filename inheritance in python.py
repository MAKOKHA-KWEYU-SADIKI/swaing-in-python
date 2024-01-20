#all type of inheritance in one program for the beginner
class operation :
    def addition(sef,a,b):
        return a+b
class mult(operation):
    def multipl(self,a,b):
        return a*b
o=mult()
print(o.addition(10,10))       
print(o.multipl(10,10))
#multilevel inheritace in python
class numbers:
    def intergers(self,num):
        return f"{num} this is an integer"
class positiveNumbers(numbers):
    def positive(sef,num):
        return f"{num} this is a positive integer"
class greaterthanTen(positiveNumbers):
    def greatChek(self,args):
        if args>10:
            print("the number is greater than ten")
        else:
            print("number is less than ten")
        return args
obj=greaterthanTen()
print(obj.intergers(100))
print(obj.positive(10))
print(obj.greatChek(90))
#this is cool
#two more types
#multiple inheritance
class animals:
    def p(self):
      print("animals eat")
class animalia:
    def h(self):
        print("they also do eat") 
class mamalia(animalia,animals):
    def child(self):
        print("inherits from animalia and animals")
ob=mamalia()
ob.p() 
ob.h()
ob.child()                   
#this is the last type of inheritance
#haerachical inheritance
class animal:
    def p1(self,two,tree):
        return two,tree
class reptiles(animal):
    def c2(self,example):
        return example
class mamals(animal):
    def c1(self,example):
        return example
b=mamals()
f=reptiles()
print(b.p1("man","fish"))
print(f.c2("snake"))
print(b.c1("child"))   
print(f.p1("frog","lions"))          
