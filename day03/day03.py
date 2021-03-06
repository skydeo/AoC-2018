import timeit

debug = False

with open('input.txt', 'r+') as f:
  puzzle_input = [i for i in f.read().splitlines()]

test_input = '''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2'''.splitlines()


def clean_input(input_list):
  cleaned_input = []

  for item in input_list:
    item = item.replace('#','').replace('@ ','').replace(':','').split(' ')
    cleaned_row = []
    cleaned_row.append(int(item[0]))
    cleaned_row.append(tuple(list(map(int, item[1].split(',')))))
    cleaned_row.append(tuple(list(map(int, item[2].split('x')))))

    cleaned_input.append(cleaned_row)

  return cleaned_input


def create_cloth(dimensions, char='.'):
  cloth = []
  
  for _ in range(0, dimensions[0]):
    cloth.append([char] * dimensions[1])

  return cloth


def print_cloth(cloth):
  for r in cloth:
    print(r)


def process_cloth(puzzle_input, cloth_dimensions, cloth_char = '.'):
  cloth = create_cloth(cloth_dimensions, cloth_char)

  if debug:
    print_cloth(cloth)
    print('Created new cloth.')

  for row in puzzle_input:
    ins = row[0]
    coords = row[1]
    size = row[2]

    if debug:
      print('Ins #{}: marking a {}x{} section at ({},{})'.format(ins, *size, *coords))

    for y in range(coords[0], coords[0]+size[0]):
      for x in range(coords[1], coords[1]+size[1]):
        cloth[x][y] = ins if cloth[x][y] == cloth_char else 'X'
    
    if debug:
      print_cloth(cloth)
  
  return cloth


def part_a(puzzle_input, cloth_dimensions):
  puzzle_input = clean_input(puzzle_input)
  cloth = process_cloth(puzzle_input, cloth_dimensions)

  return sum(row.count('X') for row in cloth)

def part_b(puzzle_input, cloth_dimensions):
  puzzle_input = clean_input(puzzle_input)
  cloth = process_cloth(puzzle_input, cloth_dimensions)

  for row in puzzle_input:
    ins = row[0]
    size = row[2][0] * row[2][1]

    if sum(row.count(ins) for row in cloth) == size:
      return ins

start_time = timeit.default_timer()
part_a = part_a(puzzle_input, (1000, 1000))
run_time = round(timeit.default_timer()-start_time, 2)
print('{} square inches are within 2+ claims.\t({}s)'.format(part_a, run_time))

start_time = timeit.default_timer()
part_b = part_b(puzzle_input, (1000, 1000))
run_time = round(timeit.default_timer()-start_time, 2)
print('Claim {} is intact.\t({}s)'.format(part_b, run_time))

