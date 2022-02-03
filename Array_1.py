from array import *
def Append_Array(array):

    array = array("i",[])
    elements = int(input("Enter the number of elements:  "))
    print("Enter ", elements, " elements")
    for i in range(0,elements):
        n = int(input())
        array.insert(0,n)
    print(array)

Append_Array(array)

