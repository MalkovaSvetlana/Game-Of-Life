import pygame
import sys

#   задание парметров экрана (ширина, высота), ращмера клетки, fps - количество обновлений жизни клетки в секунду
screen_size = width, height = (820, 580)
cell_size = 10
fps = 10

screen = pygame.display.set_mode(screen_size)
display = pygame.Surface(screen_size)
clock = pygame.time.Clock()

#   задание цвета для дисплея, границ и клеток
display_colour = (0, 0, 0)
boarders_colour = (20, 20, 20)
cell_colour = (255, 255, 255)

code = True
playing = True
left_mouse_button = False
right_mouse_button = False
boarders = False
cells = []
rows = width // cell_size
columns = height // cell_size

pygame.display.set_caption('Game Of Life')

class GameOfLife():
    def __init__(self, width, height, size):
        '''конструктор принимает ширину, высоту, размер, состояние, координаты по ox и oy
    '''
        #   частичное заимствование
        self.width = width
        self.height = height
        self.size = size
        self.alive = False
        self.width_posiition = self.width // size
        self.height_position = self.height // size
        self.rect = pygame.Rect(width, height, size, size)
        #   конец частичного заимствования

    def Neighbors(self, cells):
        '''находит среди всех возможных соседних 8 клеток существующие
    return положения всех существующих "соседей" клетки
    '''
        neighbors = []
        neighbors_list = [[0, 1], [1, 0], [0,-1], [-1,0], [1,-1], [-1,1], [1, 1], [-1,-1]]
        for neighbor in neighbors_list:
            neighbor[0] += self.width_posiition
            neighbor[1] += self.height_position
            #   заимствование
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= len(cells[0]) or neighbor[1] >= len(cells):
                continue
            neighbors.append(cells[neighbor[1]][neighbor[0]])
        return neighbors
            #   конец заимствования

    def update(self):
        '''обновляет состояние (жизнь/смерть) клетки, основываясь на количестве "соседей" этой клетки
    '''
        living_neigbhors = 0
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

    def draw(self, display):
        '''отрисовывает границы и клетки на основе введённых цветов и размеров
    '''
        if self.alive:
            pygame.draw.rect(display, cell_colour, self.rect)
        else:
            if boarders:
                pygame.draw.rect(display, boarders_colour, self.rect, 1)

#   заимствование
for i in range(columns):
    cells.append([GameOfLife(j*cell_size, i*cell_size, cell_size) for j in range(rows)])

for columns in cells:
    for cell in columns:
        cell.neighbors = cell.Neighbors(cells)
#   конец заимствования

def draw():
    '''заполняет экран заданным цветом и отрисовывает клетки, обновляя экран
'''
    display.fill(display_colour)

    for row in cells:
        for cell in row:
            cell.draw(display)

    screen.blit(display, (0, 0))

    pygame.display.update()

while code:

    ox, oy = pygame.mouse.get_pos()

    if not playing:
        clock.tick(fps)

    if not playing:
        for row in cells:
            for cell in row:
                cell.update()

        for row in cells:
            for cell in row:
                cell.alive = cell.continues_living

    for event in pygame.event.get():
        #   если происходит выход из программы, она закрывается и перестаёт работать
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            #   если нажимается клавиша b, появляются (при нечётном количестве нажатий) и исчезают (при чётном) границы кеток
            if event.key == pygame.K_b:
                boarders = not boarders

        if playing:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_mouse_button = True
                if event.button == 3:
                    right_mouse_button = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    left_mouse_button = False
                if event.button == 3:
                    right_mouse_button = False                    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = False
                #   полностью удаляет все живые клетки с поля (происходит только в состоянии паузы)
                if event.key == pygame.K_BACKSPACE:
                    for columns in cells:
                        for cell in columns:
                            cell.alive = False

            if left_mouse_button:
                #   при нажатии лкм появляется новая живая клетка, на которую указывает курсор (происходит только в состоянии паузы)
                  cells[oy // cell_size][ox // cell_size].alive = True
            if right_mouse_button:
                #   при нажатии пкм убирается живая клетка, на которую указывает курсор (происходит только в состоянии паузы)
                  cells[oy // cell_size][ox // cell_size].alive = False
        else:
            #   при нажатии пробела (нечётное количество раз) программа начинает работать или, наоборот, встаёт на паузу (чётное количество нажатий)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = True

    draw()