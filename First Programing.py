
##                                               PYTHON FIRST PROGRAMMING                    
#                                            1.  INPUT FUNCTIONS // ATTRIBUTES                  

# q=input("first no:")
# z=input("second no:")
# def sum (q,z):
#     return q+z
# print(sum(q,z))

# a= 1
# B="3"
# print("sum:",a+float(B))

# A= int(input("entered first number:"))
# B= int(input("entered second number:"))

# print("sum of both numbers:",A+B)
# print("AVERAGE OF BOTH NO :",A+B/2)
# if("A+B/2=", 4):
#    print("TRUE VALUES OF AVERAGE")
# else:
#    print("NOT FOUND THE REAL VALUES")

# A= int(input("SIDES OF THE SQUARES :"))
# print("sides of the squares :",A*A)
# if("SIDES OF THE THE SQUARES=",25):
#     print("hence true values ")
# else:
#     print("falses values ")

# a= float(input("entered the first no:"))
# b= float(input("entered the second no:"))
# print("average of two no:",(a + b) / 2)

# X=int(input("entered the 1st no:"))
# V= int(input("entered the second no:\n"))
# if(X >= V):
#     print("TRUE")
# else:
#     print("FALSE")

# str= "lucky chauhan"
# print(str[7])
# print(len(str))
# print(type(str))
# print(str[:])

# str= input("entered the sentence:")
# print(str)
# print(str.endswith("anythings"))
# print(str.capitalize())
# print(str.replace("is","was"))
# print(str.find("is"))
# print(str.count("is"))

# a= input("users name :")
# print(len(a))

# q= "hello everyone my self lucky chauhan $ today i am here to start $ my introduction $"
# print(q.count("$"))

                                    ## CONDITIOAL STATEMENT [ IF,ELSE,ELIF]                        

# LIGHT= input("entere the light color:")
# if(LIGHT=="red"):
#     print("stop the vehichles")
# elif(LIGHT=="yellow"):
#     print("you can wait for some min ")
# elif(LIGHT== "green "):
#     print("you can go")
# else:
#     print("light is broken")


# marks= 98

# if(marks >= 90):
#     print("grade A")
# elif(marks >= 80 and marks <90 ):
#     print("grade B")
# elif( marks >= 70 and marks <80):
#     print("grade C")  

# else:
#     print("grade D")      

# Q.NO 1 
# NO= int(input("no entered by the users:"))
# if(NO % 2 == 0):
#     print("no is even")
# else:
#     print("no is odd")

## Q.NO 2 
# A= int(input("entered the 1st no:"))
# B=int(input("entered the 2nd no:"))
# C=int(input("entered the 3rd no:"))
# if(A> B and A > C):
#     print("GRETEST=",A)
# elif(B > C and B > A):
#     print("GRETEST:",B)
# elif(C > A and C > B ):
#     print("GREATEST=",C)
# else:
#     print("wrong eternity done by the user")

# Q.NO 3
# X = int(input("entered the no:"))
   
# if(X % 7 == 0):
#     print("it is multiple of 7")

# else:
#     print("not multiple of 7")   

                                        # THE list ######

# marks =[67, 65, 54, 78,56,32,65,"lucky","bholu"]
# print(marks[:8])

# x= [34,87,98,90,65,67,66,32,21,30]
# x.append(66)
# x.sort()
# x.sort(reverse=True)
# x.reverse()
# x.insert(5,"bholu")
# x.remove(87)  
# x.pop(7)
# print(x)
# print(len(x))
                                        #THE TUPLES #

# A=(56,67,89,52,"lucky",67)
# b= (98,87,56,"bholu")
# print(A.count(67))
# print(A.index(67))
# print(A.__add__(b))

   #Q. NO 1
# movies = []
# a = input("first movie :")
# movies.append(a)
# b= input("second movie :")
# movies.append(b)
# c=  input("third movie :")
# movies.append(c)
# print(movies)

# Q. NO 2
# list= ["c","d","a","b","a","a"]
# list.sort()
# print(list)

                                    # dictionary#

# dict={
#     "name":"lucky",
#     "marks": [89,98,67,65,34],
#     "cgpa" : 9.9 ,
# }  
# # print(dict["cgpa"])
# # print(dict.keys())
# # print(dict.items())
# # print(dict.values())
# (dict.update({"school": "apna school"}))
# print(dict)

                                #  SETS ##

# X={67,89,87,67,99,100,"lucky","bholu"}
# X.add(98)
# X.remove("lucky")
# X.pop()
# print(X)

# Q.NO 1
# dict={
#     "table":["a piece of furnitures","list of facts and figures"],
#     "cat": "a small animals"
# }
# print(dict)
 
                        # loops ("while")         
                       
# i = 1
# while i <= 1000:
#     print("to gand marao phir",i)
#     i += 1

# i= 5
# while i < 6:
#     print(i)
#     i=i-1 

# i= 1
# while i <= 200:
#     print(i)
#     i += 1


#q no 1
# i = 1
# while i <= 100:
#     print(i)
#     i +=1

#q no 2
# i=100
# while i>=1:
#     print(i)
#     i-=1

#q no =3
# n= int(input("entered the no:"))
# i=1
# while i <=10:
#     print(n*i)
#     i+=1

# Q.NO 4..
# num= [1,4,9,16,25,36,49,64,81,100]
# idx= 0
# while idx< len(num):
#     print(num[idx])
#     idx += 1


#Q no=5
# tup=(1,4,9,16,25,36,49,64,81,100)
# x= 49
# idx =0
# while idx<len(tup):
#     if(tup[idx]== x):
#      print("found at idx",idx)
#     idx+=1

# i= 100
# while i>=1:
#     print(i)
#     if(i==80):
#         break
#     i-=5 

# list =[ "lucky",45,56,76,98]
# for el in list:
#     print(el)

# Q.NO 1 
# tup=(1,4,9,16,25,36,49,64,81,100)
# idx=0
# x= 81
# for el in tup:
#    if(el == x):
#     print("found at idx:",idx)
#     idx += 1


                         ## range function

# for el in range(2,12,2):
#     print(el)

# # Q .NO 1
# for numb in range(1,101,1):
#     print(numb)

# Q.NO 2    
# for el in range(100,0, -1) :
#     print( el)


                            ### the functions ####

# def print_hello():
#     print("hello")

# print_hello()

# def average(a,b,c,d,e):
#     return(a+b+c+d+e/2)
# print(average(2,4,6,8,10))

# print(int((average(34,24,90,84,12))))
      
# print(int(average(65,34,56,98,100)))


# def divide( a,b):
#     return(a/b)
# print(divide(34,17))

#  Q NO =1
# chracter =["lucky","bholu","golu","rounak","chotu"]
# def print_len(chracter):
#     print(len(chracter))

# print_len(chracter)


# print_len(names)

#Q NO= 2
# def converter(usd_val):
#     inr_val= usd_val * 87
#     print(usd_val,"usd=",inr_val,"inr")
# converter(789)   

                                    # THE RECURSION#####
# def show(n):
#     if(n==0):
#      return
#     print(n)
#     show(n-1)  
# show(8)

##                                                     ## ><><---- FILES I\O IN PYTHONS

# f= open("demo.txt","w")
# f.write("lucky chauhan is biggsst suppoeter of bjp and just wanted to amke india akhand bharat")
# f.close

# import os
# os.remove("demo.txt")

# f= open("demo.txt","w")
# f. write("hii everyone my name is lucky chauhan\n ,i am from gaya also known as the land od of enlightment\n  and to maintain solidatry " \
# "with each and eveyone ,\n so i am learning" \
# "coding from apna college and my programming language that \n i had choosen is python" \
# "and i just wanted to get deeper in this \n language and to master each and every code " \
# "for the  learning" \
# "\n thank you  " )

# f= open("demo.txt","r")
# print(f.read())
# f.close


# f = open("demo.txt","a")
# f.write("so much for giving me your precious time. ")
# f.close
                                            ## to overwrite from the begining###  [ r+ ]
# f= open("demo.txt","r+")
# f.write("ladies and gentleman")
# # print(f.read())
# f.close
                                            ##### to truncete and to read ###    [ w+ ]
# 

# f= open("demo.txt","a+")
# f.write("\nhe is the only who trutly care for me\n he always used to call me and ask me whether and good or not \n " \
# "i know this is not his real side " \
# "everyone has its dark side but i know that perhaps this is all beyond of the lmit")
# print(f.read())
# f.close
                                                ### TO OPEN A NEW FILE ###

# with open ("practise.txt","x")as f:
#    f.write("hii everyone")
    
# f= open("demo.txt","w")
# f.write("hii everyone") 
# f.close  

                                    ###### DELETING A FILES ###

# import os
# os.remove("demo.txt")


            # Q .NUMBER 1 ####

# f= open("practise.txt","x")
# f.write("HII EVERYONE\n WE ARE LEARNING FILE I\O \n USING JAVA\n I LIKE PROGRAMMING IN JAVA ")
# f.close

            # Q NO 2 #####

# f=open("practise.txt","r")
# data= f.read()
# print(data)

# new_data=data.replace("java","python")
# print(new_data)

# f= open("practise.txt","w")
# f.write(new_data)


           # Q NO 3 ###

# word= "learning"
# f= open("practise.txt","r")
# data= f.read
# if(data.find(word) != -1):
#     print("found")
# else:
#     print("not found")

# import os
# os.remove("practise.txt")


# f= open("practise.txt","w")
# f.write("lucky is learning python from apna college")
# f.close

# import os
# os.remove("practise.txt")

# import os
# os.remove("second task")


