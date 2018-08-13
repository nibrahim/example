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


def test_sum_of_neighbors():

    assert game_of_life.sum_of(2, 1) == 2
    

def test_if_alive():
    assert game_of_life.if_alive(2,1) == 1

def test_if_alive_sides():
    assert game_of_life.if_alive(3,3) == 0

def test_if_alive_left_mid():
    assert game_of_life.if_alive(2,0) == 1

def test_if_alive_right_mid():
    assert game_of_life.if_alive(2,3) == 0


def test_if_dead():
    assert game_of_life.if_dead(2,0) == 1

