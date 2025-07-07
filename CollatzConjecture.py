import time
import math
import numpy as np
from numba import njit, prange
from line_profiler import LineProfiler

MAX_N = 1000000000

@njit
def StepSim(prevNums, num):
    maxSteps = 1000
    temp = np.empty(maxSteps, dtype=np.int64)
    idx = 0

    while num < MAX_N and prevNums[num] == 0:
        temp[idx] = num
        idx += 1
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1

    for i in range(idx):
        num = temp[i]
        if num < MAX_N:
            prevNums[num] = 1

@njit
def RunCollatz(prevNums, start, end):
    for i in range(start, end):
        StepSim(prevNums, i)

def main():
    duration = int(input("How long would you like to test for in seconds?: "))
    prevNums = np.zeros(MAX_N, dtype=np.uint8)
    prevNums[1] = 1
    prevNums[2] = 1
    prevNums[4] = 1

    startTime = time.monotonic()
    i = 1

    print("Calculating...")
    while time.monotonic() - startTime < duration:
        RunCollatz(prevNums, i, i + 100000)
        i += 10000

    print(f'Calculated up to 2**{math.log2(i):.2f} ({i})')

if __name__ == "__main__":
    main()
