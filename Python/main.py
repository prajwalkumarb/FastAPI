#assignment_1
'''Write a Python program that can do the following:
- You have $50
- You buy an item that is $15, that has a 3% tax
- Using the print()  Print how much money you have left, after purchasing the item.'''
#M1
# initial_amount = 50
# final_amount=initial_amount-15-((15)*(3/100))
# print(final_amount)

#M2
# money=50
# price=15
# tax=3/100
#
# final_amount=money-price-tax
# print(final_amount)

#==================================================================================================
#Assignment_2
'''
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)
- Ask the user how many days until their birthday
- Using the print()function. Print an approx. number of weeks until their birthday
- 1 week is = to 7 days.'''

# days=int(input("enter how many days until your birthday"))
# week=round(days/7)
# print(f"{week} week left for the Bday")

#=======================================================================================================

#Assignment_3

'''
Lists Assignment
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals'''

# zoo=['lion','tiger','zebra','orangutan','deer']
# zoo.pop(2)
# zoo.append("Rabbit")
# zoo.pop(0)
# print(zoo)
# print(zoo[0:3])

#========================================================================================

#Assignment_4

'''
If Else Assignment
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable
Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59'''

# grade=int(input("Enter the marks"))
# if grade>=90 and grade<=100:
#     print("A")
# elif grade>=80 and grade<=89:
#     print("B")
# elif grade>=70 and grade<=79:
#     print("C")
# elif grade>=60 and grade<=69:
#     print("D")
# elif grade>=0 and grade<=59:
#     print("F")
# else:
#     print("enter the valid Marks")

#=================================================================================================
#Assignment_5

'''
Loops Assignment
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all elements of the my_list variable 3 times.
- When printing the elements, use a for loop to print the elements
- However, if the element of the for loop is equal to Monday, continue without printing'''

# my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# count=0
# while count<3:
#     count+=1
#     for i in my_list:
#         if i=="Monday":
#             continue
#         else:
#             print(i)
#     print()
#=====================================================================================================

#Assignment_6

'''
Dictionaries Assignment
Based on the dictionary:
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values
- Create a new variable vehicle2, which is a copy of my_vehicle
- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- Delete the mileage key and value from vehicle2
- Print just the keys from vehicle2'''

# my_vehicle = {
#     "model": "Ford",
#     "make": "Explorer",
#     "year": 2018,
#     "mileage": 40000
# }
#
# for i,j in my_vehicle.items():
#     print(i,j)
# variable2=my_vehicle.copy()
# variable2["number_of_tires"]=4
# variable2.pop("mileage")
# print()
# for i in variable2:
#     print(i)

#========================================================================================

#Assignment_7

'''
Functions Assignment
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values'''

def my_details(firstname, lastname, age):
    dect = {'Firstname':firstname,'lastname':lastname,'age':age}
    print(dect)
my_details("Prajwal","Kumar",21)