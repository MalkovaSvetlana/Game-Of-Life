import unittest
import sys
import pygame
from main import Neighbors, update, draw, draw_display
class Cell_TestCase(unittest.TestCase):
    '''Тесты для функций класса GameOfLife
        '''
    cells = []
    def test_Neighbors(self):
        neighbors = []
        neighbors_list = [[0, 1], [1, 0], [0,-1], [-1,0], [1,-1], [-1,1], [1, 1], [-1,-1]]
        for neighbor in neighbors_list:
            neighbor[0] += self.width_posiition
            neighbor[1] += self.height_position
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= len(cells[0]) or neighbor[1] >= len(cells):
                continue
            neighbors.append(cells[neighbor[1]][neighbor[0]])
        self.assertEqual()

def test_draw1(self):
    self.assertEqual(pygame.display.update())

if __name__ == "__main__":
    unittest.main()