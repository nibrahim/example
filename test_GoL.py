import game_of_life

def test_return():
    grid = 4
    grid_out = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    #print(grid_out[0][1])
    assert game_of_life.grid(grid) == grid_out

def test_cell_position():
    grid_size = 4
    grid_matrix = game_of_life.grid(grid_size)
    initial_positions = [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]]
    
    assert game_of_life.initial_position() == initial_positions
