# Module 9 List Statistics Assignment
# Teresa Yu

#importing random module for random choiced numbers for lists
import random

#Take a list of floats and returns the lowest one
#example: lowestnum = [1.5, 4.1, 8.0, 10.06, 3.004] -> 1.5
#if the list is empty returns 0.0

# creating an empty list for floats
listFloat = []

# looping a random amount of times to determine the size of the list, has to be less than or equal to 10 
for i in range(random.randrange(10)):
  # adding a random float in between 1 and 10
  listFloat.append(random.uniform(1, 10))
#printing the final randomized float list for documentation
print(listFloat)

#if the list is empty, print a message saying so and 0.0
#if it's not empty, print a message indicating the smallest number
if len(listFloat) == 0:
  print('The list is empty, 0.0')
else:
  print("The smallest number in the list is", min(listFloat))


print('-'*80)
#Takes a list of integers and returns the product of all its even integers and the product of all the odd integers 
#example: evenProduct = [-1, 4, -6, 10, 3] -> -240
#example: oddProduct = [-1, 4, -6, 10, 3] -> -3

# initializing the needed lists of integers, even and odd numbers
listInt = []
even = []
odd = []

# determining a randomized size from 1 to 10 and values of the list consisting of integers from -10 to 10
for i in range(random.randrange(1,10)):
  listInt.append(random.randint(-10,10))
# printing the list for documentation
print(listInt)

# checking each number in the list to see if it is odd or even
# even numbers go in the even list, odd go in odd list
for number in listInt:
  if number % 2 == 0:
    even.append(number)
  else:
    odd.append(number)


product = 1
#if there are no odd or even numbers, print a message. there is no need to check if there is an empty list here
if len(odd) == 0:
  print("there are no odd numbers")
elif len(even) == 0:
  print("there are no even numbers")
#loop through each of the values in the even and odd lists find the product
else:
  for number in even:
    product *= number
  print('The product of the even numbers is:', product)
  
  product = 1
  for number in odd:
    product *= number
  print('The product of the odd numbers is:', product)



