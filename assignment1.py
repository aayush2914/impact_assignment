# Quess- 1
str1 = "Aayush"
lis = ["Aayush",15,6.25]
flo = 6.53
tup = (15.5,6,'Aayush')
#ques-2
""" 
    Type of var1 is string
    Type of var2 is string
    Type of var3 is list
    Type of var4 is float
"""
#ques-3
var1 = 5
var2 = 3
# / is the division operator it returns the quotient after division
print(var1/var2)
# % is the modulous operator it returns the remainder after the division
print(var1%var2)
# // is the floor division operator it returns the floor value of the quotient
print(var1//var2)
# ** is the power operator it return the power of given number
print(var1**var2)
# Ques -4
b_list = [15,15.6,25,True,"Aayush",False,[15,26,78],(17,18),{35,78},'aayu']
for i in range(0,len(b_list)):
    print(b_list[i] , " is of type: ", type(b_list[i]))
#Ques-5
A = int(input("Enter number A: "))
B = int(input("Enter number B: "))
if(A%B==0):
    print("A is completely divisible by B")
    print("Number of times A is divisible by B is" , int(A/B))
else:
    print("A is not divisible by B")

#Ques - 6
a_list = [25,65,12,35,1,85,78,15,15,68,12,68,95,45,25,36,15,26,18,28,29,39,69,64,24,65,37,69]
for i in range(0,len(a_list)):
    if(a_list[i]%3==0):
        print(a_list[i], " is divisible by 3")
    else:
        print(a_list[i]," is not divisible by 3")
#Ques - 7
"""Mutuable data types are those data types which allows to change its value without changing its identity, examples of immutable data types: list,set,dictionary"""
list2 = ["Aayush",15,18]
set1 = {155,168,'Aayu'}
dict = {'key' :101,
        'value': 125}
list2.append(280)
set1.add(180)
print(list2)
print(set1)
"""Immutuable data types are those data types which does not allows to change its value without changing its identity, examples of immutable data types: int,float,string"""
i = 5
f = 15.5
str1 = "Aayushj"
