import timeit
# import string
import collections

with open('input.txt', 'r+') as f:
  puzzle_input = [i for i in f.read().splitlines()]

test_input = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

def part_a(puzzle_input):
  twos = 0
  threes = 0
  for p in puzzle_input:
    counter = collections.Counter(p)
    values = set(counter.values())
    if 2 in values:
      twos += 1
    if 3 in values:
      threes += 1

  return twos * threes

test_input = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

def part_b(puzzle_input):
  for p in puzzle_input:
    for i in puzzle_input:
      diff = 0
      for z in zip(p, i):
        if z[0] != z[1]:
          diff += 1
      
      if diff == 1:
        answer = ''
        for z in zip(p,i):
          if z[0] == z[1]:
            answer += z[0]
        return answer
  
  return 'ERROR'


start_time = timeit.default_timer()
print('Part a: {}\t({}s)'.format(part_a(puzzle_input),round(timeit.default_timer()-start_time,2)))

start_time = timeit.default_timer()
print('Part b: {}\t({}s)'.format(part_b(puzzle_input),round(timeit.default_timer()-start_time,2)))
