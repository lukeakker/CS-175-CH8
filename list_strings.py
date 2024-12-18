# -*- coding: utf-8 -*-
"""List_Strings.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-W0RMPkJQuFt4MTr1QugGvvXtBkmE4CC
"""

#Lucas Vandenakker
#CS175
#Palindrome

str1 = input("Enter a string: ")

tempstr = str1

str1.strip()

str1.lower()

str1 = str1.replace(" ", "")

str2 = str1[::-1] #this reverses the string

if(str1 == str2):
  print(f"Yes the string {tempstr} is a palindrome!")

else:
  print(f"No, the string, {tempstr}, is not a palindrome")

#Lucas Vandenakker
#CS175
#num vowels

str1 = input("Enter a string: ")

vowels = []

for char in str1:

  if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u") :
     vowels.append(char)


print(f"There are {len(vowels)} vowels")

#Lucas Vandenakker
#CS175
#longest word

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = max(words, key=len)

print(f"The longest word is '{longest}'")

#Lucas Vandenakker
#CS175
#max and min

numbers = [3, 5, 2, 9, 6]

print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

#Lucas Vandenakker
#CS175
#remove duplicates

items = [1, 2, 2, 3, 4, 4, 5]

setItems = set(items)

listItems = list(setItems)

print(f"List without duplicate elements: {listItems}")

#Lucas Vandenakker
#CS175
#even and odd

nums = [3, 5, 2, 9, 6]

evens = []
odds = []

for n in nums:
  if n % 2 == 0:
    evens.append(n)
  else:
    odds.append(n)

print(f"Evens: {evens}\nOdds: {odds}")

#Lucas Vandenakker
#CS175
#merge lists

list1a = [1, 2, 3, 4]
list2b = [3, 4, 5, 6]

mergedList = list1a + list2b

setL1st = set(mergedList)

newL1st = list(setL1st)

newL1st.sort()

print(f"Sorted list: {newL1st}")

#Lucas Vandenakker
#CS175
#differnt lists

list1 = [1,2,3,4]
list2 = [3,4,5,6]

setList1 = set(list1)
setList2 = set(list2)

difference = setList1 - setList2

print(f"Difference of list1-list2 = {list(difference)}")

#Lucas Vandenakker
#CS175
#anagrams

words = ["listen", "enlist", "hello", "world", "drowl"]

anagrams = []

for i in range(len(words)):

  for j in range(i+1, len(words)):

    word1 = words[i]
    word2 = words[j]

    if(sorted(word1) == sorted(word2)  ):
      tempTuple = (word1, word2)
      anagrams.append(tempTuple)

print(f"Anagrams: {anagrams}")

#Lucas Vandenakker
#CS175
#concat strings

words = ["Hello", "world", "Python", "rocks"]

longString = " - ".join(words)

print(longString)

#Lucas Vandenakker
#CS175
#only words

string = "Hello, World! 123"


word = "".join(char for char in string if char.isalpha())

print(f"Alphabetic characters only: {word}")