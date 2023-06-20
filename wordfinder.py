# With a board and a Trie, find all words possible
from Board import Board
from Trie import Trie, TrieNode

board = Board()
trie = Trie()

### NO SWAPS
def get_starting_position_words(prefix: str, visited: list(), row: int, col: int) -> list:
    # Get all words that can be made from a given starting position on the board, with given prefix
    words = [] # perhaps better if this is a set rather than a list, and also needs to store the positions of words for TL and 2x

    # DFS on the board and trie
    tile = (row, col)
    
    # for each neighbour that is unvisited get letters that are a proper prefix of a word
    neighbours = board.get_neighbours(*tile)

    # Add word if it is valid
    if trie.is_word(prefix):
        words.append((prefix, visited))

    for letter in neighbours:
        position = neighbours[letter]
        if position in visited or not trie.lookup(prefix + letter):
            # Do nothing if this tile is already visited in this DFS or if it cannot form a word
            pass
        else:
            newvisited = list(visited) # this could just be passed by reference and then removed from after DFS call
            newvisited.append(position)

            # Descend in DFS
            words += get_starting_position_words(prefix + letter, newvisited, *position)
    

    return words

def get_all_words() -> list:
    words = []

    for row in range(5):
        for col in range(5):
            starting_letter = board.get(row, col)
            words += get_starting_position_words(starting_letter, [(row, col)], row, col)
    
    return words

def get_top_words() -> list:
    words = get_all_words()
    
    word_values = [(word, board.get_word_value(tiles)) for (word, tiles) in words]
    word_values.sort(key=lambda x : x[1], reverse=True)

    return word_values

### SWAPS
def get_starting_position_words_swappable(node: TrieNode, visited: list(), swaps: int, row: int, col: int) -> list:
    words = []
    tile = (row, col)
    neighbours = board.get_neighbours(*tile)

    if node.is_word: 
        words.append((node.string, list(visited)))

    # Look at neighbours in trie
    for char in node.children:
        
        # Look at neighbours in board
        for letter in neighbours:
            position = neighbours[letter]

            # If this is unvisited:
            if position not in visited:
                newvisited = list(visited)
                newvisited.append(position)

                newnode = node.children[char]
                # If this letter is the same as the char, this DFS call doesnt use a swap
                if char == letter:
                    words += get_starting_position_words_swappable(newnode, newvisited, swaps, *position)                        
                elif swaps >= 1:
                    words += get_starting_position_words_swappable(newnode, newvisited, swaps-1, *position)
                    
    
    return words

def get_top_words_swappable(no_swaps: int = 0) -> list:
    words = []

    for row in range(5):
        for col in range(5):
            starting_letter = board.get(row, col)

            if starting_letter in trie.root.children:
                starting_node = trie.root.children[starting_letter]
                words += get_starting_position_words_swappable(starting_node, [(row, col)], no_swaps, row, col)
    
    word_values = [(word, board.get_word_value(tiles)) for (word, tiles) in words]
    word_values.sort(key=lambda x : x[1], reverse=True)

    return word_values

def get_top_ten_words_swappable_tiles(no_swaps: int = 0) -> list:
    words = []

    for row in range(5):
        for col in range(5):
            starting_letter = board.get(row, col)

            if starting_letter in trie.root.children:
                starting_node = trie.root.children[starting_letter]
                words += get_starting_position_words_swappable(starting_node, [(row, col)], no_swaps, row, col)
    
    word_values = [(word, board.get_word_value(tiles), tiles) for (word, tiles) in words]
    word_values.sort(key=lambda x : x[1], reverse=True)

    for i in range(10):
        print(word_values[i])

    

if __name__ == "__main__":
    board.set_board([["a", "b", "c", "e", "a"],
                     ["f", "g", "l", "n", "j"],
                     ["j", "k", "l", "m", "n"],
                     ["o", "p", "q", "l", "h"], 
                     ["t", "u", "v", "i", "t"]])
    
    with open("wordlist.txt", "r") as f:
        for i, line in enumerate(f):
            trie.insert(line.strip())
    
    # print(get_top_words())

    print("\n-----------------------------------\n")
    
    # no_swap_words = get_top_words_swappable(0)

    # one_swap_words = get_top_words_swappable(1)

    # required_one_swap_words = [(word, val) for (word, val) in one_swap_words if (word, val) not in no_swap_words]

    # print(required_one_swap_words[:20])

    # zero_swap_words = get_top_words_swappable(0)
    # one_swap_words = get_top_words_swappable(1)
    # two_swap_words = get_top_words_swappable(2)
    # three_swap_words = get_top_words_swappable(3)

    # print(f"no swaps : {len(zero_swap_words)}")
    # print(f"one swap : {len(one_swap_words)}")
    # print(f"two swaps: {len(two_swap_words)}")
    # print(f"three swaps: {len(three_swap_words)}")
    
    # print(zero_swap_words)

    board.set_board([["o", "i", "h", "u", "i"],
                     ["g", "n", "v", "o", "e"],
                     ["i", "g", "e", "q", "e"],
                     ["i", "j", "s", "e", "e"], 
                     ["f", "n", "u", "b", "e"]])
    board.DL = {(0,0)}
    board.doubles = {(2,0)}
    get_top_ten_words_swappable_tiles(1)




