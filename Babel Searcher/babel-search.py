import random
import time

inputWord = str(input("Enter a word to find: "))
babelString, alphaString, count, = "", "a b c d e f g h i j k l m n o p q r s t u v w x y z", 0
alphaString = alphaString.split()

start = time.time()
while (inputWord in babelString) == False:
    character = alphaString[random.randint(0, 25)]
    babelString = "".join([babelString, character])
    count +=1
end = time.time()

print(f"Babel String: {babelString} <--")
print(f"Word found: \"{inputWord}\", Comparisons: {count}, Time Taken: {end - start}s")
