import pygame
import sys

# здесь определяются константы,
# классы и функции
FPS = 60

SC_WIDTH = 800
SC_HEIGHT = 500
SKY = (127, 199, 255)
WHITE = (255, 255, 255)
# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))  # переменная нашего окна
pygame.display.set_caption('Dancing Red Robot')

clock = pygame.time.Clock()

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # заливаем фон
    sc.fill(SKY)



    # --------
    # изменение объектов
    r = pygame.Rect(0, 480, 800, 20)
    pygame.draw.rect(sc, WHITE, r, 0)
    # обновление экрана
    pygame.display.update()
