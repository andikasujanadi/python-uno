import random


def add_pack(deck, color):
    for i in range(10):
        if i!= 0:
            deck.append(f'{i}_{color}')
        deck.append(f'{i}_{color}')
    for i in range(2):
        deck.append(f'stop_{color}')
        deck.append(f'reverse_{color}')
        deck.append(f'+2_{color}')
    deck.append(f'+4_black')
    deck.append(f'colorless_black')

def add_deck(deck):
    add_pack(deck,'red')
    add_pack(deck,'yellow')
    add_pack(deck,'green')
    add_pack(deck,'blue')

def shuffle(deck):
    loop = random.randint(1,10)
    for i in range(loop):
        random.shuffle(deck)

if __name__ == '__main__':
    new_deck = []
    add_deck(new_deck)
    print(new_deck)
    print()
    shuffle(new_deck)
    print(new_deck)