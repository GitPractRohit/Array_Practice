'''
############################# Basics of Array ##############################################################
'''
# we have one difference between list and array in python is "In python array contains the same data type"
# We have TypeCode for making the array in python which will be available online.
from array import *
# import array as arr
# Vals = array('i',[5,8,9,4,3,12,45,88])  # i stands for integer

# If we dont know the data type of an array which means we outsource the data although we dont know the values as well

# NewArray = array(Vals.typecode, (a for a in Vals))

# NewArray = array(Vals.typecode, (a*a for a in Vals)) # if we need square of the present vales
'''
for i in NewArray:
    print(i)
'''
'''
# Doing same with the while loop for this we need to check three coditions
    1] Initialization
    2] Check for the Condition
    3] we have to do Incrementy decrement by ourself
'''
'''
i = 0
while i<len(NewArray):   # I dont know the lenth of the array
    print(NewArray[i])
    i+=1
'''

'''
print(Vals)
print(Vals.buffer_info())   # (1946392750736, 8) 1946392750736---this is address of this array and 8 --- Size
print(Vals.typecode)
Vals.reverse()        # we can reverse the entire array
print(Vals)
print(Vals[0])
print(Vals[0:5])
print(Vals[4:5])  # getting only number 3 from the array

'''
'''
# Printing all the array at once using for loop because we know the range of the array

# for i in range(8):
 #   print(Vals[i])
# Another way to write the same code
for i in Vals:
    print(i)
'''

'''
# If we dent kown the lent of array then we go with

for i in range(len(Vals)):
    print(Vals[i])
'''

'''
######################################################################################################################## 
Taking the input from user then convert it in the Array which means we take the values from the user in the form of Array
'''

Array = array('i',[])

N = int(input("Please enter the value : "))  # how many values do we need in the array

for i in range(N):
    x = int(input("Please next enter the value : "))
    Array.append(x)

print(Array)

Val = int(input("enter the value for the search : "))
k = 0
for e in Array:
    if e == Val:
        print(k)
        break
    k+=1