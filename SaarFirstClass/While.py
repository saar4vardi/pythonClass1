"""תרגיל 1"""
# num1 = int(input("enter a three digit number number: "))
# while 99 < num1 < 1000:
#     print(num1//100 + (num1//10) % 10 + num1 % 10)
#     num1 = int(input("enter another three digit number number: "))
# print("wrong number, DDOSSSSSSSSSSSSSS ERRORRRRRR")
"""תרגיל 2"""
# age = int(input("enter your age: "))
# while 0 <= age <= 120:
#     if 0 <= age <= 18:
#         print("kid")
#     else:
#         if 19 <= age <= 60:
#             print("adult")
#         else:
#             if 61 <= age <= 120:
#                 print("senior")
#     age = int(input("enter your age: "))
# print("R.I.P")

"""תרגיל 3"""
# num1 = int(input("enter an even number number: "))
# num2 = int(input("enter an even number number: "))
# while num1 % 2 == 0 and num2 % 2 == 0:
#     print(num1+num2)
#     num1 = int(input("enter an even number number: "))
#     num2 = int(input("enter an even number number: "))
# print(num1 * num2)
"""תרגיל 4"""
# num1 = int(input("enter an even number number: "))
# num2 = int(input("enter an even number number: "))
# while num1 + num2 == 10:
#     num1 = int(input("enter an even number number: "))
#     num2 = int(input("enter an even number number: "))
# print("Sum != 10")
"""תרגיל 5"""
# day = int(input("enter day"))
# month = int(input("enter month"))
# year = int(input("enter year"))
# while 1 <= day <= 31 and 1 <= month <= 12 and 1950 <= year <= 2025:
#     if year // 10 % 10 == 0:
#         print(f"{day}/{month}/0{year % 100}")
#     else:
#         print(f"{day}/{month}/{year % 100}")
#     day = int(input("enter day"))
#     month = int(input("enter month"))
#     year = int(input("enter year"))
# print("wrong date")
"""תרגילי לולאות בסיסיים"""
# num1 = 0
# i = 6
# while i > 0:
#     num1 += int(input("enter a number: "))
#     i -= 1
# print(num1)
"""תרגיל 2"""
# num1 = 0
# num2 = 0
# i = 6
# even = 0
# while i > 0:
#     num1 = int(input("enter a number: "))
#     i -= 1
#     if num1 % 2 == 0:
#         num2 += num1
#         even += 1
# if even > 0:
#     print(num2/even)
# else:
#     print("0")
"""תרגיל 3"""
# i = 10
# while i <= 99:
#     i += 1
#     if i % 10 == 7:
#         print(i)
"""תרגיל 4"""
# i = 10
# total = 0
# while i <= 99:
#     if i % 10 == 0:
#         total += i
#     i += 1
#
# print(total)
"""תרגיל 5"""
# avg = 0
# count = 0
# grade = int(input("enter your grade: "))
# while 0 <= grade <= 100:
#     if 60 <= grade <= 100:
#         avg += grade
#     count += 1
#     grade = int(input("enter your grade: "))
# print(avg/count)
"""תרגיל 6"""
# avg1 = 0
# avg2 = 0
# count1 = 0
# count2 = 0
# grade = int(input("enter your grade: "))
# while 0 <= grade <= 100:
#     if grade >= 60:
#         avg1 += grade
#         count1 += 1
#     else:
#         avg2 += grade
#         count2 += 1
#     grade = int(input("enter your grade: "))
#
# if avg2 == 0 and avg1 == 0:
#     print(f"fail avg is {avg2}")
#     print(f"pass avg is {avg1}")
# else:
#     if avg2 == 0:
#         print(f"fail avg is {avg2}")
#         print(f"pass avg is {avg1 / count1}")
#     else:
#         if avg1 == 0:
#             print(f"pass avg is {avg1}")
#             print(f"fail avg is {avg2 / count2}")
#         else:
#             print(avg1/count1)
#             print(avg2/count2)
"""תרגיל 7"""
# i = 1
# total = 0
# for i in range(1,5):
#     number = int(input("enter a number: "))
#     total += number % 10
# print(f"the sum of the right digits in each number is: {total}")
"""תרגיל 8"""
# number = int(input("enter a number: "))
# for number in range(0,number):
#     if number % 5 == 0:
#         print(number)
"""תרגיל 9"""
# number = int(input("enter a number: "))
# for number in range(2,number,2):
#     print(number)
"""תרגיל 10"""
# count = 0
# i = int(input("enter a number: "))
# while i != 0:
#     if i % 7 == 0 or i % 3 == 0:
#         count += 1
#     i = int(input("enter a number: "))
# print(count)

