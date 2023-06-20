# Spellcasters board, 5x5 with letters in each position. Words can be made from diagonals and up and down

class Board:
    def __init__(self):
        # Index as board[row][col]
        self.board = [["", "", "", "", ""] for i in range(5)]

        self.letter_values = {"a": 1, "e": 1, "i": 1, "o": 1,
                              "n": 2, "r": 2, "s": 2, "t": 2,
                              "d": 3, "g": 3, "l": 3,
                              "b": 4, "h": 4, "p": 4, "m": 4, "u": 4, "y": 4,
                              "c": 5, "f": 5, "v": 5, "w": 5,
                              "k": 6,
                              "j": 7, "x": 7,
                              "q": 8, "z": 8}
        
        # Set of tiles with double letter
        self.DL = {}

        # Set of tiles with triple letter
        self.TL = {}

        # Set of tiles with gems
        self.gems = {}

        # Set of tiles with 2x
        self.doubles = {}

        # Long word bonus (applied after 2x)
        self.long_word_bonus = 10

    def set_board(self, board):
        self.board = board
    
    def get(self, row: int, col: int) -> str:
        return self.board[row][col]
    
    def get_val(self, row: int, col: int) -> int:
        return self.letter_values[self.get(row, col)]

    def get_neighbours(self, row: int, col: int) -> str:
        # Get the surrounding letters of a tile
        letters = {}

        # Assert row, col in range
        assert 0 <= row <= 4 and 0 <= col <= 4

        for row_off, col_off in [(-1, -1), (-1, 0), (-1, 1), 
                                 (0, -1), (0, 1),
                                 (1, -1), (1, 0), (1, 1)]:

            if 0 <= row + row_off <= 4 and 0 <= col + col_off <= 4:
                letter = self.get(row + row_off, col + col_off)
                position = (row + row_off, col + col_off)
                letters[letter] = position
        
        return letters
    
    def get_word_value(self, tiles: list) -> int:
        # Assumes that the tiles list forms a valid word, and that the tiles list forms a valid sequence of tiles (e.g. connected)
        val = 0
        double = False

        for tile in tiles:
            if tile in self.DL:
                val += 2 * self.get_val(*tile)
            elif tile in self.TL:
                val += 3 * self.get_val(*tile)
            else:
                val += self.get_val(*tile)
            
            if tile in self.doubles:
                double = True
        
        if double: 
            val *= 2
        if len(tiles) >= 6:
            val += 10
        
        return val


if __name__ == "__main__":
    board = Board()
    board.set_board([["a", "b", "c", "d", "e"],
                     ["f", "g", "h", "i", "j"],
                     ["j", "k", "l", "m", "n"],
                     ["o", "p", "q", "r", "s"],
                     ["t", "u", "v", "w", "x"]])
    
    print(board.get_neighbours(4, 0))

    tile = (1, 2)
    print(board.get_neighbours(*tile))

    neighbours = board.get_neighbours(*tile)
    for letter in neighbours:
        print(neighbours[letter])