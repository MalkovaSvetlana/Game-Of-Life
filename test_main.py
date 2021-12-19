import unittest
import pygame
class Cell_TestCase(unittest.TestCase):

    def test_Neighbors(self):
        cells = []
        size = 10
        self.size = size
        width = 500
        self.width = width
        self.width_posiition = self.width // size
        height = 400
        self.height = height
        self.height_position = self.height // size

        neighbors = []
        neighbors_list = [[0, 1], [1, 0], [0,-1], [-1,0], [1,-1], [-1,1], [1, 1], [-1,-1]]
        for neighbor in neighbors_list:
            neighbor[0] += self.width_posiition
            neighbor[1] += self.height_position
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= len(cells[0]) or neighbor[1] >= len(cells):
                continue
            neighbors.append(cells[neighbor[1]][neighbor[0]])
        self.assertEqual()
    

    def test_update(self):
        living_neigbhors = 0
        neighbors = [1, 2, 4]
        for neighbor in self.neighbors:
            if neighbor.alive:
                living_neigbhors += 1
        if self.alive:
            if living_neigbhors < 2 or living_neigbhors > 3:
                self.continues_living = False
            else:
                self.continues_living = True
        else:
            if living_neigbhors == 3:
                self.continues_living = True
            else:
                self.continues_living = False
        self.assertEqual(neighbors, False)
    

    def test_draw(self):
        boarders = False
        self.alive = False
        cell_colour = (255, 255, 255)
        boarders_colour = (20, 20, 20)
        screen_size = (700, 400)
        display = pygame.Surface(screen_size)

        if self.alive:
            pygame.draw.rect(display, cell_colour, self.rect)
        else:
            if boarders:
                pygame.draw.rect(display, boarders_colour, self.rect, 1)
        self.assertEqual()

if __name__ == "__main__":
    unittest.main()