import os
import sys
import pygame
import requests


class Params(object):
    def __init__(self):
        self.ll = '37.530887,55.70311'
        self.lx = "37.530887"
        self.ly = "55.703118"
        self.z = 12
        self.l = "map"

    def up(self):
        if self.z < 17:
            self.z += 1
            print(self.z)

    def down(self):
        if self.z > 1:
            self.z -= 1
            print(self.z)

    def up3(self):
        self.lx = float(self.lx)
        self.lx += 0.2
        self.lx = str(self.lx)
        self.ll = self.lx + "," + self.ly

    def down3(self):
        self.lx = float(self.lx)
        self.lx -= 0.2
        self.lx = str(self.lx)
        self.ll = self.lx + "," + self.ly

    def right(self):
        self.ly = float(self.lx)
        self.ly += 0.2
        self.ly = str(self.ly)
        self.ll = self.lx + "," + self.ly

    def left(self):
        self.ly = float(self.lx)
        self.ly -= 0.2
        self.ly = str(self.ly)
        self.ll = self.lx + "," + self.ly


def load_map(p):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={}&z={}&size=600,450&l={}".format(p.ll, p.z, p.l)
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


pygame.init()
params = Params()
map_file = load_map(params)
screen = pygame.display.set_mode((600, 450))
params = Params()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    map_file = load_map(params)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    key = pygame.key.get_pressed()
    if key[pygame.K_PAGEUP]:
        params.up()
    if key[pygame.K_PAGEDOWN]:
        params.down()
    if key[pygame.K_UP]:
        params.up3()
    if key[pygame.K_DOWN]:
        params.down3()
    if key[pygame.K_LEFT]:
        params.left()
    if key[pygame.K_RIGHT]:
        params.right()

pygame.quit()

os.remove(map_file)
