import re
import random


class Playground():

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        self.playground = [[False for _ in range(width)] for _ in range(height)]

    def draw_field(self) -> None:
        for row in self.playground:
            for elem in row:
                print('#', end = ' ') if elem else print('.', end = ' ')
            print()
        print()

    def add_block(self, x: int, y: int) -> None:
        valid_i, valid_j = self.block_pos_validator(x, y)
        for col in valid_i:
            self.playground[y][col] = True
        for row in valid_j:
            self.playground[row][x] = True


    def is_blocked(self, x: int, y: int) -> bool:
        return self.playground[y][x]

    def block_pos_validator(self,  x: int, y: int):
        valid_col = []
        valid_row = []
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
        self.turn = 0

    # def get_turn_player(playground: Playground) -> tuple[int, int]:
    #     return ''

    def welcome(self):
        print(f'Welcome to the {self.name}')

    def play(self):
        self.welcome()

        width = FilterInput('Please enter the width of the plan: ').is_integer()
        height = FilterInput('Please enter the height of the plan: ').is_integer()
        field = Playground(width, height)

        players = Game.choose_players()

        while not field.is_full():
            field.draw_field()


    @staticmethod
    def choose_players() -> tuple[int, int]:
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
            players.append(FilterInput(f"{'First' if i == 1 else 'Second'} player: ").is_integer())
        return tuple(players)







class FilterInput():

    def __init__(self, str):
        self.name = ""
        self.str = str

    def is_integer(self):
        while 1:
            value = input(self.str)
            if bool(re.match(r'\d+$', value)):
                self.value = value
                return int(self.value)
            else:
                print('Input must contain only a number, without any other characters')

    def is_tuple(self):
        if bool(re.match(r'\d \d+$', self.value)):
            return tuple(map(int, self.get_value()).split(' '))




class Player():



    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type


class User(Player):

    def is_player(self):
        return



class Computer(Player):

    def __init__(self) -> None:
        super().__init__()

    def is_computer(self):
        return True

    def set_strategy(self) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Default()

    def get_strategy(self):
        return self.strategy

    def executeStrategy(self) -> str:
        print(self.strategy.execute())



class Strategy:
    def selection(self) -> None:
        raise NotImplementedError('Strategy must be defined in subclass')

class StrategyIterative(Strategy):

    def executeStrategy(self) -> str:
        print('StrategyIterative executed')

class StrategyRandom(Strategy):

    def executeStrategy(self) -> str:
        print('StrategyRandom executed')

class StrategyMaxBlock(Strategy):

    def executeStrategy(self) -> str:
        print('StrategyMaxBlock executed')

class StrategyMinBlock(Strategy):

    def executeStrategy(self) -> str:
        print('StrategyMinBlock executed')

class StrategyEnding(Strategy):

    def executeStrategy(self) -> str:
        print('StrategyEnding executed')



def main():
    game = Game()
    game.play()

if __name__=='__main__':
    main()