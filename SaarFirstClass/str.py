"""1"""
# str = "Antartica"
# str = str.strip("A")
# str = str.replace("a", "")
# print(str)
"""2"""
# str = "ant"
# for char in str:
#     print(str[0::len(str) - 1])
"""3"""
# from random import randint
# namecode = input("Enter desired namecode: ")
# password = ""
# for word in namecode:
#     password += namecode[randint(0, len(namecode) - 1)]
# print(password)
"""4"""
# list1 = []
# word1 = input("enter a word: ")
# word2 = input("enter a word: ")
# for char1 in word1:
#     if word2.find(char1) >= 0 and char1 not in list1:
#         list1.append(char1)
# print(len(list1))
"""5"""
# sentence = "the word the appears in the sentence 3 times"
# word = "the"
# list1 = []
# ind = 0
# while sentence.find(word, ind) != -1:
#     next_index = sentence.find(word, ind)
#     ind = next_index + 1
#     list1.append(next_index)
# print(list1)
"""6"""
# sentence = "the word the appears in the sentence 3 times"
# list1 = sentence.split()
# print(list1)
# list1 = [word.capitalize() for word in list1]
# print(list1)
"""7"""
sentence = "the word the appears in the sentence 3 times"
char = "t"
# words = sentence.split()
# print(words)
new_sentence = sentence.replace("t", "T")
print(new_sentence)

# for word in words:
#     if word[0] == char:
#         words[words.index(word)] = words[words.index(word)].capitalize()
# print(words)


#for char in sentence:
#     if char == "t":
#         new_sentence[sentence.index(char)] = sentence[sentence.index(char)].capitalize()
#         print(sentence)
