class GamePlayground:

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        self.blocked_row_pos = []
        self.blocked_col_pos = []
        self.playground = [[True for _ in range(width)] for _ in range(height)]
        self.draw_field()

    def draw_field(self) -> None:
        for row in self.playground:
            for elem in row:
                print('.', end = ' ') if elem else print('#', end = ' ')
            print()
        print()

    def add_block(self, x: int, y: int) -> None:
        for i, j in zip(range(x-1, x+2), range(y-1, y+2)):
            if 0 <= i <= self.width - 1:
                self.blocked_pos.append(self.playground[y][i])
                self.playground[y][i] = False
                self.blocked_row_pos.append(self.playground[y][i])
            if 0 <= j <= self.height - 1:
                self.blocked_pos.append(self.playground[j][x])
                self.playground[j][x] = False
                self.blocked_col_pos.append(self.playground[j][x])
        self.draw_field()

    # def is_blocked(self, x: int, y: int) -> bool:


    # def is_full(self) -> bool:



class GameParticipant:

    def __init__(self) -> None:
        pass



class Player(GameParticipant):

    def __init__(self) -> None:
        super().__init__()



def main():
    field = GamePlayground(10, 10)
    # field.add_block(3, 3)
    field.add_block(9, 0)

if __name__=='__main__':
    main()