import random


lottery_numbers = set(random.sample(range(22), 6))


players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]


top_player = players[0]


def correct_answers(list_answers_lotery: list, list_answers_user: list) -> int:
  return len(list_answers_lotery.intersection(list_answers_user))


for player in players:
  numbers_matched = correct_answers(lottery_numbers, player['numbers'])
  if numbers_matched > correct_answers(lottery_numbers, top_player['numbers']):
    top_player = player


winnings = 100 ** correct_answers(lottery_numbers, top_player['numbers'])


print('{} won {}.'.format(top_player['name'], winnings))