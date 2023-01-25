""" Arrays 1D,2D,3D  pixels,picture,resolution of images where multi dimensional matrices are used
a1=[1,2,3]
a2=[[1,2],[3,4]]
"""





"""
row=2
col=2
arr=[]
for i in range(row):
    ele=[]
    for j in range(col):
        ele.append(int(input()))
    arr.append(ele) 
print(arr)    
        """
"""
#addition of 2 matrices
a=[[1,1],[2,2]]
b=[[3,3],[4,4]]
c=[]
for i in range(len(a)):
    d=[]
    for j in range(len(a)):
        ele=a[i][j]+b[i][j]
        d.append(ele)
    c.append(d)
   
print(c)  




#taking arrays as inputs
arr1=[]
arr2=[]
row=2
col=2
for i in range(row):
    temp=input().split()
    ele=list(map(int,temp)) 
    arr1.append(ele) 
for i in range(row):
    temp=input().split()
    ele=list(map(int,temp)) 
    arr2.append(ele)    
res=[[0 for j in range(col)] for i in range(row)]   
print(arr1)
print(arr2)
for i in range(row):
    for j in range(col):
        res[i][j]=arr1[i][j]+arr2[i][j]
print(res)
"""
#datastructures 2d arrays


# doing transpose of matrix 3*3----> 7 more similar problems


"""
#slicing
l=[1,2,3,4,5,6,7,8,9,10]
print(l)
print(l[0:5])
print(l[0:10:2])
print(l[:])
print(l[1:])
print(l[:5])
print(l[::-1])
"""
#negative indexing only in python
#fibonacci series   0 1 1 2 3 5 8 ........
# generate a fibonacci series until 25, generate sequnce up to 25 elememts in the series (while loop)
l=[0,1]
while len(l)<25:
    l.append(l[-1]+l[-2])
print(l)
print(len(l))    


#fibonacci series without list 
    

    