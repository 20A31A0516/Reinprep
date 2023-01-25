

d={ 1:"aisshwarya",2:"divya",3:"latha"
   }
print(d[1])
print(d[2])
print(d[3])
print(d.get(1))
d.update({4:"sri"})
print(d)

d={ 1:"aisshwarya",2:"divya",3:"latha"}
l=list(d.keys())
print(l)
l2=[]
for i in range(len(l)):
    l2.append(d[l[i]])
print(l2)    


for i in d:
    print(i) # we will get keys
    print(d[i]) # we will get values
    
d1={1:'a',2:'b'}
d2={1:'c',2:'d'}
d3={1:'e',2:'f'}
d4={1:'g',2:'h'}
d5={1:'i',2:'j'}
l=[]
l.append(d1)
l.append(d2)
l.append(d3)
l.append(d4)
l.append(d5)
print(l)  

#taking user inputs in ductonary
d={}
for i in range(1,6):
    names=input()
    values=int(input())
    d[names]=values
print(d)    

l=[]
for i in range(2):
    d={
       'key1':input('enter key 1:'),
       'key2':input('enter key2:')}
    l.append(d)
print(l)


l=[]
d={}
for i in range(2):
    d.update({'key1':input('enter key 1:'),
    'key2':input('enter key2:'})                   # key1:100 key1 :100 why? reference variable is same
    l.append(d)
print(l)    
# to avoid the above
l=[]
d={}
for i in range(2):
    d.update({'key1':input('enter key 1:'),
    'key2':input('enter key2:'})                   
    l.append(d)
print(l)


#code refactoring

#login management system small project using python



#check whether password is correct or wrong for a particular user
l.keys()
l.values()
l.items()   #tuple #json"""
d=[
   {'a':1},{'b':2},{'c':3},{'d':4}]
un=input()
pa=int(input())
temp={
      un:pa}
if temp in d:
    print("Found")
else:
    print("Not found")    
    
#signup or registration program  add username and passwords into existing list    
    
     
