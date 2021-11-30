class Playground():

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        self.playground = [[False for _ in range(width)] for _ in range(height)]
        self.draw_field()

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
        self.draw_field()

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


class GameController():

    def __init__(self) -> None:
        pass

    def get_turn_player(playground: Playground) -> tuple[int, int]:
        return ''

    def set_field_size():




class Participant():

    def __init__(self) -> None:
        pass


class Player(Participant):

    def __init__(self) -> None:
        super().__init__()


class Computer(Participant):

    def __init__(self) -> None:
        super().__init__()


def main():
    field = Playground(3, 3)
    # field.add_block(3, 3)
    x = [1, 0, 2, 0, 2, 1]
    y = [1, 0, 2, 2, 0, 1]
    for each_X, each_Y in zip(x, y):
        if not field.is_blocked(each_X, each_Y) and not field.is_full():
            field.add_block( each_X, each_Y)
        else:
            print('DUUUUUUUUUUDE')

if __name__=='__main__':
    main()