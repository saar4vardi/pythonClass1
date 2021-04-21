"""9.1"""
from datetime import *
from time import *

# name = input("enter your name: ")
# age = int(input("enter your age: "))
# g = datetime.now()
# year = g.strftime("%Y")
# year = int(year) + 100 - age
# print(year)

"""9.2"""
# t = datetime.now()
# america = t.strftime("%d/%m/%y")
# europe = t.strftime("%m/%d/%y")
# print(f"the american date of today is: {america}")
# print(f"the european date of today is: {europe}")

"""9.3"""
# day = input("enter the day you were born: ")
# month = str(input("enter the month you were born in: "))
# year = input("enter the year you were born in: ")
# g = datetime(int(year), int(month), int(day))
# day = g.strftime("%d")
# month = g.strftime("%b")
# year = g.strftime("%Y")
# print(f"{month} - {day} - {year}")

"""9.4"""
# now = datetime.now()
# day = int(input("Please enter a number: "))
# print("The day of the current week is: ", (now + timedelta(days=(day-6))))

"""14.1+3 """
with open("C:/Users/SAAR/saar/story.txt", "w") as targil:
    targil.write("A boy is playing there"
                 "\nThere is a playground "
                 "\nAn airplane is in the sky "
                 "\nThe sky is pink "
                 "\nAlphabets and numbers are allowed in the password")
with open("C:/Users/SAAR/saar/story.txt", "r+") as targil:
    x = targil.readline()
    while x != "":
        print(x.strip())
        x = targil.readline()

"""14.2"""
with open("C:/Users/SAAR/saar/story.txt", "r+") as targil:
    count = 0
    while targil.readline() != "T":
        count += 1
        line = targil.readline()
        if not line:
            break
    print(f"the number of Lines without the letter (T) is: {count}")

with open("C:/Users/SAAR/saar/story.txt", "r+") as targil:
    count2 = 0
    for line in targil:
        words = line.split()
        for word in words:
            if word == "the" or word == "The":
                count2 += 1

print(f"the number of times the word (the) or (The) appears is: {count2}")
with open("C:/Users/SAAR/saar/story.txt", "r+") as targil:
    count_words = 0
    for line2 in targil:
        words2 = line2.split()
        for word in words2:
            count_words += 1
print(f"the number of words in the file is: {count_words}")

"""14.4"""

