from random import choice, shuffle


def play_game(user_choice, user_switch):
    # Define doors and prizes
    doors = [1, 2, 3]
    prizes = ['car', 'zonk1', 'zonk2']
    shuffle(prizes)
    doors = list(zip(doors, prizes))

    # Ask contestant to choose a door
    # user_choice = int(input("Please choose a door (1-3)\n"))

    # Reveal a door (not the car and not their choice)
    reveal_options = [i for i in doors if i[0] != user_choice and i[1] != 'car']
    revealed = choice(reveal_options)
    # print(f'The car is NOT behind door number {revealed[0]}!')

    # Ask contestant if they want to switch or stay with their initial choice
    # user_switch = input('Would you like to switch your choice? (y/n)\n')
    if user_switch == 'y':
        user_choice = next(i[0] for i in doors if i[0] != user_choice and i != revealed)

    # Reveal the outcome
    car = next(i[0] for i in doors if i[1] == 'car')
    if car == user_choice:
        # print('You won a NEW CAR!!!')
        return 'win'
    else:
        # print('Sorry, you picked incorrectly.')
        return 'lose'


results = []
for i in range(10000):
    choices = [1, 2, 3]
    result = play_game(choice(choices), 'y')
    results.append(result)

print(f"Win: {results.count('win') / len(results) * 100}%")
print(f"Loss: {results.count('lose') / len(results) * 100}%")
