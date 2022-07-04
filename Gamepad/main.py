import bluetooth
import json
import pygame

pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game")

x = 700
y = 720
weight = 650
height = 40
speed = 10
run = True
stick_press = False

sensor_address = '98:b3:32:21:3b:c0'
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect((sensor_address, 1))


buffer = ""

while True:
    data = socket.recv(1024)
    buffer += str(data, encoding='ascii')


    try:
        data = json.loads(buffer)
        print("Received chunk", data)
        print(data['pinX'])
        buffer = ""


        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if data['pinZ'] < 1000:
            stick_press = not stick_press
        print(stick_press)
        if stick_press == False:
            if data['pinX'] > 515:
                x -= speed
            if data['pinX'] < 505:
                x += speed
            if data['pinY'] < 526:
                y -= speed
            if data['pinY'] > 526:
                y += speed
        else:
            if data['gyrX'] > 2:
                x -= speed
            if data['gyrX'] < 1:
                x += speed
            if data['gyrY'] > 2:
                y -= speed
            if data['gyrY'] < 1:
                y += speed

        pygame.draw.rect(window, (0, 255, 0), (40, 30, 40, 40))

        if x < 80 and y < 100:
            window.fill((0, 0, 0))
            f = pygame.font.SysFont('arial', 80, True, False)
            text = f.render('NEXT LEVEL', 1, (255, 255, 255), (0, 0, 0))
            window.blit(text, text.get_rect(center=(400, 400)))
            i = 185
            while run:
                pygame.time.delay(10)
                i += 1
                pygame.draw.rect(window, (255, 255, 255), (i, 550, 40, 40))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

        if x > 780:
            x = 780
        if x < 20:
            x = 20
        if y > 780:
            y = 780
        if y < 20:
            y = 20

        window.fill((0, 0, 0))
        pygame.draw.circle(window, (0, 0, 255), (x, y), 20)
        pygame.draw.rect(window, (0, 255, 0), (40, 30, 40, 40))
        pygame.draw.rect(window, (255, 0, 0), (0, 100, weight, height))

        if 100 + height + 20 > y > 100 + 20 and x < weight + 10:
            y = 100 + height + 20
        if 100 - 20 < y < 100 + 20 and x < weight + 10:
            y = 100 - 20
        if 100 + height + 18 > y > 100 - 18 and x < weight + 20:
            x = weight + 20

        pygame.draw.rect(window, (255, 0, 0), (150, 200, weight, height))

        if 200 + height + 20 > y > 200 + 20 and x > 800 - weight - 10:
            y = 200 + height + 20
        if 200 - 20 < y < 200 + 20 and x > 800 - weight - 10:
            y = 200 - 20
        if 200 + height + 18 > y > 200 - 18 and x > 800 - weight - 20:
            x = 800 - weight - 20

        pygame.draw.rect(window, (255, 0, 0), (0, 300, weight, height))

        if 300 + height + 20 > y > 300 + 20 and x < weight + 10:
            y = 300 + height + 20
        if 300 - 20 < y < 300 + 20 and x < weight + 10:
            y = 300 - 20
        if 300 + height + 18 > y > 300 - 18 and x < weight + 20:
            x = weight + 20

        pygame.draw.rect(window, (255, 0, 0), (150, 400, weight, height))

        if 400 + height + 20 > y > 400 + 20 and x > 800 - weight - 10:
            y = 400 + height + 20
        if 400 - 20 < y < 400 + 20 and x > 800 - weight - 10:
            y = 400 - 20
        if 400 + height + 18 > y > 400 - 18 and x > 800 - weight - 20:
            x = 800 - weight - 20

        pygame.draw.rect(window, (255, 0, 0), (0, 500, weight, height))

        if 500 + height + 20 > y > 500 + 20 and x < weight + 10:
            y = 500 + height + 20
        if 500 - 20 < y < 500 + 20 and x < weight + 10:
            y = 500 - 20
        if 500 + height + 18 > y > 500 - 18 and x < weight + 20:
            x = weight + 20

        pygame.draw.rect(window, (255, 0, 0), (150, 600, weight, height))

        if 600 + height + 20 > y > 600 + 20 and x > 800 - weight - 10:
            y = 600 + height + 20
        if 600 - 20 < y < 600 + 20 and x > 800 - weight - 10:
            y = 600 - 20
        if 600 + height + 18 > y > 600 - 18 and x > 800 - weight - 20:
            x = 800 - weight - 20

        pygame.display.update()
    except json.JSONDecodeError as e:
        continue


socket.close()