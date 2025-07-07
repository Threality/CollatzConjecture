import time
import math

def StepSim(prevNums, num, curArray):
    if num in prevNums:
        for num in curArray:
            prevNums.add(num)
        return prevNums
    elif num % 2 == 0:
        curArray.append(num)
        curArray = StepSim(prevNums, num // 2, curArray)
    else:
        curArray.append(num)
        curArray = StepSim(prevNums, 3 * num + 1, curArray)
    return curArray
    
def main():
    prevNums = {1, 2, 4}
    duration = int(input("What number would you like to test up until?: "))
    startTime = time.monotonic()
    lastPercent = -1

    print("Calculating...")
    for i in range(duration + 1):
        percent = int((i / duration) * 100)
        prevNums = StepSim(prevNums, i + 1, [])
        
        if percent != lastPercent:
            print(f"\rProgress: {percent}%", end="", flush=True) # percent calcs reduce speed by ~2-300000/s
            lastPercent = percent

    print(f'\nCalculated up to 2**{math.log2(i):.2f} ({i})')
    print(f'Calculation took: {(time.monotonic() - startTime):.2f} seconds')
    print(f'Average integers checked per second: {(i/(time.monotonic() - startTime)):.2f}')

if __name__ == "__main__":
    main()