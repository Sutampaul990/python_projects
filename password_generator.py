from ast import parse
import random
from tokenize import String
from xml.dom.expatbuilder import parseString #implement of random library
print("Welcome to Py_Password Generator!")
#pre_Stock
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','%','^','&','(',')','<','>']
numbers=['0','1','2','3','4','5','6','7','8','9']
s=int(input("How many letters would you like in your password? \n"))
sym=int(input("How many symbols would you like? \n"))
num=int(input("How many numbers would you like? \n"))

# main part of the Code
store_list= []

for char in range(1,s+1):
    #letters 1 to user_input 
    store_list.append(random.choice(letters))
for symb in range(1,sym+1):
    #symbols 1 to user_input    
    store_list.append(random.choice(symbols))
for numb in range(1,num+1):
    #numbers 1 to user_input    
    store_list.append(random.choice(numbers))


print(store_list)
random.shuffle(store_list)
password=""
for char in store_list:
    password+=char

print(f"Here is your Password : {password}")