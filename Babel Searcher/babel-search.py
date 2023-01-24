import random

inputWord = str(input("Enter a word to find: "))
babelString = ""
alphaString = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphaString = alphaString.split()
count = 0

while (inputWord in babelString) == False:
    character = alphaString[random.randint(0, 25)]
    babelString = babelString + character
    count = count + 1

print(f"String used:\n{babelString} <--\nWord found: \"{inputWord}\", Time Taken: {count} characters")