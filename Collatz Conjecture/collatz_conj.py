x = int(input("Input a starting number: "))
limit = int(input("Enter a limit for outputs: "))
count = 0

while count < limit:

    print(x)

    if x % 2 == 0:

        x = x / 2

    else:

        x = (3 * x) + 1

    count = count + 1