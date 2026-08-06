#  1st project
#                 MAKING A BANK CLASS USING OOPS WHERE WE SEE SUDDEN CHNAGE WHEN WE CREDIT OR DEBIT SOME AMOUNT .
  class Bank:
     def __init__(self,acc_no,bal):
         self.acc_no=acc_no
         self.bal= bal

    def debited (self,amount):
         self.bal -= amount
         print("RS:", amount,"was debited")
         print("total balance :",self.bal)

      def credited(self,amount):
          self.bal += amount
          print("RS:", amount,"was credited")
          print("total balance:",self.bal)

  acc1= Bank(234565,55000)
  acc1.credited(4400)   
  acc1.debited(600)


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

# ALTERNATIVE 
# ADVANCED CALCULATOR USING SAME SYNTAX BUT BIT COMPLEX USE OF CONDITIONALS .

print("><><><>\n WELCOME TO ADVANCED CALCULATORS  ><><><> \n")
a = int(input("ENTERD THE FIRST NO :"))
opt1 = input("ENTERD THE FIRST OPERATOR =")
b = int(input("ENTERD THE SECOND NO ="))
opt2 = input("ENTERD THE OPERATOR 2 = ")
c = int(input(" ENTERD THE THIRD NO : "))

if (opt1 == "+" and opt2 == "+"):
    print("ADDITION OF ALL THE THREE NO =\n", a + b + c)
elif ( opt1 == "+" and opt2 == "-"):
    print("ADDITION AND SUBSTRACTION OF THREE NO = \n", a + b - c)
elif( opt1 == "+" and opt2 == "*"):
    print(" ADDITION AND MULTIPLICATIONS OF THREE NO IS = \n", a + b * c)
elif ( opt1 == "+" and opt2 == "/"):
    if( c != 0):
        print(" ADDITION AND DIVISION OF THREE NO IS = \n", a + b / c)
    else :
        print(" VALUE OF BASE  C IS 0 SO CANT DEFINED")
elif (opt1 == "-"  and opt2 == "+"):
    print(" SUBSTRACTION AND ADDITION OF THREE NO =\n", a - b + c)
elif( opt1 == "-" and opt2 == "-"):
    print("SUBSTARCTION AND SUBSTRACTION OF THREE NO IS =\n", a - b - c)
elif(opt1 == "-" and opt2 == "*"):
    print(" SUBSTRACTION AND MULTIPLICATION OF THREE NO IS = \n", a - b * c)
elif( opt1 == "-" and opt2 == "/"):
    if( c != 0):
        print("SUBSTRACTION AND DIVISION OF THREE NO IS = \n ", a - b / c)
    else:
        print("VALUE OF BASE  C IS 0 SO CANT DEFINED")
elif (opt1 == "*" and opt2 == "+"):
    print("MULTIPLICATION AND ADDITION OF THREE NO IS = \n", a * b + c)
elif( opt1 == "*" and opt2 == "-"):
    print("MULTIPLICATIONS AND SUBSTRACTION OF THREE NON IS = \n", a * b - c)
elif (opt1 == "*" and opt2 == "*"):
    print("MULTIPLICATION OF THREE NO IS =\n", a * b * c)
elif( opt1 == "*" and opt2 == "/"):
    if( c != 0):
        print("MULTIPLICATION AND DIVISION OPF THREE NO = \n", a * b / c)
    else :
        print("VALUE OF BASE IS 0 SO CANT DEFINED")
elif( opt1 == "/" and opt2 == "+"):
    if ( b != 0):
        print("DIVISION AND ADDITION OF THREE NO IS = \n", a / b + c)
    else:
        print("VALUE OF BASE IS 0 SO CANT DEFINED")
elif (opt1 == "/" and opt2 == "-"):
    if ( b != 0):
        print("DIVISION AND SUBSTRACTION OF THREE NO IS = \n", a / b - c)
    else:
        print("VALUE OF BASE IS 0 SO CANT DEFINED")
elif( opt1 == "/" and opt2 == "*"):
    if ( b != 0):
        print("DIVISION AND MULTIPLIVCATION OF THREE NO IS = \n", a / b - c)
    else:
        print("VALUE OF BASE IS 0 SO CANT DEFINED")
elif(opt1 == "/" and opt2 == "/"):
    if( b != 0 and c != 0):
        print(" DIVISION OF ALL THREE NO IS = \n", a / b / c)
else :
    print("| OPERATORS MISMATCH DUE TO ANOTHER OPERATOR USED")
print("><><><> | ALL THE OPERATIONS EXECUTED SUCCESFULLY ><><> | /\n")

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


# PROJECT 2
# GRAPHICS IN LIBRARY
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

#    PROJECTS 7 . 
#    MAKING QRCODE OF ANY TEXT OR URL AND SAVING IN PNG.FILES USING PYTHON .

import qrcode

text = input("ENTER THE TEXT OR URL FOR QR")

qr = qrcode.make(text)

filename = "USER.png"

qr.save(filename)

print("QRCODE SAVE AS FILENAME = ",filename)








