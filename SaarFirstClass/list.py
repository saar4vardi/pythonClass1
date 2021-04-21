from random import *
"""5.1"""
# list1 =[]
# num = input("enter an item to the list: ")
# while num != "":
#     list1.append(int(num))
#     num = input("enter an item to the list: ")
# print(min(list1))
# print(max(list1))
# print(sum(list1) / len(list1))

"""5.3"""
# list1 = []
# for i in range(10):
#     list1.append(randint(1, 10))
# print(list1)
"""5.4"""
# list1 = []
# list2 = []
# for i in range(3):
#     list1.append(input("enter a number"))
#     list2.append(input("enter a number"))
# list3 = list1 + list2
# print(len(list3))
"""5.5"""
# list1 = []
# passes = 0
# num3 = int(input("enter a number: "))
# while -1 < num3 < 101:
#     list1.append(num3)
#     if num3 >= 60:
#         passes += 1
#     num3 = int(input("enter a number"))
# print(f"the numbers of kids who passed the test is: {passes}")
# print(f"the numbers of kids who failed the test is: {len(list1) - passes}")
"""5.6"""
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(list1)):
#      list1[i] *= 2
# print(list1)
# list1 = []
# list3 = []
# for i in range(10):
#     list1.append(i)
# print(list1)
# print(list1[-3:])
# list1.reverse()
# print(list1)
# for i in range(0, 10, 2):
#     print(list1[i])
# for i in range(0, 10):
#     if list1[i] % 2 != 0:
#         list3.append(list1[i])
# print(list3)
# list1.reverse()
# list4 = list1[0::len(list1) -1]
# print(list4)
# print("=========================================")
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(list1)):
#     if i == 4 or i == 5 or i == len(list1) -1:
#         list1[i] = int(input("enter a number: "))
# print(list1)
# print("=========================================")
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# indexes = [4, 5, -1]
# numbers = [int(input("enter a number: ")), int(input("enter a number: ")), int(input("enter a number: "))]
# for i in range(len(indexes)):
#     list1[indexes[i]] = numbers[i]
# print(list1)
# print("=========================================")
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# indexes = [4, 5, -1]
# numbers = [int(input("enter a number: ")), int(input("enter a number: ")), int(input("enter a number: "))]
# for i in indexes:
#     list1[i] = numbers[indexes.index(i)]
# print(list1)
# print("=========================================")
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# indexes = [4, 5, -1]
# numbers = [int(input("enter a number: ")), int(input("enter a number: ")), int(input("enter a number: "))]
# for i, num in zip(indexes, numbers):
#     list1[i] = num
# print(list1)
