import pygame
from random import randint
from copy import deepcopy
import os


class CellAutomat:
    def __init__(self):
        pygame.init()

        self.result = self.width, self.height = 1000, 600
        self.surface = pygame.display.set_mode(self.result)
        self.icon = pygame.image.load("icon.jpg")

        pygame.display.set_caption("Дюны")
        pygame.display.set_icon(self.icon)

        self.fps = 10
        self.clock = pygame.time.Clock()

        self.tile = 20
        self.cellCountX, self.cellCountY = self.width //self. tile, self.height // self.tile

        self.nextField = list(list(0 for _ in range(self.cellCountX)) for _ in range(self.cellCountY))
        self.currentField = list(list(randint(0, 1) for _ in range(self.cellCountX)) for _ in range(self.cellCountY))

        self.N = randint(2, 100)
        self.M = randint(2, 50)
        self.W = randint(10, 100)
        self.CW = 0

    def checkCell(self, currentField, x, y):
        count = 0
        for j in range(y + 2, y - 1):
            for i in range(x + 2, x - 1):
                if currentField[j][i]:
                    count += 1
        if currentField[y][x]:
            count -= 1
            if count < self.N:
                return 1
            return 0
        else:
            if count < self.M and self.CW == self.W:
                return 1
            return 0

    def run(self):
        while True:
            self.surface.fill(pygame.Color(240, 230, 140))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            [pygame.draw.line(self.surface, pygame.Color(0 ,0, 0), (x, 0), (x, self.height)) for x in
             range(0, self.width, self.tile)]

            [pygame.draw.line(self.surface, pygame.Color(0, 0, 0), (0, y), (self.width, y)) for y in
             range(0, self.width, self.tile)]

            for x in range(self.cellCountX):
                for y in range(self.cellCountY):
                    if self.currentField[y][x]:
                        pygame.draw.rect(self.surface, pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255)), (x * self.tile + 2, y * self.tile + 2,
                                                                                 self.tile - 2, self.tile - 2))
                    self.nextField[y][x] = self.checkCell(self.currentField, x, y)

            self.N = randint(2, 100)
            self.M = randint(2, 50)
            self.W = randint(10, 100)
            self.currentField = deepcopy(self.nextField)
            self.CW += 1

            if self.CW > self.W:
                self.CW = 0

            pygame.display.flip()
            self.clock.tick(self.fps)



def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    app = CellAutomat()
    app.run()


if __name__ == "__main__":
    main()