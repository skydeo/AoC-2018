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
      common = ''
      for z in zip(p,i):
        if z[0] == z[1]:
          common += z[0]
      
      if len(common) == len(i)-1:
        return common
  
  return 'No matching boxes found (something went wrong).'


start_time = timeit.default_timer()
print('Part a: {}\t({}s)'.format(part_a(puzzle_input),round(timeit.default_timer()-start_time,2)))

start_time = timeit.default_timer()
print('Part b: {}\t({}s)'.format(part_b(puzzle_input),round(timeit.default_timer()-start_time,2)))
