'''
# Calculate exponents in the Python programming language
In mathematics, an exponent of a number says how many times that number is repeatedly multiplied with itself (Wikipedia, 2019). We usually express that operation as bn, where b is the base and n is the exponent or power. We often call that type of operation “b raised to the n-th power”, “b raised to the power of n”, or most briefly as “b to the n” (Wikipedia, 2019).

Python has three ways to exponentiate values:

The ** operator. To program 25 we do 2 ** 5.
The built-in pow() function. 23 coded becomes pow(2, 3).
The math.pow() function. To calculate 35, we do math.pow(3, 5).

'''


# square = []
# for x in range (10):
#     square.append(pow(x, 2))
# print(square)   #output >>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# square = []
# for x in range (10):
#   square.append(x **2)
# print(square)   #output >>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


'''

This can also be achieved using list comprehension
'''

# print([ x**2 for x in range (10)]) #output >>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# print([pow(x, 2)for x in range (10)]) #output >>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


'''
Example 2

Always know the inner loop runs the total number of times of the outer loop-in our case it runs 4 times

'''

# sales = []
# for x in [1, 2, 3, 4]:
#    for y in [3, 1, 4]:
#      if x !=y:
#         sales.append((x, y))
# print(sales)

'''
Above can be simplified with list comprehension

'''

#print([(x, y)for x in [1, 2, 3, 4] for y in [3, 1, 4]  if x !=y])


#output >>[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 3), (4, 1)]


'''
Nested list comprehension-A list with in a list

'''

hey= [
       [4, 5, 6],
       [3, 8, 9],
       [6, 7, 5]
  
  ]








#Multi-dimensional lists in Python



# Python program to demonstrate printing
# of complete multidimensional list
# a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
# print(a)
# #output >> [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]

'''

Approach 2: Accessing with the help of loop.

'''


# Python program to demonstrate printing
# of complete multidimensional list row
# by row.
# a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
# for record in a:
#     print(record)

'''
Approach 3: Accessing using square brackets.
Example:

'''
# Python program to demonstrate that we
# can access multidimensional list using
# square brackets
a = [ [2, 4, 6, 8 ], 
    [ 1, 3, 5, 7 ], 
    [ 8, 6, 4, 2 ], 
    [ 7, 5, 3, 1 ] ] 

#print(len(a))     #output 4      
for i in range(len(a)) : 
  for j in range(len(a[i])) : 
     print(a[i][j], end=" ")
  print()



'''
Creating a multidimensional list with all zeros:
# Python program to create a m x n matrix
# with all 0s

'''
# m = 4
# n = 5

# a = [[0 for x in range(n)] for x in range(m)]
# print(a)
# Output:
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

'''
1. append(): Adds an element at the end of the list.
Example:


# Adding a sublist

'''
  
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a.append([5, 10, 15, 20, 25])
print(a)

#Output: [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

'''
# Extending a sublist 
'''
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[0].extend([12, 14, 16, 18])
print(a)
#Output:  [[2, 4, 6, 8, 10, 12, 14, 16, 18], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]






'''
append: Appends object at the end.

x = [1, 2, 3]
x.append([4, 5])
print(x)
gives you: [1, 2, 3, [4, 5]]

extend: Extends list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print(x)
gives you: [1, 2, 3, 4, 5]


'''
'''

3. reverse(): Reverses the order of the list.
'''

# Reversing a sublist 
  
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[2].reverse()
print(a)
Output:
[[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [20, 16, 12, 8, 4]]                            