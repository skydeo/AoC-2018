import timeit
from datetime import datetime
from operator import add

with open('04.in', 'r+') as f:
  puzzle_input = [i for i in f.read().splitlines()]

with open('test.in', 'r+') as f:
  test_input = [i for i in f.read().splitlines()]


def sort_input(puzzle_input):
  datetimes = [[datetime.strptime(r[1:17], '%Y-%m-%d %H:%M'), r[19:]] for r in puzzle_input]
  sorted_input = sorted(datetimes, key=lambda x: x[0])

  return sorted_input

def build_log(text_log):
  guard = None
  sleep_schedule = {}
  sleep_start = None

  for row in text_log:
    text = row[1]
    if '#' in text:
      guard = text.split(' ')[1][1:]
    elif 'falls asleep' in text:
      sleep_start = row[0].minute
    elif 'wakes up' in text:
      wake_up = row[0].minute

      sleep_time = [0] * (sleep_start-1) + [1] * (wake_up - sleep_start) + [0] * (61 - wake_up)
      if guard not in sleep_schedule:
        sleep_schedule[guard] = sleep_time
      else:
        sleep_schedule[guard] = list(map(add, sleep_time, sleep_schedule[guard]))
  
  return(sleep_schedule)
      

def part_a(sleep_schedule):
  time_asleep = {}
  for guard in sleep_schedule:
    time_asleep[guard] = sum(sleep_schedule[guard])
  
  sleepiest = max(time_asleep, key=time_asleep.get)

  return int(sleepiest) * (sleep_schedule[sleepiest].index(max(sleep_schedule[sleepiest])) + 1)


def part_b(sleep_schedule):
  days_asleep = 0
  sleepiest = 0

  for guard in sleep_schedule:
    if max(sleep_schedule[guard]) > days_asleep:
      days_asleep = max(sleep_schedule[guard])
      sleepiest = guard
  
  return int(sleepiest) * (sleep_schedule[sleepiest].index(max(sleep_schedule[sleepiest])) + 1)


start_time = timeit.default_timer()
sleep_schedule = build_log(sort_input(puzzle_input))
print('Sleep schedule built.\t({}s)'.format(round(timeit.default_timer()-start_time, 3)))

start_time = timeit.default_timer()
part_a = part_a(sleep_schedule)
print('Checksum of the sleepiest guard: {}.'.format(part_a))

start_time = timeit.default_timer()
part_b = part_b(sleep_schedule)
print('Checksum of the most regularly sleepy guard: {}.'.format(part_b))
