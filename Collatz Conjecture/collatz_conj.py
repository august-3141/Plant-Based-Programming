x = int(input("Input a starting number: "))
limit = False

while limit == False:

    print(int(x))

    if x == 1:

        limit = True

    else:

        if x % 2 == 0:

            x = x / 2

        else:

            x = (3 * x) + 1