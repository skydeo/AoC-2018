import timeit
import re
from collections import defaultdict, deque

test = False

# test_input = "23 25"
test_input = "10 1618"

players, points = map(int, re.compile('\d+').findall(open('09.in', 'r+').read().strip() if not test else test_input))



def rotate_to_index(bad_list, starting_value):
  return bad_list[bad_list.index(starting_value):] + bad_list[:bad_list.index(starting_value)]


def play_game(num_players, last_marble):
  print(f"Playing a game\n{'-'*(13+len(str(last_marble)))}\nPlayers:     {num_players}\nLast marble: {last_marble}\n")

  scores = defaultdict(int)
  circle = [0]
  c_marble = 0

  for x in range(1,last_marble+1):
    c_player = (x % num_players) or num_players

    if (x % 23) != 0:
      insert_pos = (circle.index(c_marble) + 2) % len(circle)
      circle.insert(insert_pos, x)
      c_marble = x
      scores[c_player] += 0
    else:
      scores[c_player] += x
      pop_pos = (circle.index(c_marble) - 7) % len(circle)
      pop_value = circle.pop(pop_pos)
      scores[c_player] += pop_value
      c_marble = circle[pop_pos % len(circle)]

  return(scores)

def play_game_faster(num_players, last_marble):
  print(f"Playing a game\n{'-'*(13+len(str(last_marble)))}\nPlayers:     {num_players}\nLast marble: {last_marble}\n")

  scores = defaultdict(int)
  circle = deque([0])
  c_marble = 0

  for x in range(1,last_marble+1):

    if (x % 23) != 0:
      circle.rotate(-1)
      circle.append(x)
    else:
      circle.rotate(7)
      c_player = (x % num_players) or num_players
      scores[c_player] += x + circle.pop()
      circle.rotate(-1)

  return(scores)


start_time = timeit.default_timer()
part_a = play_game(players, points)
run_time = round(timeit.default_timer()-start_time,2)
print(f"Player {max(part_a, key=part_a.get)} won with a max score of {max(part_a.values())}.\t({run_time}s)\n")

start_time = timeit.default_timer()
part_b = play_game_faster(players, points * 100)
run_time = round(timeit.default_timer()-start_time,2)
print(f"Player {max(part_b, key=part_b.get)} won with a max score of {max(part_b.values())}.\t({run_time}s)\n")
