#swapping two variable
v1=12
v2=21
temp=v1
v1=v2
v2=temp
print(v1,v2) 
#l=[]
total=0
a=[10,2,3,4,5,6,7,8,9,1]
#l.append(a)
# print(l)
# temp=a[0]
# a[0]=a[9]
# a[9]=temp
a[0],a[9]=a[9],a[0]
#print(sum(a))
print(a)
for i in a:
     if i==10:
         continue
     total=total+i
   
print(total)    
# temp=l[0]
# l[0]=l[9]
# l[9]=[temp] 
#print(l)