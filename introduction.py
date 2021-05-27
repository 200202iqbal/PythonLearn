for i in range(1,10):
    print(i)
    if i == 5:
        break

#cara membuat docstring di python
def double(num):
    """Function to double the value"""
    return 2*num

num = 5
print(num,"double is , ",double(num))
#cara memunculkan docstring di python
print(double.__doc__)

#mendeklarasikan dan memberikan nilai variabel
website = "google.com"
print(website)

#mendeklarasikan dan memberikan nilai ke variabel secara multiple
a,b,c = 5,3.2,"Hello"
print(a,b,c)

#mendeklarasikan dan memberikan nilai yang sama ke variabel yang berbeda
a=b=c = "same"
print(a,b,c)

#constant
import constant as ct
print("PI = ",ct.PI)
print("Gravity = ",ct.GRAVITY)

#decimal
import decimal as dc
print(0.1)
print(dc.Decimal(0.1))

from decimal import Decimal as dc
print(dc('1.1') + dc('2.2'))
print(dc('2.5') * dc('3'))

#fraction
import fractions
#merubah angka float menjadi pecahan
s = type(fractions.Fraction(1.5))
print(fractions.Fraction(1.5))
print(s)
#merubah ke bentuk pecahan. hasilnya 1/25
print(fractions.Fraction(1,25))

#random
import random
#memunculkan nilai random dari range 10 sampai 20
# random.randrange(stop)
# random.randrange(start, stop[, step])
print(random.randrange(10,20))
x = ["a","b","c","d","e"]

#Mendapatkan random choice
i = 0
while i < 5:
# random.choice(seq)
# Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.    
    print(random.choice(x))
    i += 1

# random.shuffle(x[, random])
# Shuffle the sequence x in place.
random.shuffle(x)

#print random element
print(random.random())

drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

#collection
fruits = ["apple","mango","orange"] #list
numbers = (1,2,3) #tuple
aplhabets = {"a":"apple","b":"ball","c":"cat"} #dictionary
vowel = ("a","i","u","o","e") #set

print(fruits)
print(numbers)
print(aplhabets)
print(vowel)

#print
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# Here, objects is the value(s) to be printed.
# The sep separator is used between the values. It defaults into a space character.
# After all values are printed, end is printed. It defaults into a new line.

print(1,2,3,4)
print(1,2,3,4,sep="#")
print(1,2,3,4,sep="#",end="end\n")

#output formatting
x = 5
y = 10
print("The value of x is {} and y is {}".format(x,y))
print("I love {0} and {1}".format("bread","butter"))
print("I love {1} and {0}".format("bread","butter"))

x = 12.3456789
print("The value of x is %3.2f" %x)
print("The value of x is %3.4f" %x)

# Identity operators
# is and is not are the identity operators in Python. 
# They are used to check if two values (or variables) are located on the same part of the memory. 
# Two variables that are equal does not imply that they are identical.

# is	True if the operands are identical (refer to the same object)	x is True
# is not	True if the operands are not identical (do not refer to the same object)



