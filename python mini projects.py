#  1st project

  class Bank:
     def __init__(self,acc_no,bal):
         self.acc_no=acc_no
         self.bal= bal

    def debited (self,amount):
         self.bal -= amount
         print("RS:", amount,"was credited")
         print("total balance :",self.bal)

      def credited(self,amount):
          self.bal += amount
          print("RS:", amount,"was credited")
          print("total balance:",self.bal)

  acc1= Bank(234565,55000)
  acc1.credited(4400)   
  acc1.debited(600)

 ## Q.NO 1

 print("hello lucky \nhow are you")

 #   Q.NO 2

  print("lucky chauhan, age =18 years old,city = patna city")

 ## Q.NO 3

a= float(input("entered the no:"))
b= float(input("entered the second no:"))
print("before swapping:","a=",a ,"b=",b)
a= a+b
b=a-b
a=b-a
print("after swapping:","a=",a ,"b=",b)



## Q.NO 4

 a= "lucky chauhan"
 b= 56
 c= 76.889
E= None

print(type(d))
print(type(c))
print(type(b))
print(type(a))
print(type(E))

# Q.NO 5 
def converter(celcius):
    return( (celcius * 9/5) +32)
print(converter(65))

x= int(input("entered the celcius to convert:"))
print("farenhite=",(x * 9/5) +32) 


 ## Q.NO 6 
X= input("enterd name:")     
y= input("enterd age:")  

print("hello",X,"you are",y ,"year old")

# // # Q.NO 7
x= int(input("lenght of rectangle:"))
y= int(input("breadth of rectangle:"))
print("perimeter of rectangle =", 2*(x+y))
print("AREA of rectangle =",x * y)


// # Q.NO 8
x= int(input("enterd no:"))

if(x >  0):
   print("positive")
elif( x < 0):
  print("negative")  
else:
   print("0")     

// ## Q.NO 9 
i = 1
while i <= 50:
    print(i)
    i += 1

for el in range (1,51,1):
    print(el)

 ### Q.NO 10
i= 0
while i <= 100:
    print(i)
    i +=2

for i in  range (0,101,2) :
    print("\n\n",i)  

# Q.NO 11
n= int(input("enterd a number:"))

print("sum using formula=", n*(n+1)/2)    

 ## Q.NO 12

n= int(input("entered the factorial:")) 
if n <0 :
    print("FACTORIAL DOES NOT DEFINE FOR  0 ANFD NEGATIVE VALUES:") 

else:
    factorial =1
    for i in range(1,n+1):
        factorial *= i
    print("FACTORIAL OF",n,"is:",factorial)
       
# Q.NO 13 

str= ["lucky","bholu","golu","34","45","rounak"]
str.reverse()
print(str)

Q.NO 14

str= "he is such a good boy i have ever met"
vowel= "aeiouAEIOU"
count= 0

for cha in str:
    if cha in vowel:
        count+= 1

print("number of vowelin the str:",vowel(str))        

# Q.NO 16

list=[34,65,89,90,100,76,43,12]
largest= max(list)

print("the largest number is :", largest)

# Q.NO 17
list=[34,65,89,90,100,76,43,12]
x= sum(list)

print("sum of all el in list is :", x)

# Q.NO 18
str= ["lucky","bholu","34","bholu","golu"]
str.remove("bholu")
print(str)
 
# Q.NO 19
list=[24,45,65,42,80,100,49,89]

for numb in list:
    if numb % 2 == 0:
        print(numb)

# Q.NO 20
n= int(input("entered the no:"))
def is_prime(n):
    if n<= 1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
    
if is_prime(n):
    print(n,"is a prime no.")

else:
    print(n,"is not a prime no.")

# Q,NO 21
n= int(input("enteered the no:"))
def squarenumber(n):
    return(n*n)

print(squarenumber(n))

# Q.NO 22
def count(sentence):
    return(len(sentence))

print(count("lucky chauhan is such a good coder in his entire village"))

#another type
def count(sentences):
    words= sentences.split()
    return len(words)

print(count("lucky chauhan is such a good coder in his entire village"))

# Q.NO 23
n= int(input("entered the following year:"))
if( n % 4 == 0):
    print("it is a leap year,thank you")

else:
    print("its not a leap year, thank you")    

# Q.NO 24
p= input("enterd the first no:")
q=  input("enterd the second no:")
r= input("enterd the third no:")

if( p >= q and p >= r):
    greatest =p
elif( q >= p and q >= r):
    greatest=  q
else:
    greatest = r     
print("the greatest no is :", greatest)

Q.NO 25
n= int(input("entered the no:"))
if( n % 3 == 0 and n % 5 == 0):
    print("yes its divisible")

else:
    print(" no its not divisible ")    









                                            # MINI PROJECT IN PYTHON #####

## PROJECT 1
### CALCULATOR
print("------><><>< SIMPLE CALCULATOR ------><>< 🧮🎉✔️🎲")
print("operators used in the calculators :+,-,*,/---><")

A= int(input("entered the first numbers:"))
B= int(input("entered the second number:"))
C=int(input("entered the second number:"))
opt= (input("ENTERED THE OPERATORS:"))

print("ADDTIONS OPERATOR \n\n")
if(opt == "+"):
    print("\n sum of two numbers:",A+ B + C )
    print(" SUBSTRACTIONS OPERATORS")
elif(opt == "-"):
    print("\nsubstraction of two numbers:\n\n",A- B - C)
    print("MULTIPLICATIONS OPERATORS:\n")
elif(opt == "*"):
    print("\nmultiPLICATIONNS OF TWO NUMBERS:\n\n",A * B * C)    
    print("\n DIVISIONS OPERATORS")
elif(opt == "/"):
    if(B != 0):
        print("division of two numbers:\n\n",A / B and B / C)
    else:
        print("error ocured as base is== 0 ❌❌❌")

else:
    print("cannot find the operation because of unidentified opterators❌❌:\n\n")

print("\n\n  ALL OPERATIONS DONE SUCCESFULLY :------><><><> ✔️🎉💕🤞😎")          

# PROJECT 2
# NUMBER GUESSING GAME

print("\n\n ------><> NUMBERS GUESSSINGS GAMES:------><><><🧮❤️🙌 ")
import random
print("\n\n WELCOME TO THE NUMBER GUESSING GANE-----><>< 🎲")

secret_numbert= random.randint(1,200)

attempt=0
guess= 0

while guess != secret_numbert:
    guess= int(input("entered your guess(1- 200):"))
    attempt += 1

    if guess > secret_numbert:
        print("TO HIGH ,TRY AGAIN NOW:\n\n")
    elif guess < secret_numbert :
        print(" \n TO LOW ,TRY AGAIN NOW:\n")
    else:
      print("\n CONGRATULATION YOU GUESSD IT RIGHT🎉🎉✔️❤️",attempt)    

# PROJECT 3
# PASSWORD_GENERATOR

import random
import string

print("Welcome to the password generator world!")

def simple_password(length):
    characters = string.ascii_letters + string.digits   # notice it's characters not character
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated Password:", simple_password(100))


PROJECT 2
GRAPHICS IN LIBRARY
from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h=0
for i in range(100):
    color(hsv_to_rgb(h,1,1))
    h+=0.014
    left(1)
    forward(1)
    for j in range(3):
        left(2)
        circle(160)
        hideturtle()
done()


## PROJECT 3
# HYPONOTIC CIRCLES
from turtle import *
import colorsys

bgcolor("black")
speed(0)
h= 0
for i in range(100):
    c= colorsys.hsv_to_rgb(h,1,1)
    color(c)
    circle(100 + i*5)
    h += 0.02
    left(15)

done()    

# PROJECT 4
# STAR BURST

from turtle import *
import colorsys

bgcolor("black")
speed(0)
h= 0

for i in range(600):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    forward( i*2)
    left(150)
    h += 0.005

done()   

## PROJECT 5
## RED CURVE

import turtle
t= turtle.Turtle()
screen= turtle.Screen()
screen.bgcolor("black")
t.speed(4)

colors= ["red","dark red"]
screen.tracer(3)

for number in range(400):
    t.forward(number+1)
    t.right(89)
    t.pencolor(colors[number%2])

screen.update()
turtle.done()    

# PROJECT 6

from turtle import*
import colorsys
bgcolor ("black")
tracer(500)

def draw():
    h= 0
    for i in range(100):
        c= colorsys.hsv_to_rgb(h,1,1)
        h+= 0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor(c)
        begin_fill()
        rt(98)
        circle(i,12)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j,299,steps=2)
        end_fill()
draw()
done()

# PROJECT 7
# COLOURFUL SPIRAL

from turtle import*
import colorsys
bgcolor("black")
tracer(2)
pensize(4)
h=0
for i in range(300):
    c= colorsys.hsv_to_rgb(h,1,1)
    color(c)
    forward(i*2)
    left(59)
    h += 0.005
done()    

# PROJECT 8
#RAINBOW HEXAGON Pattern

from turtle import*
import colorsys

speed(0)
h=0
bgcolor("black")

for i in range(300):
    c= colorsys.hsv_to_rgb(h,1,1)
    color(c)
    circle(150)
    left(10)
    h += 0.005

done()    


