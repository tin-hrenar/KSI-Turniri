import pygame
import pygame_textinput
from sys import exit
'''Ideju i pomoc za popup window dao Ivan Golek'''
def blit_button(rect, text, screen):
    t = (rect.x+rect.w/2-10, rect.y+rect.h/2-15)
    screen.blit(text, t)
    pygame.draw.rect(screen, 'White', rect, width = 3)

def blit_button2(rect, text, screen):
    t = (rect.x, rect.y)
    screen.blit(text, t)
    pygame.draw.rect(screen, 'White', rect, width = 3)

def popup():
    print('popup')
    pygame.init()
    
    screen2 = pygame.display.set_mode((300, 200))
    pygame.display.set_caption('Jeste li sigurni?')
    clock = pygame.time.Clock()
    start_font = pygame.font.SysFont('Comic Sans MS', 20)

    pozadina = pygame.image.load('pozadina.png')

    sure_text = start_font.render('Jeste li sigurni?', True, 'White')
    sure_rect = sure_text.get_rect(center = (150, 70))
    da_text = start_font.render('Da', True, 'White')
    da_rect = sure_text.get_rect(center = (150, 130))
    ne_text = start_font.render('Ne', True, 'White')
    ne_rect = sure_text.get_rect(center = (150, 165))

    #print('sure:', sure_rect.x, sure_rect.y, sure_rect.w, sure_rect.h)
    #print('da:', da_rect.x, da_rect.y, da_rect.w, da_rect.h)
    #print('ne:', ne_rect.x, ne_rect.y, ne_rect.w, ne_rect.h)


    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == True:
            if da_rect.collidepoint(mx, my):
                return 1
            elif ne_rect.collidepoint(mx, my):
                return 0
                
    #    print('pos: ', mx, my)
    #    print('sure:', sure_rect.x, sure_rect.y, sure_rect.w, sure_rect.h)
    #    print('da:', da_rect.x, da_rect.y, da_rect.w, da_rect.h)
    #    print('ne:', ne_rect.x, ne_rect.y, ne_rect.w, ne_rect.h)
        screen2.blit(pozadina, (0, 0))
        screen2.blit(sure_text, sure_rect)
        blit_button(da_rect, da_text, screen2)
        blit_button(ne_rect, ne_text, screen2)
        pygame.display.update()
        clock.tick(60)

def popup2():
    pygame.init()
    
    screen2 = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Upisivanje imena')
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont('Comic Sans MS', 25)
    end_font = pygame.font.SysFont('Comic Sans MS', 50)
    textinput = pygame_textinput.TextInputVisualizer(font_color = 'White')
    red = 0
    lista = []
    info_text = text_font.render('Upišite imena timova, svako u svojem redu.', True, 'White')
    info_rect = info_text.get_rect(topleft = (10, 0))
    end_text = end_font.render('Završi upis', True, 'White')
    end_rect = end_text.get_rect(topleft = (700, 100))
    pygame.key.set_repeat(200, 25)
    while True:
        screen2.fill((106, 106, 106))
#        print(textinput.value)
        events = pygame.event.get()
        textinput.update(events)
        
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                lista.append(textinput.value)
                textinput.value = ''
                red += 30

        for i in range(len(lista)):
            text = text_font.render(str(lista[i]), True, 'White')
            screen2.blit(text, (10, 30+i*30))

        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == True:
            if end_rect.collidepoint(mx, my):
                return lista

        blit_button2(end_rect, end_text, screen2)
        pygame.draw.rect(screen2, 'White', end_rect, width = 3)
        screen2.blit(info_text, info_rect)
        screen2.blit(textinput.surface, (10, 40+red))
        pygame.display.update()
        clock.tick(60)
        
    

if __name__ == '__main__':
    popup()
    pygame.quit()
    exit()
