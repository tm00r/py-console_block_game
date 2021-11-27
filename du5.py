class Playground:

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        self.playground = [[True for _ in range(width)] for _ in range(height)]
        self.draw_field()

    def draw_field(self) -> None:
        for row in self.playground:
            for elem in row:
                print('.', end = ' ') if elem else print('#', end = ' ')
            print()
        print()

    def add_block(self, x: int, y: int) -> None:
        valid_i, valid_j = self.block_pos_control(x, y)
        for i, j in zip(valid_i, valid_j):
                self.playground[y][i] = False
                self.playground[j][x] = False
        self.draw_field()

    def is_blocked(self, x: int, y: int) -> bool:
        valid_i, valid_j = self.block_pos_control(x, y)
        return any(
            not self.playground[y][i]
            or
            not self.playground[j][x]
            for i, j in zip(valid_i, valid_j)
        )

    def block_pos_control(self, x, y):
        valid_i = []
        valid_j = []
        for i, j in zip(range(x-1, x+2), range(y-1, y+2)):
            if 0 <= i <= self.width - 1:
                valid_i.append(i)
            if 0 <= j <= self.height - 1:
                valid_j.append(j)
        return valid_i, valid_j

    # def is_full(self) -> bool:



class Participant:

    def __init__(self) -> None:
        pass



class Player(Participant):

    def __init__(self) -> None:
        super().__init__()



def main():
    field = Playground(10, 10)
    # field.add_block(3, 3)
    x, y = 9, 0
    if not field.is_blocked(x, y):
        field.add_block(x, y)
    else:
        print('DUUUUUUUUUUDE')

if __name__=='__main__':
    main()