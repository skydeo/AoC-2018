import timeit
import string

with open('05.in', 'r+') as f:
  puzzle_input = f.read().strip()

test_input = 'dabAcCaCBAcCcaDA'

def find_and_replace_units(string_input):
  for i, char in enumerate(string_input[:-1]):
    next_char = string_input[i+1]

    if char != next_char and char.lower() == next_char.lower():
      replaced_string = string_input.replace(char+next_char, '')
      return (False, replaced_string)

  return (True, string_input)

def react_all_units(string_input):
  done = False
  while not done:
    (done, string_input) = find_and_replace_units(string_input)

  return string_input


def part_a(puzzle_input):
  return react_all_units(puzzle_input)


def part_b(puzzle_input):
  reacted_length = {}

  for pair in zip(string.ascii_lowercase, string.ascii_uppercase):
    replaced_string = puzzle_input.replace(pair[0], '')
    replaced_string = replaced_string.replace(pair[1], '')

    reacted_length[pair[0]] = len(react_all_units(replaced_string))
  
  return min(reacted_length.values())


start_time = timeit.default_timer()
result_a = part_a(puzzle_input)
print('All reactions complete. {} units remain.\t({}s)'.format(len(result_a), round(timeit.default_timer()-start_time, 2)))

start_time = timeit.default_timer()
result_b = part_b(puzzle_input)
print('The most reacted polymer is {} units.\t({}s)'.format(result_b, round(timeit.default_timer()-start_time, 2)))
