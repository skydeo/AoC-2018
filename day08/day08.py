import timeit

test = False

input_file = '08.in' if not test else '08_test.in'

with open(input_file, 'r') as f:
  puzzle_input = list(map(int, f.read().split()))


def sum_metadata(nodes):
  checksum = 0

  child_nodes = nodes.pop(0)
  metadata_entries = nodes.pop(0)

  if child_nodes == 0:
    checksum += sum(nodes.pop(0) for _ in range(metadata_entries))
  else:
    checksum += sum(sum_metadata(nodes) for _ in range(child_nodes)) + sum(nodes.pop(0) for _ in range(metadata_entries))
  
  return checksum


checksum = sum_metadata(puzzle_input)

print(f"Sum of all metadata entries: {checksum}.")
