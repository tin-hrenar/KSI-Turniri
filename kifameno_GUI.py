import pygame
import pygame_textinput
from sys import exit
import kifameno_popup as popup

pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Chi Fa Meno turnir')
clock = pygame.time.Clock()
start_font = pygame.font.Font('ComicSansMS3.ttf', 80)
leaderboard_font = pygame.font.Font('ComicSansMS3.ttf', 30)

#main()
begin_text = start_font.render('Begin', True, 'White')
begin_rect = begin_text.get_rect(center = (800, 500))
screen.blit(begin_text, begin_rect)
pygame.draw.rect(screen, 'White', begin_rect, width = 1)

#main_menu()
noviturnir_text = start_font.render('novi turnir', True, 'white')
noviturnir_rect = noviturnir_text.get_rect(center = (800, 200))
ljestvica_text = start_font.render('ljestvica', True, 'white')
ljestvica_rect = ljestvica_text.get_rect(center = (800, 400))
upisi_igru_text = start_font.render('upisi igru', True, 'white')
upisi_igru_rect = upisi_igru_text.get_rect(center = (800, 600))
genkolo_text = start_font.render('generiraj kolo', True, 'white')
genkolo_rect = genkolo_text.get_rect(center = (800, 800))

rect_list = [begin_rect] 


def rectlistmagija(mx, my):
    '''funkcija prolazi kroz sve "aktivne" hitboxeve i gleda nalazi li se kursor na nekoj od njih'''
    global rect_list
    for i in rect_list:
        if i.collidepoint(mx, my):
            return rect_list.index(i)
    return -1

'''def whiletrue():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (True, False, False):
            indx = rectlistmagija()
#            print('indx', indx)
            if indx != -1:
                pass'''
                
def blit_button(rect, text, screen, w):
    t = (rect.x+rect.w, rect.y+rect.h)
    screen.blit(text, rect)
    pygame.draw.rect(screen, 'White', rect, width = w)


def main_menu():
    global rect_list
    #rectovi: noviturnir, ljestvica, upisi igru, genkolo

#    blit_button(noviturnir_rect, noviturnir_text)
#    blit_button(ljestvica_rect, ljestvica_text)
#    blit_button(upisi_igru_rect, upisi_igru_text)
#    blit_button(genkolo_rect, genkolo_text)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (True, False, False):
            indx = rectlistmagija(mx, my)
            if indx != -1:
                match indx: #nova sintaksa: match/case
                    case 0:
                        noviturnir()
                    case 1:
                        print('ljestvica')
                        ljestvica()
                    case 2:
                        print('upisi igru')
                    case 3:
                        print('generiraj kolo')
        blit_button(noviturnir_rect, noviturnir_text, screen, 1)
        blit_button(ljestvica_rect, ljestvica_text, screen, 1)
        blit_button(upisi_igru_rect, upisi_igru_text, screen, 1)
        blit_button(genkolo_rect, genkolo_text, screen, 1)
        pygame.display.update()
        clock.tick(60)
                
def noviturnir():
    '''mainloop za upisivanje novog turnira i brisanje podataka'''
    da = popup.popup()
    
    if da:
        print('da')
        ljestvica = open('ljestvica.txt', 'w')

        lista = popup.popup2()
        print(lista)

        for i in lista:
            ljestvica.write(f'{i+",":30}0,   0   \n')
        ljestvica.close()
        
    elif not da:
        print('ne')

    pygame.quit()
    exit()

def ljestvica():
    '''mainloop za prikazivanje ljestvice'''
    global rect_list
    screen.fill('black')
    ljestvica = open('ljestvica.txt', 'r')
    l = ljestvica.readlines()
    for i in range(len(l)):
        s = l[i].split()
        text = leaderboard_font.render(str(s), True, 'White')
        screen.blit(text, (0, 0+i*31))

def main():
    '''mainloop za biranje izmedu tresete i kifa meno'''
    global rect_list
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            mx, my = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (True, False, False):
                indx = rectlistmagija(mx, my)
    #            print('indx', indx)
                if indx != -1:
                    if rect_list[indx] == begin_rect:
    #                    print('da')
                        screen.fill('black')
                        rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
                        main_menu()

        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
