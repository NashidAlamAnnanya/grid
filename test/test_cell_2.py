from ..grid import Cell

def test_bulk():
    """ Test that a cell in the bulk of the grid is correct. """

    # Instantiate a cell in the bulk of a 4x4 grid.
    c = Cell(2, 2, 4, 4)

    # Make sure that the cell has 4 neighbours.
    assert c.neighbours() == 4

    # Check the coordinates of the neighbours.
    assert c.left()  == (1, 2)
    assert c.right() == (3, 2)
    assert c.up()    == (2, 3)
    assert c.down()  == (2, 1)
