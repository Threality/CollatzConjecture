import time
import math
import numpy as np
from numba import njit, prange
from line_profiler import LineProfiler

MAX_N = 100_000_000
BATCH_SIZE = 10_000
MAX_STEPS = 10_000


@njit(parallel=True)
def MarkNumbers(prevNums, buffer, length):
    for i in range(buffer.shape[0]):
        for j in range(length[i]):
            n = buffer[i, j]
            if n < prevNums.size:
                prevNums[n] = 1


@njit
def RunCollatzParallel(start, end, maxSteps):
    size = end - start
    buffer = np.zeros((size, maxSteps), dtype=np.int64)
    lengths = np.zeros(size, dtype=np.int32)

    for idx in prange(size):
        n = start + idx
        steps = 0
        while n != 1 and steps < maxSteps:
            buffer[idx, steps] = n
            steps += 1
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        lengths[idx] = steps

    return buffer, lengths


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
        start = i
        end = i + BATCH_SIZE

        buffer, lengths = RunCollatzParallel(start, end, MAX_STEPS)
        MarkNumbers(prevNums, buffer, lengths)

        i += BATCH_SIZE

    print(f'Calculated up to 2**{math.log2(i):.2f} ({i})')


if __name__ == "__main__":
    main()
