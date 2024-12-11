puzzle_input="""7725 185 2 132869 0 1840437 62 26310"""
# puzzle_input="""125 17"""
import re
from collections import *
import math

def part1():
    stones = puzzle_input.split()
    
    # Blink 25 times
    for _ in range(25):
        i = 0
        while i < len(stones):
            stone = stones[i]
            if stone == "0":
                stones[i] = "1"
            elif len(stone) % 2 == 0:
                l, r = stone[:len(stone)//2], stone[len(stone)//2:]
                r = str(int(r)) # deal with any leading zeros
                stones[i] = l
                i += 1
                stones.insert(i, r)
            else:
                stones[i] = str(int(stone)*2024)
            i += 1
    print(len(stones))
    

def part2():
    stones = Counter([int(x) for x in puzzle_input.split()])
    
    # Blink 75 times
    for _ in range(75):
        updated_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                updated_stones[1] += count
            elif (n_digits:=int(math.log10(stone) + 1)) % 2 == 0:
                divisor = 10**(n_digits//2)
                l = stone//divisor
                r = stone - l*divisor
                updated_stones[l] += count
                updated_stones[r] += count
            else:
                updated_stones[2024*stone] += count
        stones = updated_stones
    print(stones.total())
    
    
part1()
part2()
