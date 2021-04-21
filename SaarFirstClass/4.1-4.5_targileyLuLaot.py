from random import randint
# num1 = int(input("insert a number: "))
# num2 = int(input("insert a number: "))
# if num1 < num2:
#     for i in range(num1 + 1, num2):
#         if i % 2 == 0:
#             print(i)
# else:
#     for i in range(num2 + 1, num1):
#         if i % 2 == 0:
#             print(i)

# 4.2

# num1 = int(input("insert a number: "))
# f = True
# for i in range(2, num1):
#     if num1 % i == 0:
#         f = False
# print(f"the number is: {f}")
#
# num1 = int(input("insert a number: "))
# for i in range(2, num1):
#     if num1 % i == 0:
#         print(f"the number is not rishoni")
#         break
# else:
#     print(f"the number is rishoni")

#4.3

# num1 = int(input("insert a number: "))
# num2 = randint(1, 9)
# print(num2)
# while num1 != num2:
#     if num1 > num2:
#         print("the number you inserted is bigger")
#         num1 = int(input("insert a new number: "))
#     else:
#         print("the number you inserted is smaller")
#         num1 = int(input("insert a new number: "))
# print("the numbers are equal")

#4.4
# num1 = int(input("insert a number between 1-100: "))
# Max = 100
# Min = 1
# bigsmallequal = "big"
# count = 0
# while bigsmallequal != "equal":
#     num2 = randint(Min, Max)
#     print(num2)
#     bigsmallequal = str(input("is the number: big, small, equal ?"))
#     count += 1
#     if bigsmallequal == "big":
#         Max = num2 - 1
#     else:
#         Min = num2 + 1
# print(f"the number is equal. it took the system: {count} times to guess")

# 4.5
# a = 0
# b = 1
# fabo = int(input("enter the number you want the fabonachi to count up to: "))
# print(f"{a},{b},", end="")
# for i in range(0, fabo//2 - 1):
#     a = b + a
#     b = b + a
#     print(f"{a},{b},", end="")

# תרגילי לולאות 1
# grade = int(input("enter your grade: "))
# highestgrade = 0
# avg = 0
# count = 0
# while 0 < grade < 100:
#     if grade > highestgrade:
#         highestgrade = grade
#     avg += grade
#     count += 1
#     grade = int(input("enter your grade: "))
# print(f"the highest grade is: {highestgrade}\n the average grade is: {avg//count}"
# avg = avg//grade
#       f"\n the difference between the highest grade and the average grade is: {highestgrade - avg}")
# תרגילי לולאות 2
# password = str(input("enter password: "))
# password2 = str(input("enter same password: "))
# count = 1
# while password != password2:
#     print("ERROR - wrong password!!")
#     password2 = str(input("enter same password: "))
#     count += 1
#     if count == 5:
#         print("ERORR TOO MANY TRIES.")
#         break
# else:
#     print("password passed successfully, thank you")
# דרך שנייה
# password = str(input("enter password: "))
# password2 = str(input("enter same password: "))
# for i in range(1, 5):
#     if password != password2:
#         print("ERROR - wrong password!!")
#         password2 = str(input("enter same password: "))
#     else:
#         print("password passed successfully, thank you")
#         break
# else:
#     print("ERORR TOO MANY TRIES.")
"""תרגיל מס 2"""
# num1 = int(input("enter a number: "))
# numsum = 0
# while num1//10 > 0:
#         numsum += num1 % 10
#         num1 //= 10
# numsum += num1
# print(numsum)

#תרגיל 3
# num1 = int(input("enter a number: "))
# if num1 > 0:
#     smallnum = num1
# while num1 != 0:
#     if num1 < 0:
#         continue
#     elif num1 < smallnum:
#         smallnum = num1
# first_run = True
# smallnum = 0
# while True:
#     num1 = int(input("enter a number: "))
#     if num1 > 0 and first_run:
#         smallnum = num1
#         first_run = False
#     if num1 == 0:
#         break
#     elif num1 < 0:
#         continue
#     elif num1 < smallnum:
#         smallnum = num1
# if smallnum == 0:
#     print("No positive numbers were registered!")
# else:
#     print("The smallest number is - " + str(smallnum))
# לקלוט מילה ולהדפיס בכל שורה את האות הבאה מספר פעמים לפי מיקום האות. למשל, אם נקלט: abcd,
# word = input("enter a word: ")
# digit = 0
# for i in word:
#     digit += 1
#     print(digit*i)

# word = input("enter a word: ")
# digit = 0
# for i in word:
#     digit += 1
#     for c in range(digit):
#         print(i, end="")
#     print()
#תרגיל 4
# num1 = int(input("enter a number: "))
# while num1//10 != 0:
#         num1 //= 10
# print(num1)
#תרגיל 5
# num2 = 0
# tint = 0
# for i in range(1,8):
#     num1 = int(input("enter a number: "))
#     if num1 > num2:
#         num2 = num1
#         tint = i
# print(tint)

#תרגיל 6
# num = int(input("enter a number"))
# invert_num = 0
# while num//10 != 0:
#     invert_num = invert_num * 10 + num % 10
#     num //= 10
# invert_num = invert_num * 10 + num
# print(invert_num)
# print(invert_num * 2)

# #תרגיל 7
# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")
# division = 0
# while num1.isnumeric() and num2.isnumeric():
#     if num2 >= num1:
#         print("Error, enter new numbers (The 1st number should be bigger!)")
#         num1 = input("Enter a number: ")
#         num2 = input("Enter a number: ")
#     else:
#         for i in range(int(num2), int(num1) + 1, int(num2)):
#             division += 1
#         break
# print(f"{num1} / {num2} = {division}")
# print (f"{num1} % {num2} = {int(num1) - int(num2) * division}")

# תרגיל 8
# mini = 0
# for i in range(1, 6):
#     num = int(input("Enter A Number: "))
#     if num > 7:
#         if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
#             if mini == 0 or num < mini:
#                 mini = num
#     elif num == 2 or num == 3 or num == 5 or num == 7:
#         if num < mini or mini == 0:
#             mini = num
# if mini == 0:
#     print("No odd numbers were registered")
# else:
#     print(f"The smallest odd number is - {mini}")

#תרגיל 8
# mini = 0
# for i in range(1, 6):
#     num = int(input("Enter A Number: "))
#     if num == 2:
#         mini = 2
#     if num > 1:
#         for j in range(2, num):
#             if (num % j) == 0:
#                 break
#             elif num < mini or mini == 0:
#                 mini = num
# if mini == 0:
#     print("No prime numbers were registered")
# else:
#     print(f"{mini} is the smallest prime number")
