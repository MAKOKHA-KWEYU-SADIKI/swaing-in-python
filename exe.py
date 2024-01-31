#hello welcome back
import random
l=[]
pp=[]
class transactions:
    def __init__(self,pin,ballance):
        self.pin=pin
        self.ballance=ballance
        #self.no=no
    def __send(self):
        print("welcome to send money service") 
        num=int(input("enter number to continue: "))
        amt=int(input("enter amount: "))
        pinn=int(input("input pin"))
        if amt>self.ballance and pinn==self.pin:
            print("inssuffincient funds inn your account ")
        print(f"successful sent {amt} to {num} ")
        l.append(amt)
        pp.append(num)
        print(l,pp)
    def des(self):
        self.__send()    
    def withdraw(self):
        p=input("select\n1. From agent\n2. From ATM\n enter:")
        if  p=="1":
            print("welcome to withdrwal")
            agen=int(input("enter agent no: "))
            amt=int(input("enter ammount"))
            pinn=int(input("enter mpesa pin"))
            if amt<self.ballance and pinn==self.pin:
                 l.append(amt)
                 pp.append(agen)
                 print(f"succefull withdrawal of {amt} from {agen}")
            elif pinn!=self.pin:
                print("wrong Mpesa pin") 
            elif amt>self.ballance:
                print("inssufficient funds to withdraw")
        elif p=="2":
            print("sorry the service if currently unavailable please visit the nearest bank")
        else:
            print("invalid input")
    def deposite(self):
        print("welcome to deposite service")   
        p=int(input("1.proceed\n2.quit\ninput "))
        if p==1:
          print("give your relevant details to mpesa agent and the ammount")
        while p==2:
            print("goodbye")
            break         
    def buyairtime(self):
        inp=int(input("enter option\n1.own number\n2.other number"))
        if inp==1:
            ent=int(input("enter ammount: "))
            pin=int(input("enter mpesa pin"))
            if pin==self.pin and ent<self.ballance:
                print(f"successful bought worthy {ent}")
            elif pin!=self.pin:
                print("incorrect pin")
            elif ent>=self.ballance:
                print("inssuffincient funds")    
        elif inp==2:
            no=int(input("enter number: "))
            ent=int(input("enter ammount: "))
            pin=int(input("enter mpesa pin"))
            if pin==self.pin and ent<self.ballance:
                print(f"successful bought airtime of ammount {ent} to {no}")
            elif pin!=self.pin:
                print("incorrect pin")
            elif ent>=self.ballance:
                print("inssuffincient funds") 
        else:
            print("invalid input")      

class account(transactions):
    def __init__(self,pin,ballance):
         super(account,self).__init__(pin,ballance) 
    def acc(self):
        print("sorry for the inconviniences the suvice is currently unavailable")
    def bal(self):
        i=int(input("enter mpesa pin: "))
        if i==self.pin:
            print(f"account ballance is {self.ballance}") 
        else:
             print("invalid pin")     
class  loansSaving(transactions):
    def __init__(self,pin,ballance):
        super(loansSaving,self).__init__(pin,ballance)
    def sell(self):
            print("welcome to loans and savings account")
            inpu=int(input("1.Helb\n2.hef\n3.kcb\n4.hustler\n5.fuliza\n6.hakiki\n: "))
            if inpu==1 or inpu==2 or inpu==3 or inpu==4 or inpu==5 or inpu==6:
                print("services currently unavailable")
               # break
            else:# inpu!=1 or 2 or 3 or 4 or 5 or 6:
                print("invalid input")  


    #def min(self):
      #  print(pp,l)
      #  z=zip(l,pp)
       # for i in z:
class statement:
    def __init__(self,alp,num):
        self.alp=alp
        self.num=num 
        self.tc=0
        self.netTc()
    def rnd(self):
        i=random.choice(self.alp)+str(random.randint(self.num))
        print(i)         
def main():
 # f=statement()
  d=transactions(4545,500000)
  s=loansSaving(4545,45210)
  db=account(4545,45450000)

  while True:
    print("welcome to MPESA transactions \nand queries with beast servises as naver before")
    i=int(input("1.Send money\n2.withdraw cash\n3.deposite cash\n4.buy airtime\n5.loan and savings\n6.ballance inquiries\n7.my account\n9.quit\ninput  :"))
    if i==1:
       d.des()
    elif i==2:
       d.withdraw()
    elif i==3:
       d.deposite()    
    elif i==4:
       d.buyairtime()
    elif i==5:
       s.sell()
    elif i==6:
     db.bal()
    elif i==7:  
     db.acc()
    elif i==8: 
     f.rnd()
    elif i==9:
     print("Goodbye")
     break
if __name__ == "__main__":
    main()    