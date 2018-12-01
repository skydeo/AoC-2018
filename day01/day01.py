import timeit

with open('input.txt', 'r+') as f:
  input = [int(i.replace('+','')) for i in f.read().splitlines()]

def part_a(input):
  freq = 0
  for df in input:
    freq += df
  
  return freq


def part_b(input):
  freq = 0
  found_freqs = set()

  i = 0
  # while freq not in found_freqs:
  while True:
    freq += input[i%len(input)]
    if freq in found_freqs:
      return freq
    else:
      found_freqs.add(freq)
      i += 1


start_time = timeit.default_timer()
print('Part a: {}\t({}s)'.format(part_a(input),round(timeit.default_timer()-start_time,3)))
start_time = timeit.default_timer()
print('Part b: {}\t({}s)'.format(part_b(input),round(timeit.default_timer()-start_time,3)))
