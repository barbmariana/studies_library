# function that return the maximum ways
def countWays(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    ways = [0] * (n + 1)  # This way we reserve the space to all the numbers
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]


# main program

numberOfSteps = int(input("How many steps: "))
if numberOfSteps < 0:
    numberOfSteps = int(input("Number of steps should be a positive number: "))
else:
    numOfWays = countWays(numberOfSteps)
    print("Posso subir a escada de", numberOfSteps, "degraus de :", numOfWays, "formas")
