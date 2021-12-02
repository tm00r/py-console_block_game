import re
import random as rand


class Playground():

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        self.playground = [[False for _ in range(width)] for _ in range(height)]


    def get_field(self):
        return self.playground

    def draw_field(self) -> None:
        print()
        for row in self.playground:
            for elem in row:
                print('#', end = ' ') if elem else print('.', end = ' ')
            print()
        print()

    def add_block(self, tuple) -> None:
        x, y = tuple   #repeat :(
        valid_i, valid_j = self.block_pos_validator(tuple)
        for row in valid_i:
            self.playground[row][y] = True
        for col in valid_j:
            self.playground[x][col] = True

    def is_blocked(self, tuple) -> bool:
        x, y = tuple   #repeat :(
        return self.playground[x][y]

    def block_pos_validator(self,  tuple):
        valid_col = []
        valid_row = []
        x, y = tuple   #repeat :(
        for col, row in zip(range(x-1, x+2), range(y-1, y+2)):
            if 0 <= col <= self.width - 1:
                valid_col.append(col)
            if 0 <= row <= self.height - 1:
                valid_row.append(row)
        return valid_col, valid_row

    def is_full(self) -> bool:
        return all(sum(row) == self.width for row in self.playground)



class Game():

    def __init__(self) -> None:
        self.name = 'Blocking Game'

    def welcome(self):
        print(f'Welcome to the {self.name}')

    @staticmethod
    def choose_players():
        players = []
        for i in range(1,3):
            print()
            print(f"Who will play {'first' if i == 1 else 'second'}?")
            print('''Select a player:
                0: User
                1: Step-by-step strategy
                2: Random strategy
                3: Maximum blocking strategy
                4: Minimum blocking strategy
                5: Nice-End strategy''')
            players.append(integer_value(f"{'First' if i == 1 else 'Second'} player: ", 0, 5))
        return tuple(players)

    def play(self):
        self.welcome()

        end_game_status = False
        round_number = 1

        width = integer_value('Please enter the width of the plan: ', 2, 100)
        height =  integer_value('Please enter the height of the plan: ', 2, 100)
        field = Playground(width, height)

        player_types = Game.choose_players()
        players = [Player(player_types[i]) for i in range(2)]

        field.draw_field()

        while not end_game_status:

            for player in players:
                if field.is_full():
                    end_game_status = True
                else:
                    print(f"Round: {round_number}. It's {player.name} turn")
                    while 1:
                        point = player.do_your_strategy(field.get_field())
                        if field.is_blocked(point):
                            print(f'The point {point} is already blocked')
                        else:
                            field.add_block(point)
                            print(f'{player.name} blocked point {point}')
                            field.draw_field()
                            break
                    round_number += 1
        return f'{player.name} WON this game'



class Player():

    namespace = {
                    'User': 0,
                    'Computer_with_Step-by-step_strategy': 0,
                    'Computer_with_Random_strategy': 0,
                    'Computer_with_MaxBlock_strategy': 0,
                    'Computer_with_MinBlock_strategy': 0,
                    'Computer_with_NiceEnd_strategy': 0
                }

    def __init__(self, type):
        name, strategy = Player.choose_strategy(type)
        self.name = name
        self.strategy = strategy

    def do_your_strategy(self, field):
        return self.strategy.execute_strategy(field)

    @staticmethod
    def choose_strategy(type):
        name = list(Player.namespace.keys())[type]
        Player.namespace[name] += 1
        if Player.namespace[name] > 1:
            name +='_2'

        match type:                 # Python 3.10.0+ is REQUIRED for 'match'
            case 0: strategy = HumanStrategy
            case 1: strategy = StrategyСoherent
            case 2: strategy = StrategyRandom
            case 3: strategy = StrategyMaxBlock
            case 4: strategy = StrategyMinBlock
            case 5: strategy = StrategyNiceEnd

        # strategy = {              # Python 3.10.0+ is NOT required for this
        #             0: HumanStrategy,
        #             1: StrategyСoherent,
        #             2: StrategyRandom,
        #             3: StrategyMaxBlock,
        #             4: StrategyMinBlock,
        #             5: StrategyNiceEnd,
        #     }.get(type)

        return name, strategy


class Strategy():

    def __init__(self, strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self, field):
        return self._strategy.execute_strategy(field)

class HumanStrategy(Strategy):
    def execute_strategy(field):
        return tuple_value('Enter a point coordinates (row space column): ', len(field[0]), len(field))

class StrategyСoherent(Strategy):
    def execute_strategy(field):
        for i, row in enumerate(field):
            for j in range(len(row)):
                if not row[j]:
                    return (i, j)

class StrategyRandom(Strategy):
    def execute_strategy(field):
        while 1:
            row = rand.randint(0, len(field[0]) - 1)
            col = rand.randint(0, len(field) - 1)
            if not field[row][col]:
                return (row, col)

#
class StrategyMaxBlock(Strategy):
    def execute_strategy(field):
        max_sum = 0
        sum = 0
        for row in range(1, len(field[0]) - 1):
            for col in range(1, len(field) - 1):
                if not field[row][col]:
                    sum += 1
                    if not field[row-1][col]:
                        sum += 1
                    if not field[row+1][col]:
                        sum += 1
                    if not field[row][col-1]:
                        sum += 1
                    if not field[row][col+1]:
                        sum += 1
                if sum > max_sum:
                    max_sum = sum
                    good_spot = (row, col)
        if max_sum == 0:
            good_spot = Strategy(StrategyСoherent).execute_strategy(field)
        return good_spot

class StrategyMinBlock(Strategy):
    def execute_strategy(field):
        print('StrategyMinBlock executed')
        return None

class StrategyNiceEnd(Strategy):
    def execute_strategy(field):
        print('StrategyNiceEnd executed')
        return None


# I failed to implement this with classes
# Сhecks the entered input for strict matching of the form, checks whether the number do not exceed the limit value. Returns the input as an integer
def integer_value(string, min_val, max_val):
        while 1:
            value = input(string)
            if not bool(re.match(r'\d+$', value)) or not (min_val <= int(value) <= max_val):
                print(f'Input must contain only a number between {min_val} - {max_val}, without any other characters')
            else:
                return int(value)

# I failed to implement this with classes
# Сhecks the input (pair of numbers) for strict matching of the form, checks whether the coordinates do not exceed the limit values. Returns the input as an tuple
def tuple_value(string, max_x, max_y):
    output = f'Input must contain integers without any other characters. X is between 0 - {max_x}, Y is between 0 - {max_y}'
    while 1:
        value = input(string)
        if not bool(re.match(r'\d \d+$', value)):
            print(output)
            continue
        else:
            value = tuple(map(int, value.split(' ')))
            for i, item in enumerate(value):
                if (i == 0 and item > max_x) or (i == 1 and item > max_y):
                    break
                else:
                    return value
        print(output)




def main():
    game = Game()
    print(game.play())

if __name__=='__main__':
    main()