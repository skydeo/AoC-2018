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


def part_a(puzzle_input, cloth_dimensions, cloth_char = '.'):
  puzzle_input = clean_input(puzzle_input)

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
  
  return sum(row.count('X') for row in cloth)


print('{} square inches are within 2+ claims.'.format(part_a(puzzle_input, (1000, 1000))))

