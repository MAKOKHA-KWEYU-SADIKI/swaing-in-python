#this is polymophism
#ducktyping
class birds:
    def fly(self):
        print("birds do fly")
    def walk(self):
        print("birds do walk")
class animals:
    def walk(self):
        print("they do walk")
        print("all birds are animals")
    def fly(self):
         print("birds do fly")    
def duck(duk):
    duk.walk()
    duk.fly()
    print("this is polymophism")
d=birds()
duck(d)                        
s=animals()
duck(s)