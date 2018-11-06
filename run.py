import pygame, sys
import numpy as np

class Maze(object):

    player = pygame.image.load('img/player.png')  # importowanie obrazu
    wall = pygame.image.load('img/bricks.png')  # importowanie obrazu
    floor = pygame.image.load('img/light_gray_wool.png')  # importowanie obrazu
    price = pygame.image.load('img/price.png')  # importowanie obrazu
    piece_width = 64
    piece_height = 64
    def __init__(self,display_width, display_height, tab):
        self.display_width = display_width
        self.display_height = display_height
        self.numMaze = tab
        self.display = pygame.display.set_mode((self.display_width, self.display_height))  # tworzenie okna
        self.x = 0
        self.y = 0
        pygame.init()

        crashed = True
        while crashed:  # petla gry

            # instrukcje do wcisnietych przyciskow
            for event in pygame.event.get():  # pobiera wszystkie zdarzenia do zmiennej "event"
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.x += self.piece_width
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.x -= self.piece_width
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.y += self.piece_height
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.y -= self.piece_height
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    crashed = False

            self.changeMaze()
            self.fillMaze()

    def changeMaze(self):

        if self.x >= self.piece_width:
            self.x -= self.piece_width

            loctab = np.zeros(self.numMaze.shape)

            for i in range(self.numMaze.shape[0]): # move blocks
                if i == self.numMaze.shape[0]-1:
                    loctab[:, i] = self.numMaze[:, 0]
                else:
                    loctab[:, i] = self.numMaze[:, i + 1]

            self.numMaze = loctab

        elif self.x <= -self.piece_width:
            self.x += self.piece_width

            loctab = np.zeros(self.numMaze.shape)

            for i in range(self.numMaze.shape[0]):
                if i == 0:
                    loctab[:, i] = self.numMaze[:, self.numMaze.shape[0] - 1]
                else:
                    loctab[:, i] = self.numMaze[:, i - 1]

            self.numMaze = loctab

        if self.y >= self.piece_height:
            self.y -= self.piece_height

            loctab = np.zeros(self.numMaze.shape)

            for i in range(self.numMaze.shape[1]):
                if i == self.numMaze.shape[1]-1:
                    loctab[i] = self.numMaze[0]
                else:
                    loctab[i] = self.numMaze[i + 1]

            self.numMaze = loctab

        elif self.y <= -self.piece_height:
            self.y += self.piece_height

            loctab = np.zeros(self.numMaze.shape)

            for i in range(self.numMaze.shape[1]):
                if i == 0:
                    loctab[i] = self.numMaze[self.numMaze.shape[1] - 1]
                else:
                    loctab[i] = self.numMaze[i - 1]

            self.numMaze = loctab

        return self.numMaze

    def fillMaze(self):

        board_x = self.numMaze.shape[0]
        board_y = self.numMaze.shape[1]

        midle_x = self.display_width / 2 - self.piece_width / 2
        midle_y = self.display_height / 2 - self.piece_height / 2

        first_x = self.display_width / 2 - board_x * self.piece_width / 2
        first_y = self.display_height / 2 - board_y * self.piece_height / 2

        shift_x = 0
        shift_y = 0

        self.display.fill((0, 0, 0))

        for element in self.numMaze.flat:
            if element == 1:
                self.display.blit(self.wall, (first_x + shift_x + self.x, first_y + shift_y + self.y))
            if element == 0:
                self.display.blit(self.floor, (first_x + shift_x + self.x, first_y + shift_y + self.y))
            if element == 2:
                self.display.blit(self.price, (first_x + shift_x + self.x, first_y + shift_y + self.y))

            if shift_x < (self.numMaze.shape[0]-1)*self.piece_width:
                shift_x += self.piece_width
            else:
                shift_x = 0
                shift_y += self.piece_height

        self.display.blit(self.player, (midle_x, midle_y))  # wstawia obiekt w dana lokalizacje
        pygame.display.flip()  # podmienia obrazy

# ---------------------------------------------------------------------------------------------------------------------

tab = np.array([[2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],  # 0
                [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1],  # 1
                [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],  # 2
                [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],  # 3
                [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],  # 4
                [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],  # 5
                [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],  # 6
                [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],  # 7
                [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],  # 8
                [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],  # 9
                [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]]) # 10

m = Maze(1000, 1000, tab)
