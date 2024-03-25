import pygame
import pygame_textinput
from sys import exit
import kifameno_popup as popup

pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Chi Fa Meno turnir')
clock = pygame.time.Clock()

start_font = pygame.font.Font('ComicSansMS3.ttf', 80)
natrag_font = pygame.font.Font('ComicSansMS3.ttf', 50)
leaderboard_font = pygame.font.Font('ComicSansMS3.ttf', 20)

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

#ljestvica()
natrag_text = natrag_font.render('natrag', True, 'white')
natrag_rect = natrag_text.get_rect(center = (1500, 100))
imeigraca_text = natrag_font.render('ime igraca', True, 'white')
imeigraca_rect = imeigraca_text.get_rect(center = (525, 40))
bodovi_text = leaderboard_font.render('bodovi', True, 'white')
bodovi_rect = bodovi_text.get_rect(center = (800, 40))
punti_text = leaderboard_font.render('punti', True, 'white')
punti_rect = punti_text.get_rect(center = (900, 40))

rect_list = [begin_rect] 


'''def rectlistmagija(mx, my):
    #funkcija prolazi kroz sve "aktivne" hitboxeve i gleda nalazi li se kursor na nekoj od njih
    global rect_list
    for i in rect_list:
        if i.collidepoint(mx, my):
            return rect_list.index(i)
    return -1'''

def whiletrue():
    '''stvari koje bi trebao pisat u svakom mainloopu, pa ne trebam'''
    global rect_list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == True:
        for i in rect_list:
            if i.collidepoint(mx, my):
                return rect_list.index(i)
        return -1
                
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
        indx = whiletrue()             
        if indx != -1:
            match indx: #nova sintaksa: match/case
                case 0:
                    print('noviturnir')
                    noviturnir()
                case 1:
                    print('ljestvica')
                    rect_list = [natrag_rect]
                    ljestvica()
                case 2:
                    upisi_igru()
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
    #podaci se obrisu samo nakon drugog popupa, radi sigurnosti podataka
    da = popup.popup()
    
    if da:
        print('da')
        

        lista = popup.popup2()
        print(lista)
        ljestvica = open('ljestvica.txt', 'w')
        for i in lista:
            ljestvica.write(f'{i:30}|0  |0  |\n')
        ljestvica.close()
        
#    else:
#        print('ne')

    pygame.quit()
    exit()

def ljestvica():
    '''mainloop za prikazivanje ljestvice'''
    global rect_list
    screen.fill('black')
    ljestvica = open('ljestvica.txt', 'r')
    l = ljestvica.readlines()
    pos_lista = [525, 800, 900]
    

    while True:
        indx = whiletrue()
        if indx == 0:
            screen.fill('black')
            rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
            main_menu()

        blit_button(natrag_rect, natrag_text, screen, 1)
        for i in range(len(l)):
            s = l[i].split('|')
            del s[-1]
            for j in range(len(s)):
                s[j] = s[j].strip()
                
            for pos in pos_lista:
                text = leaderboard_font.render(str(s[pos_lista.index(pos)]), True, 'White')
                rect = text.get_rect(center = (pos, 100+i*40))
                screen.blit(text, rect)
                pygame.draw.line(screen,'White', (0, 120+i*40), (1200, 120+i*40))
        pygame.draw.line(screen,'White', (0, 80), (1200, 80))
        pygame.draw.line(screen,'White', (300, 0), (300, 1200))
        pygame.draw.line(screen,'White', (750, 0), (750, 1200))
        pygame.draw.line(screen,'White', (850, 0), (850, 1200))
        pygame.draw.line(screen,'White', (950, 0), (950, 1200))
        screen.blit(imeigraca_text, imeigraca_rect)
        screen.blit(bodovi_text, bodovi_rect)
        screen.blit(punti_text, punti_rect)

        pygame.display.update()
        clock.tick(60)

def upisi_igru():
    '''mainloop za upisivanje nove igre'''
    print('upisi igru')
    pass

def main():
    '''mainloop za biranje izmedu tresete i kifa meno'''
    global rect_list
    while True:
        indx = whiletrue()
        if indx == 0:
            screen.fill('black')
            rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
            main_menu()

        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
