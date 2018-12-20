import timeit
import re

test = False

input_file = '10.in' if not test else '10_test.in'

with open(input_file, 'r') as f:
  puzzle_input = [list(map(int, re.findall('-?\d+', l))) for l in open(input_file, 'r').read().splitlines()]

# for r in puzzle_input:
#   print(r)

def bb_size(cv_list, second):
  min_x = min(x + second * vx for (x, y, vx, vy) in cv_list)
  max_x = max(x + second * vx for (x, y, vx, vy) in cv_list)
  min_y = min(y + second * vy for (x, y, vx, vy) in cv_list)
  max_y = max(y + second * vy for (x, y, vx, vy) in cv_list)

  return [max_x, min_x, max_y, min_y]


def smallest_bb_time(puzzle_input):
  min_bb = 1 << 32
  min_s = 0
  bb = []
  
  for s in range(0,100000):
    cur_bb = bb_size(puzzle_input, s)
    cur_bb_size = cur_bb[0] - cur_bb[1] + cur_bb[2] - cur_bb[3]
    if cur_bb_size < min_bb:
      min_bb = cur_bb_size
      min_s = s
      bb = cur_bb
  
  print(f"Smallest bb ({min_bb}) found in second {min_s}\n{bb}.")

  return min_s, bb



def part_a(puzzle_input):
  time, bb = smallest_bb_time(puzzle_input)

  x_lb = bb[1]
  y_lb = bb[3]

  print(x_lb, y_lb)
  
  r = 1
  for t in range(time,time+r):
    max_x, min_x, max_y, min_y = bb_size(puzzle_input, t)
    screen = [['.'] * (max_x+1-x_lb) for _ in range(max_y+1-y_lb)]
    print(f"Screen size is {len(screen[0])} x {len(screen)}.")

    for [x, y, vx, vy] in puzzle_input:
      x_pos = x + t * vx - x_lb
      y_pos = y + t * vy - y_lb
      screen[y_pos][x_pos] = '#'

    print(f"second: {t}")
    for s in screen:
      print(''.join(s))
    print()

part_a(puzzle_input)
  
