""" Number = 5 #var Number = 5 """

"""
addition = 77+ 49
print (addition)

subtraction = 77-49
print (subtraction)

multiplication = 7*14
print (multiplication)

division = 28/7
print (division)

expo = 2**8
print (expo)

modulo = 7%3
print (modulo)


mealCost =  45 
restaurant = 0.0675
tip = 0.15
meal = mealCost + (mealCost*restaurant)
final  = meal + (meal*tip)
print (final)


#These are strings, a series of letters.
name = "sophia"
food = "Drapple"
ship = "Wolflet"
marmalade = "HUNGRY"


number = 19 #int
number1 = 21.3 #float

# int x float  =  float
"""

"""
#indexes starts from 0, goes by letter in order when printing
a = "Dude" [0]
print (a)

n = "Marmalade" [6]
print (n)

"""
"""
cat = "CatsWithCatnip"
print (len(cat))
"""
"""
#some need parentheses and others need a period.

name = "LLAMA"
print (name.lower())
"""
"""
name = "llama"
print (name.upper())

#upper and lower only work on strings
#len works on lists, but upper and lower only works on strings

fruit = 'Drapple' + 'is' + 'Wonderful'
print (fruit)
#fruit1 = 'Tomato'
#fruit2 = '


#this is a string
number = 7
print (str(number))
"""
"""
name = "Marmer"
print ("You_want_some_food" %s %(name)
"""

""" name = input("What's your name? ")
print (name)
"""
       

# == checks if true
# != not equal
# < less than check
# > more than check
# <= less than or equal to
# >= more than or equal to

#value1: (20-10) >15
#value2: (10 + 17) == 3**16
#value3: (1**2) <= -1
#value4: 40*4 >= -4
#value5: 100 != 10**2

#1<2 and 2<3

#2<1 or 2<3

#and False makes a stement false

# false and false make a statement false.
# value2: -(-(-(-2))) == -2 and 4 >= 16**0.5

#with or, if one statement is right, the other one is too.

#not checks if both are false, if both are false, it is true, and two trues is false.
"""
if 10<9:
    print ("Eight is less than nine")
elif 5>6:
    print ("Five is less than six")
else:
    print ("I have a printer jam ;)")
"""

"""
TASK:
Ask the user to enter a valid word
check that it is a valid word
convert the word to pig latin
display the word
"""
#TASK
"""
ay = 'ay'

word = input("Please submit a word ")

if len(word) > 0:
    first = word[0]
    new_word = word + first + ay
    new_word = new_word[1:len(new_word)]
    print (new_word)
else:
    print("Please submit a word with more characters!")
    """

"""
def square(n):#prints a number's square
    print (n**2)
    return(n**2)
    square(21)
"""
"""
def cube(n):
    print (n**3)
    

def uncube (n):
    if(n%3) == 0:
        cube(n)
    else:
            print ("False")
cube(7)
uncube(7)

import math

print (math.sqrt(49))
"""
"""
maximum = max(1,2,3)
print (maximum)

minimum = min(1, 2, 3)
print(minimum)


absolute = abs(-78)
print(absolute)

print(type(24))
#the above prints what kind of thing is in the parentheses. ex. float, string, etc.
"""
"""
#TASK
#Create a function that calculates that cost for each city, each night is $150
#Create a function that returns the plane ride cost to go to each city.

def overnight_cost(n): # the variable 'n' is the number of nights
    #print (n*150)
    return(n*150)



def plane_cost(city):
    if city == "Toronto":
        return 183
    elif city == "Hamilton":
        return 220
    elif city == "Paris":
        return 222
    elif city == "Burlington":
        return 475
    elif city == "Artemisia":
        return 525
    elif city == "Hogsmeade":
        return 210
    elif city == "Rieux":
        return 175

plane= input ("What city are you travelling to?")
planecost = plane_cost(plane)

overnight = input ("How many nights are you staying?")
overnightcost = overnight_cost(overnight)

def car_rental(c):
    cost = c*40
    if c >= 7:
        cost = cost - 50
    elif c >= 3:
        cost = cost - 20
        
    return cost
car = input ("How many days are you renting a car for?")
carcost = car_rental(car)
    
def total_cost():
    totalcity = input ("Which city are you travelling to? ")
    if totalcity == "Toronto" or totalcity == "Hamilton" or totalcity == "Paris" or totalcity == "Burlington" or totalcity == "Artemisia" or totalcity == "Hogsmeade" or totalcity == "Rieux":
        totaldays = int(input ("How many nights are you staying? "))
        totalcost = overnight_cost(totaldays) + plane_cost(totalcity) + car_rental(totaldays)
        print(totalcost)

    else:
        totalcity = input ("Please enter a valid city.")
        total_cost()

total_cost()
"""

"""
total_cost("Toronto", 29)
total_cost("Paris", 3)
total_cost("Hamilton", 6)
total_cost("Burlington", 15)
"""

"""
numbers = [1, 2, 3, 4]
#This is a list

print(numbers[1] + numbers[3])
"""
"""
letters =  ["a", "b", "c"]

letters.append("d") #append is like adding
#print(letters)

#print(len(letters))

new_list = letters[1:3]
print (new_list)

#When slicing lists, add the index number that you want to include to the first one that you included.

letters[:2] #gets frist two items
letters[3:] #gets last four items
"""
"""
animals = ["owl", "cat", "bat"]
print(animals.index("bat"))

animals.insert(1, "ant")

animals.sort()
print(animals)
"""
"""
d = {'key1': 1, 'key2': 2, 'key3': 3}
print (d['key2'])
d['key3'] = 4
print(d['key3'])

del d['key3']
print (d)
"""
"""
numbers = [1, 2, 3, 4]
for number in numbers:
    number = number + 1
    print(number)
"""
"""
#TASK
#Create a list containing five numbers
#write a for loop that prints the square of each number
#sort the list

number_list = [3, 6, 4, 7, 14]
number_list.sort()
for number in number_list:
    number = number**2
    print(number)
"""
"""
numbers = [4, 7, 5, 9, 3]
numb = []
for num in numbers:
    numb.append(num**2)
    numb.sort()
    print(numb)
"""
"""
def printfirst(items):
    print (items[0])

numbers = (2, 4, 7,3)
printfirst(numbers)
"""

"""range(6)""" # This creates a list from 0 to the number that you put in #Creates a list with that many numbers
"""range(1,6)""" # goes from 1 to 6
"""range(1, 6, 1)""" # creates a list that skips every other number
"""
new_list = []
for item in list:
    print item

for item in range(len(list1)):
    print list[i]"""
"""
list_of_lists = [[1, 2, 3], [4, 5, 6]]
for list in list_of_lists:
    for item in list:
        print(item)
"""

board = []

for x in range(5):
    board.append(["0"] * 5)

def print_board(board):
    for row in board:
        print(*row, sep= ' ')#prints each row separately
print_board(board)

from random import randint

def random_row(board):
    return(randint(0,len(board)-1))

def random_col(board):
    return(randint(0,len(board[0]) - 1))

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

for turn in range(5):
    print (turn+1)
    
    guess_row = int( input("Guess a row from 0 to 4 "))
    guess_col = int(input("Guess a column from 0 to 4 "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You guessed correctly.")
        break
    else:
        if( guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4):
            print("Please enter valid coordinates")
        elif(board[guess_row][guess_col] == "X"):
            print("This was already guessed.")
        else:
            print("Incorrect guess.")
            board[guess_row][guess_col] = "X"
            print_board(board)

        if turn == 4:
            print("GAME OVER")











