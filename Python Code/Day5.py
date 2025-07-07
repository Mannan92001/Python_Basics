### 1. Check Positive, Negative, or Zero
# Ask the user to enter a number. Print whether it's positive, negative, or zero.
num=float(input("Enter your number:   "))
if num>0:
    print("Positive")
elif num==0:
    print("Zero")  
else:
     print("Negative")      
### 2. Find the Smallest of Three Numbers
# Take 3 numbers from the user and print the smallest one.
num1=float(input("enter your first number:  "))
num2=float(input("enter your second number:  "))
num3=float(input("enter your third number:  "))
if num1<num2 and num1<num3:
    print("First is smaller1 than other two")
elif num2<num1 and num2<num3:
    print("Second is smaller than other two") 
elif   num3<num1 and num3<num2: 
    print("Third is smaller than other two")
else:
#     print("All numbers are equall")    
### Check if Number is Divisible by Both 3 and 5
# Ask for a number and check if it's divisible by both 3 and 5, only 3, only 5, or neither.
 num=float(input("Enter your number:   "))
 if num%3==0 and num%5==0:
     print("this num is divided by both") 
 elif num%3==0:
     print(f"Divide by 3  {num/3}")
 elif num%5==0:
     print(f"Divide by 5  {num/5}")    
 else:
     print("Not divide by 3 and 5")       
###Print all even numbers from 1 to N (using a loop).
 n=int(input("Enter your end number:  "))
 for i in range(1,n+1):
     if i%2==0:
      print(i)
###  Count Vowels in a String
# Ask the user to enter a word or sentence, then count and print the number of vowels.
 word=input("Enter your word or sentence:  ")
 sum=0
 for i in word:
     if i.lower()in"aeiou":
         sum+=1
 print(sum) 
### 6. Reverse a String Without Using [::-1]
# Ask the user to enter a string. Reverse it using a loop (not slicing).
 text=input("enter your word:  ")
 reverse=""
 for i in text:
     reverse=i+reverse
 print(reverse)    
### 7.Count Digits, Letters, and Spaces in a String
# Take input like a sentence and count how many:

# Letters

# Digits

# Spaces
 word=input("Enter your sentence:   ")
 let=0
 dig=0
 spac=0
 for i in word:
     if i.isalpha():
         let+=1
     elif i.isdigit():
         dig+=1 
     elif i==" ":
         spac+=1
 print(let)               
 print(dig)               
 print(spac)               