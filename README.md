# CollatzConjecture

Here are three separate scripts I created to allow for brute forcing many numbers of the Collatz conjecture. 

My goal was to test whether the first 2^32 integers were positive however I only managed to achieve 2^29 before killing the process for fear over my pc's life (it was using all RAM, virtual memory and had 100% NVME usage lol).

MyCollatzConjectureBasic.py was the first iteration I programmed before realising I really needed to dive into learning multiprocessing/threading and using Numba to increase processing speed. However, since attempting to implement both of these features I realised a huge problem with them both. They require a max step count to be even vaguely fast, which means that both CollatzConjecture.py and CollatzConjectureWithNumba.py both dont actually test whether something fits into the conjecture. I also found multiprocessing was slower than using a single core because of the expensive operations involved in merging known values (prevNums) together after each batch as well as the fact that each core doesnt benefit from the memoization of other cores in that batch. Numba non-multiprocessing was slightly faster than my original algorithm, however as mentioned before doesnt properly check whether it fits into the conjecture.

If you want to find out whether a specific number follows the pattern you can use SingleNumberTester.py but you wont find one that is false. If you do somehow manage to find one it will either detect it is in a loop (that doesnt return to zero) and will return false or will run indefinitely through some other unforeseen methods.

Probably dont use CollatzConjecture.py or CollatzConjectureWithNumba.py. If your really interested in testing large numbers use MyCollatzConjectureBasic.py but dont go over 2^28 unless you are willing to max out RAM, virtual memory and disk for 10+ mins. Especially dont use high numbers if you are on a hard drive (disk thrashing would go crazy). It uses so much memory because it saves all values it knows lead to zero in a set which is checked constantly to reduce the time to calculate each number (very large cache)

Also warning I used ChatGPT to help me learn multiprocessing with Numba, so suspicious code in the non-basic algorithms is likely me trying to understand what it all means.

If you know how to optimise it further, please improve it, but make sure you let me know because I want to see it!

Also Im not sure whether recursive is faster than iterative.
