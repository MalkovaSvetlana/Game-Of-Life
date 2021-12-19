import unittest
from main import main

class GameOfLife_TestCase(unittest.TestCase):
    '''Тесты для функций класса GameOfLife
        '''
    def test_neighbor(self, cells):
        living_neigbhors = 4
        self.assertEqual(living_neigbhors, False)
