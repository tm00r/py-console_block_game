import re
import random


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

    def welcome(self):
        print(f'Welcome to the {self.name}')

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
            players.append(FilterInput(f"{'First' if i == 1 else 'Second'} player: ").is_integer())
        return tuple(players)

    def play(self):
        self.welcome()

        width = FilterInput('Please enter the width of the plan: ').is_integer()
        height = FilterInput('Please enter the height of the plan: ').is_integer()
        field = Playground(width, height)

        players = Game.choose_players()
        player_1 = Player(players[0])
        player_2 = Player(players[1])

        while not field.is_full():
            field.draw_field()
            while 1:
                step_1 = player_1.do_your_strategy()
                if not field.is_blocked(step_1):
                    field.add_block(step_1)
                    break
                else:
                    print(f'The point {step1} is already blocked')



    # def get_turn_player(playground: Playground) -> tuple[int, int]:
    #     return ''

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
        while 1:
            value = input(self.str)
            if bool(re.match(r'\d \d+$', self.value)):
                self.value = value
                return tuple(map(int, self.value).split(' '))
            else:
                print('Input must contain only a pair of integer numbers separated by a space')


class Player():

    # TotalNumberOfPlayers = 0
    # MAX_Inst = 2

    def __init__(self, type):
        name, strategy = Player.choose_strategy(type)
        self.name = name
        self.strategy = strategy

    # def __new__(cls, type):
    #     if (cls.TotalNumberOfPlayers >= cls.MAX_Inst):
    #         print("ERROR: Cannot create more Players!")
    #         return
    #     player = super().__new__(cls)
    #     player._init_player(Player.choose_strategy(type))
    #     cls.TotalNumberOfPlayers += 1
    #     return player

    # def _init_player(self, name, strategy):
    #     self.name = name
    #     self.strategy = strategy

    def do_your_strategy(self):
        result = Strategy(self.strategy()).execute_strategy()

    @staticmethod
    def choose_strategy(type):
        name = 'Cumputer with'
        match type:
            case 1:
                return 'User', HumanStrategy
            case 2:
                return name, StrategyIterative
            case 3:
                return name, StrategyRandom
            case 4:
                return name, StrategyMaxBlock
            case 5:
                return name, StrategyMinBlock
            case 6:
                return name, StrategyEnding

        # return {
        #         1: HumanStrategy,
        #         2: StrategyIterative,
        #         3: StrategyRandom,
        #         4: StrategyMaxBlock,
        #         5: StrategyMinBlock,
        #         6: StrategyEnding,
        #                 }.get(type)


class Strategy():

    def __init__(self, strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self):
        result = self._strategy.execute_strategy()

    def change_strategy(self, new_strategy):
        self._strategy = new_strategy


class HumanStrategy(Strategy):

    def execute_strategy():
        return FilterInput('Enter a point coordinates (column space row)').is_tuple()

class StrategyIterative(Strategy):

    def execute_strategy(self) -> str:
        print('StrategyIterative executed')

class StrategyRandom(Strategy):

    def execute_strategy(self) -> str:
        print('StrategyRandom executed')

class StrategyMaxBlock(Strategy):

    def execute_strategy(self) -> str:
        print('StrategyMaxBlock executed')

class StrategyMinBlock(Strategy):

    def execute_strategy(self) -> str:
        print('StrategyMinBlock executed')

class StrategyEnding(Strategy):

    def execute_strategy(self) -> str:
        print('StrategyEnding executed')



def main():
    game = Game()
    game.play()

if __name__=='__main__':
    main()