def StepSim(num):
    previouslyVisited = set({})
    while num != 1:
        if num in previouslyVisited:
            return False
        previouslyVisited.add(num)
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    return True

if __name__ == "__main__":
    print(StepSim(int(input("Number: "))))