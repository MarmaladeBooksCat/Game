"""def increase_num():
    n = int(input ("Please insert a number "))
    x = int(input("Please inser another number "))
    if n == x or x == n:
        print ((n+x)*2)
    else:
        print (n+x)
increase_num()"""

# Create a function that gets change from money
# use ifs
# use modulos

def moneymoney():
    money = float(input("Please insert an amount of money. "))
    quarters = money/0.25
    remainder = money%0.25
    print ("Quarters: ",int(quarters))
    dimes = remainder/0.10
    remainder = remainder%0.10
    print ("Dimes: ",int(dimes))
    nickels = remainder/0.05
    remainder = remainder%0.05
    print ("Nickels: ",int(nickels))
    pennies = remainder/0.01
    remainder = remainder%0.01
    print ("Pennies: ",int(pennies))

moneymoney()
