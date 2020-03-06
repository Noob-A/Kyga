import pygame
import tabulate
import sys
import threading
from pygame.locals import *
from playsound import playsound

TILE_SIZE = 40

def playMusic():
  playsound('nyan-cat-nyan-cat.mp3')


threading.Thread(target=playMusic).start()

pygame.init()


class Teacher:
  def __init__(self):
    self.icon = pygame.image.load('kygytsa.png')
    self.x_pos = 680
    self.y_pos = 40
    self.step = 1


class Xsesyshna:
  def __init__(self):
    self.icon = pygame.image.load('xseshna.png')
    self.x_pos = 640
    self.y_pos = 280


class Graphics:
  def __init__(self):
    self.wall = pygame.image.load('wall.png')
    self.door = pygame.image.load('door.png')
    self.table = pygame.image.load('table.png')
    self.floor = pygame.image.load('floor.png')
    self.heart = pygame.image.load('heart.png')
    self.scaf = pygame.image.load('scaf.png')
    self.item_window = pygame.image.load('item_window.png')


class Anim:
  def __init__(self):
    self.pistol_cartrige = pygame.image.load('pistol_cartrige.png')
    self.cannon_cartrige = pygame.image.load('cannon_cartrige.png')
    self.step = 10
    self.max = 680

  def render(self, pistol, cannon, pistol_anim, cannon_anim, x, y, maximum, step):
    if pistol:
      window.blit(pistol_anim, (x, y))
    if cannon:
      window.blit(cannon_anim, (x, y))


class Loading:
  def __init__(self):
    self.delay = 100

  def main(self, time, loading):
    x = 0
    y = 0
    loadteam = pygame.image.load('loadteam1.png')
    if loading:
      window.blit(loadteam, (x, y))
      pygame.time.delay(time)


class Gun:
  def __init__(self, pistol, cannon):
    self.pistol = pistol
    self.cannon = cannon

  def render(self, x, y, pistol, cannon):
    pistol_image = pygame.image.load('pistol_original.png')
    cannon_image = pygame.image.load('bazuka_original.png')
    if pistol == True:
      window.blit(pistol_image, (x, y))
    elif cannon == True:
      window.blit(cannon_image, (x, y))


all_maps = [
  [
    'wwwwnnnnwnnnnwnnnww',
    'wssssssssssssssfffw',
    'wfffffffffffffffff3',
    'wssssssssssssssfff3',
    'wfffffffffffffffffw',
    'wssssssssssssssfffw',
    '4fffffffffffffffffw',
    'wssssssssssssssfffw',
    'wfffffffffffffffffw',
    'wssssssssssssssfffw',
    'wwnwnwnwnwnwnwnwnww',
  ],
  [
    'wwwwwwwwwwwwwwwwwww',
    'wssfffffffffffftffw',
    'wssftftftftftfftffw',
    'wssfffffffffffffff1',
    'wffftftftftftfffff1',
    'wfffffffffffffffffw',
    'wffftftftftftfffff4',
    'wssfffffffffffffffw',
    'wssfffffffffffffffw',
    'wssfffffffffffffffw',
    'wwnwnwnwnwnwnwnwnww',
  ],
  [
    'wwwwwwwww2wwwwwwwww',
    'wfffffffffffffftffw',
    'wffftftftftftfftffw',
    'dfffffffffffffffffd',
    'dffftftftftftfffffd',
    'wfffffffffffffffffw',
    'wffftftftftftfffffw',
    'wfffffffffffffffffw',
    'wfffffffffffffffffw',
    'wfffffffffffffffffw',
    'wwnwnwnwnwnwnwnwnww',
  ],
  [
    'wdwwwwwwwwwwwwdwwwwwwwwwwwwwwwwwwwwwww',
    'wffffffffffffffffffffffffffffffffffffw',
    'wffffffffffffffffffffffffffffffffffffw',
    '1ffffffffffffffffffffffffffffffffffffw',
    'wffffffffffffffffffffffffffffffffffffw',
    'wffffffffffffffffffffffffffffffffffffw',
    '3ffffffffffffffffffffffffffffffffffffw',
    'wffffffffffffffffffffffffffffffffffffw',
    'wffffffffffffffffffffffffffffffffffffw',
    'wffffffffffffffffffffffffffffffffffffw',
    'wwwww2wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
  ]
]


def get_tile_at(x, y, map_idx=-1):
  if map_idx == -1:
    map_idx = curr_map_idx
  xx = int(x / 40)
  yy = int(y / 40)
  if yy < 0 or yy + 1 > len(all_maps[map_idx]):
    return 'z'
  if xx < 0 or xx + 1 > len(all_maps[map_idx][yy]):
    return 'z'
  return all_maps[map_idx][yy][xx]


def get_curr_map():
  return all_maps[curr_map_idx]

def find_door(door_number):
  for m in range(len(all_maps)):
    map = all_maps[m]
    if m != curr_map_idx:
      for y in range(len(map)):
        for x in range(len(map[y])):
          if all_maps[m][y][x] == door_number:
            return m, x, y
  return -1, -1, -1


kygysa = False
xs = False
loading = True
curr_map_idx = 0
pistol = False
cannon = False

teacher = Teacher()
graph = Graphics()
xseshna = Xsesyshna()
load_string = Loading()

xseshna_life = 10

background_color = ((255, 255, 255))
window = pygame.display.set_mode((TILE_SIZE * len(get_curr_map()[0]),
                                  TILE_SIZE * len(get_curr_map())))
pygame.display.set_caption('setting')
window.fill(background_color)


def build_class(cls):
  x, y = 0, 0
  for row in cls:
    for col in row:
      if col == 'w':
        window.blit(graph.wall, (x, y))
      if col == 't':
        window.blit(graph.table, (x, y))
      if col == 'f':
        window.blit(graph.floor, (x, y))
      if col == 'h':
        window.blit(graph.heart, (x, y))
      if col == 'n':
        window.blit(graph.item_window, (x, y))
      if col.isdigit():
        window.blit(graph.door, (x, y))
      if col == 's':
        window.blit(graph.scaf, (x, y))
      x += 40
    y += 40
    x = 0


pygame.key.set_repeat(1, 1)
pygame.mouse.set_visible(1)

i = 0
while loading:
  load_string.main(0, loading)
  pygame.display.flip()
  i += 1
  if i == 5:
    kygysa = True
    loading = False

while 1:

  gun = Gun(pistol, cannon)
  animation = Anim()
  build_class(get_curr_map())
  if kygysa:
    window.blit(teacher.icon, (teacher.x_pos, teacher.y_pos))
  if xseshna_life > 0:
    window.blit(xseshna.icon, (xseshna.x_pos, xseshna.y_pos))
  gun.render(teacher.x_pos, teacher.y_pos + 40, gun.pistol, gun.cannon)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
        if event.key == pygame.K_d or event.key == pygame.K_a:
          dir_x = 1 if event.key == pygame.K_d else -1
          teacher.x_pos = teacher.x_pos + dir_x * (teacher.x_pos % 10)
        if event.key == pygame.K_w or event.key == pygame.K_s:
          dir_y = 1 if event.key == pygame.K_s else -1
          teacher.y_pos = teacher.y_pos + dir_y * (teacher.y_pos % 10)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w or \
        event.key == pygame.K_a or \
        event.key == pygame.K_s or \
        event.key == pygame.K_d:

        newx = teacher.x_pos
        newy = teacher.y_pos

        if event.key == pygame.K_w:
          newy -= teacher.step
        if event.key == pygame.K_d:
          newx += teacher.step
        if event.key == pygame.K_s:
          newy += teacher.step
        if event.key == pygame.K_a:
          newx -= teacher.step

        coords = [
          (newx, newy),
          (newx + 39, newy),
          (newx, newy + 39),
          (newx + 39, newy + 39)
        ]

        ok = True
        for c in coords:
          tile = get_tile_at(c[0], c[1])
          if tile != 'f' and not tile.isdigit():
            ok = False

        if ok:
          curr_x, curr_y = teacher.x_pos, teacher.y_pos
          teacher.x_pos = newx
          teacher.y_pos = newy
          tile = get_tile_at(newx, newy)
          if tile.isdigit():
            m, x, y = find_door(tile)
            x += (newx - curr_x)
            y += (newy - curr_y)
            curr_map_idx = m
            teacher.x_pos = x * TILE_SIZE
            teacher.y_pos = y * TILE_SIZE

      if event.key == pygame.K_1:
        pistol = True
        animation.render(pistol, cannon, animation.pistol_cartrige, animation.cannon_cartrige,
                         teacher.x_pos - 10, teacher.y_pos + 40, animation.max, animation.step)
      else:
        pistol = False
      if event.key == pygame.K_2:
        cannon = True
        animation.render(pistol, cannon, animation.pistol_cartrige, animation.cannon_cartrige,
                         teacher.x_pos - 30, teacher.y_pos + 40, animation.max, animation.step)
      else:
        cannon = False

  pygame.display.flip()
