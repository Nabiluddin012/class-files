# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)



# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x=["banana","apple","cheery"]
# print(x)

# y=("BANANA","CHEERY","MANGO")
# print(y)


# x=range(34,10,7)
# print(x)


# x = {"name" : "John",
#       "age" : 36                #dict
#       }
# print(x)


# username=input("username:")
# print("username:"+username)

# a = "Hello,World!"
# print(len(a))


# a = "Hello, World!"
# print(a[0])


# print(10 > 9)
# print(10 == 9)
# print(10 < 9)


# x = 5
# x += 3 
# print(x)     #similar to x+3


# name = input("What is your name? ")
# age = input("how old are you?")
# employment= input("Are you employed or unemployed? ")
# print("Hello"+ name)
# print("You are"+ age +"years old")
# if employment == "employed":
#     print("And its great that you are "+ employment +",You should learn python")
# elif employment == "unemployed":
#     print("And you are "+employment +  "go get a job you lazy ass")

# x=12
# print((x < 5 and x < 10))



# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print(x is z), print(x is y), print(x == y)





# x = ["apple", "banana"]
# print("banana" in x)
# x = ["apple", "banana"]
# print("pineapple" in x)


# a = 200
# b = 33
# c = 500
# if a < b and c > a:
#  print("Both conditions are True")
# else:
#     print("BOTH ARE WRONG")

#nested if
# x = 41
# if x <10:
#  print("Above ten,")
#  if x < 20:
#   print("and also above 20!")
# else:
#  print("but not above 20.")

# 


# x= 1
# while x < 10:
#   print(x+1,"if you was want ,you can stay with.......")
#   x+=1



# x= 1
# while x < 10:
#   print(x)
#   x=x+2


# def mul (a,b):
#     return a*b


# print(mul(3,4))



# def mul(a,b,c):
#     return a*b*c

# print(mul(2,3,4))



# this=["banana","apple","cheery","mango","jackfruit"]


# print(this[1:3])

# i = 1
# while i < 10:
#  print(i)
#  i+= 1




# i=0
# while i < 10:
#     i+=1
#     if i==5:
#         continue
#     print(i)

# fruits=["banana","apple","cherry"]
# for x in fruits:
#     print(x)

#     for x in "banana":
#         print(x)


# fruits=["banana","apple","cheery","mango"]
# for x in fruits:
#     if x=="cheery":
#         continue
#     print(x)



# for x in range(6):
#  print(x)


# x=("one",)


# this=["banana","apple","cherry"]
# this[0]="mango"
# print(this)

# x=("mango","banana","cherry")
# y=["mango","banana","cherry"]
# z={"mango","banana","cherry"}
# print(type(x))
# print(type(y))
# print(type(z))



# x=1
# while x <0:
#     print("i beg u")
#     x+=1 
# else:
#     print("market have no value")




# for x in "banana":
#     print(x)


# MH=["baby","boys","girls"]
# for jk in MH:
#     if jk=="boys":
#         continue
#     print(jk)



# for x in range(5):
#     print(x)
# for x in range(2,9):
#     print(x)
# for x in range (5,50,10):
#     print(x)
# list=["lion","cat","tiger"]
# list2=["fish","bird","insects"]
# for x in list:
#     for y in list2:
#         print(x,y)


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#  for y in fruits:
#   print(x, y)


# def my():
#     print("hey im the function")
#my()


# def myname (nah):
#     print(nah+"yeah im form canada")

# myname("how are you")  

# def my_function(fname, lname):
#  print(fname + " hey lame" + lname)

# my_function("maa","naa") 


# def lm(*kids):
#     print("this is my child +"+kids[2])

# lm("ali","nak","ese")

# print("Workshop", "on", "Python", sep="\n")
# sep=‘\n’ will put each word in a new lin


# a = 29 # Assigning value of a
# b = 17 # Assigning value of b
# c = 36 # Assigning value of c
# average = ( a + b + c)/3
# print("Average value is ", average)

# students = {
#     "S001": {
#         "name": "Alice",
#         "age": 21,
#         "courses": {
#             "math": {"grade": "A", "credits": 3},
#             "physics": {"grade": "B+", "credits": 4},
#         }
#     },
#     "S002": {
#         "name": "Bob",
#         "age": 22,
#         "courses": {
#             "math": {"grade": "B", "credits": 3},
#             "chemistry": {"grade": "A-", "credits": 4},
#         }
#     },
#     "S003": {
#         "name": "Charlie",
#         "age": 20,
#         "courses": {
#             "biology": {"grade": "A", "credits": 4},
#             "physics": {"grade": "B", "credits": 4},
#         }
#     }
# }

# x=students["S003"]["courses"]["physics"]["credits"]
# print(x)























# thislist = ["apple", "banana", "cherry","10","20","30",True,False,100,200]

# print(len(thislist))


# x = (1)   
# y = (2.8) 
# z = ("3") 

# print(type(x))
# print(type(y))
# print(type(z))

# x = int(1)  
# y = int(2.8)
# z = int("3")

# print(type(x))
# print(type(y))
# print(type(z))

# x = float(1)   
# y = float(2.8)   
# z = float("3")   
# w = float("4.2") 

# thislist = ["apple", "banana", "cherry","watermelon","grapes","kiwi","mango"]

# for x in thislist:
#     if x == "cherry":
#         continue
#     elif x == "kiwi":
#         continue
#     elif x == "mango":
#         break
#     print(x)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:4])
# print(thislist[5])


# thislist = ["Apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list") 


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist) 

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["watermelon","kiwi"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]

# thislist.insert(1,"jackfruit")
# print(thislist)


# thislist = ["apple", "banana", "cherry","10","20","30",True,False,100,200,]

# print(len(thislist))

class person:
    def mh(self,name,age):
        self.name=name
        self.age=age


p=person()
p2=person()

p.mh("mahi","29")
p2.mh("nabil","22")
print(p.age)
print(p.name)
print(p2.name)
print(p2.age)
