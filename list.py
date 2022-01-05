
#Dynamic input of numbers in a list and displaying their squares.
# number of elements



n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
#a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
#a=list(map(int,input("Enter numbers:").split()))[:n]
#[:n] That notation is referred to as slicing. Slicing allows you to create
# a new tuple, list, or string from an existing tuple/list/string by 
# specifying a start index, an end index,

#split()return the data as string or list
#strip()removes the improper spacing or characters in given input
a=list(map(int,input("Enter numbers:").strip().split()))[:n]
print("\nList is - ", a)
#square of number
b=list(map(lambda x:x*x, a))
print("\nSquare list is -",b)

