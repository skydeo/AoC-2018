import timeit
from collections import defaultdict
import string

test = False

infile = 'test.in' if test else '07.in'


def prereqs_complete(curr_ins, fin_ins, ins_list):
  for i in (set(ins_list.keys()) - set(list(fin_ins))):
    if curr_ins in ins_list[i]:
      return False
  return True


with open(infile, 'r+') as f:
  puzzle_input = [i for i in f.read().splitlines()]

  ins = defaultdict(list)
  [ins[r[5]].append(r[36]) for r in puzzle_input]

letters = set()
after = set()
for k, v in ins.items():
  letters.add(k)
  letters.update(set(v))
  after.update(set(v))

order = sorted(list(letters - after))[0]

next_ins = sorted(list(letters - after))[1:] if len(sorted(list(letters - after))[1:]) > 0 else ins[order]
while next_ins:
  for i in next_ins:
    if prereqs_complete(i, order, ins):
      order += i
      next_ins.pop(next_ins.index(i))
      break
  next_ins.extend(ins[order[-1]])
  next_ins = sorted(list(set(next_ins)))

print('Part A:',order)
