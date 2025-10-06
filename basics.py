#hello world
print("hello world")
####################################################
#variables 

#integer
age = 25

#float
age =25.5

#string
name = "hesham"

#boolean 
student = True

#check type
print(type(student))

################################################
# lists :are orderd and mutable collection

#creat list
fruits = ["apple","panana","cherry"]
numbers = ["1","2","3"] #zero index
#access element
print(fruits[2]) #cherry

#modifying list
#adding element
fruits.append("orange")
print(fruits)
#change element
fruits[1] ="blueberry"
print(fruits)

#list operation

print(len(fruits)) #length of list
print(fruits[1:3]) #slicing

#########################################################
#basic operators
print("basic operators ")
#arithmetic
a = 10
b = 5
print(a+b) #15
print(a-b)  #5
print(a*b) #50

#comparasion 
print("comparasion ")
print(a == b) #false
print(a > b) #true
print(a < b) #false

#logical
x = True
y = False 
print(x and y) #false
print(not x) #false

############################################################
#string formatting
name ="alice"
age = 30

#f-strings
print(f"my name is {name} and im {age} years old")

#.format()method
print("my name is {} and im {} years old".format(name , age))

# %formatting 
print("my name is %s and im %d years old" %(name , age))

####################################################################
#basic string operations 
text ="hello python"
#common string methods 
print (text.upper())
print (text.lower())
print (text.split())
print (len(text))
print (text.replace("python","world"))

#string concatenation
greeting = "hello"+""+"world"

#################################################################
#conditions
score = 86
if score >= 90 :
    grade ="A"
elif score >= 80 :
    grade = "B"
else :
    grade = "F"

print(f"your grade is :{grade}")

##################################################################
#loops 
#for loop through list 
fruits = ["apple","banana","cherry"]
for fruit in fruits :
    print(fruit)

#for loop with range
for i in range(5):
    print(i)

#while loop 
count = 0
while count < 5 :
    print(count)
    count += 1

#loop control 
for i in range(10):
    if i ==3 :
        continue 
    if i == 7 :
         break 
    
###############################################################    

