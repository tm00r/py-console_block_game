from operator import index
import re
import random as rand


class Playground():

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        self.playground = [[False for _ in range(width)] for _ in range(height)]

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
        for col in valid_i:
            self.playground[y][col] = True
        for row in valid_j:
            self.playground[row][x] = True

    def is_blocked(self, tuple) -> bool:
        x, y = tuple   #repeat :(
        return self.playground[y][x]

    def not_blocked(self):
        not_blocked = []
        for row in self.playground:
            for elem in row:
                if not elem:
                    not_blocked.append((row.index(elem), self.playground.index(row)))
        return not_blocked

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
        self.field = None

    def welcome(self):
        print(f'Welcome to the {self.name}')

    def set_field(self, field):
        self.field = field

    def get_field(self):
        return self.field

    def play(self):
        self.welcome()
        end_game_status = False
        round_number = 0

        width = FilterInput('Please enter the width of the plan: ').to_integer()
        height = FilterInput('Please enter the height of the plan: ').to_integer()
        self.set_field(Playground(width, height))

        player_types = Game.choose_players()
        players = [Player(player_types[i]) for i in range(2)]

        self.field.draw_field()

        while not end_game_status:

            for player in players:
                if self.field.is_full():
                    end_game_status = True
                else:
                    not_blocked = self.field.not_blocked()
                    while 1:
                        print(f"Round: {round_number}. It's {player.name} turn")
                        step = player.do_your_strategy(not_blocked)
                        if not self.field.is_blocked(step):
                            self.field.add_block(step)
                            self.field.draw_field()
                            break
                        else:
                            print(f'The point {step} is already blocked')
                    round_number += 1


    @staticmethod
    def choose_players():
        players = []
        for i in range(1,3):
            print()
            print(f"Who will play {'first' if i == 1 else 'second'}?")
            print('''Select a player:
                1: User
                2: Step-by-step strategy
                3: Random strategy
                4: Maximum blocking strategies
                5: Minimum blocking strategies
                6: Smart terminator''')
            players.append(FilterInput(f"{'First' if i == 1 else 'Second'} player: ").to_integer())
        return tuple(players)



class FilterInput():

    def __init__(self, str):
        self.name = ""
        self.str = str

    def to_integer(self):
        while 1:
            value = input(self.str)
            if bool(re.match(r'\d+$', value)):
                self.value = value
                return int(self.value)
            else:
                print('Input must contain only a number, without any other characters')

    def to_tuple(self):
        while 1:
            value = input(self.str)
            if bool(re.match(r'\d \d+$', value)):
                self.value = value
                return tuple(map(int, self.value.split(' ')))
            else:
                print('Input must contain only a pair of integer numbers separated by a space')


class Player():

    def __init__(self, type):
        name, strategy = Player.choose_strategy(type)
        self.name = name
        self.strategy = strategy

    def do_your_strategy(self, not_blocked):
        return self.strategy.execute_strategy(not_blocked)

    @staticmethod
    def choose_strategy(type):
        name = 'Cumputer with '
        match type:
            case 1:
                return 'User', HumanStrategy
            case 2:
                return name+"Iterative strategy", StrategyIterative
            case 3:
                return name+"Random strategy", StrategyRandom
            case 4:
                return name+"MaxBlock strategy", StrategyMaxBlock
            case 5:
                return name+"MinBlock strategy", StrategyMinBlock
            case 6:
                return name+"Ending strategy", StrategyEnding

        # return {
        #         1: 'User',HumanStrategy,
        #         2: name, StrategyIterative,
        #         3: name, StrategyRandom,
        #         4: name, StrategyMaxBlock,
        #         5: name, StrategyMinBlock,
        #         6: name, StrategyEnding,
        #                 }.get(type)



class Strategy():

    def __init__(self, strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.execute_strategy()

    def change_strategy(self, new_strategy):
        self._strategy = new_strategy

class HumanStrategy(Strategy):

    def execute_strategy(not_blocked):
        return FilterInput('Enter a point coordinates (column space row): ').to_tuple()

class StrategyIterative(Strategy):

    def execute_strategy(not_blocked):
        return not_blocked[0]

class StrategyRandom(Strategy):

    def execute_strategy(not_blocked):
        return not_blocked[rand.randint(0, len(not_blocked))]

class StrategyMaxBlock(Strategy):

    def execute_strategy(not_blocked):
        print('StrategyMaxBlock executed')

class StrategyMinBlock(Strategy):

    def execute_strategy(not_blocked):
        print('StrategyMinBlock executed')

class StrategyEnding(Strategy):

    def execute_strategy(not_blocked):
        print('StrategyEnding executed')



def main():
    game = Game()
    game.play()

if __name__=='__main__':
    main()