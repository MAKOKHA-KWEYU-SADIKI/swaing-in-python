#fuction that take two boolean balues as arguments
def sleepIn(weekday,vacation):
    print("this is sleepIn function")
    return not weekday and vacation
print(sleepIn(False,True))
def elaborate(false,true):
    if false==False or true==True:
        print("this is elaboration faction")
        return True
    else:
        return False
print(elaborate(True,False))
""""
given a string andd a non-negative integer n return a 
string n time string should be jointed
"""
def pract(strg,times):
    strg=strg*times
    return strg
print(pract("how do you do: ",5))    
#given a string name return hello name
# name=input("name: ")
# print(f"hello {name}")
def greatings(name):
    return f"hello {name}"
print(greatings("sadiki"))
#function to take the element in a list and returns true if the first or last element is 6

def ele(listtt):
    for i in listtt:
        if listtt[0]==6 or listtt[len(listtt)-1]==6:
            return True
        else:
            return False
print(ele([1,2,3,4,5,]))        
