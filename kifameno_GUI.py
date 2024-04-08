import pygame
import pygame_textinput
from sys import exit
import kifameno_popup as popup

pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Chi Fa Meno turnir')
clock = pygame.time.Clock()

start_font = pygame.font.Font('times new roman italic.ttf', 80)
kolo_font = pygame.font.Font('times new roman bold italic.ttf', 120)
natrag_font = pygame.font.Font('ComicSansMS3.ttf', 50)
leaderboard_font = pygame.font.Font('ComicSansMS3.ttf', 15)
upis_font = pygame.font.Font('times new roman.ttf', 30)

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
punti_text = leaderboard_font.render('pobjede', True, 'white')
punti_rect = punti_text.get_rect(center = (900, 40))

#generiraj_kolo_km()
n = 1

#upisi_igru
reset_text = natrag_font.render('reset', True, 'white')
reset_rect = reset_text.get_rect(center = (1500, 200))

rect_list = [begin_rect]


'''def rectlistmagija(mx, my):
    #funkcija prolazi kroz sve "aktivne" hitboxeve i gleda nalazi li se kursor na nekoj od njih
    global rect_list
    for i in rect_list:
        if i.collidepoint(mx, my):
            return rect_list.index(i)
    return -1'''

def whiletrue():
    '''stvari koje bi trebao pisat u svakom mainloopu, al sad ne trebam'''
    global rect_list
#    print(rect_list)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    mx, my = pygame.mouse.get_pos()
#    print(mx, my)
    if pygame.mouse.get_pressed()[0] == True:
        for i in rect_list:
            if i.collidepoint(mx, my):
#                print('bro', mx, my, i)
                return rect_list.index(i)
        return -1
                
def blit_button(rect, text, screen, w):
    '''funkcija crta "gumb" (tekst + pravokutnik sirine {w}) na ekran {screen}'''
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
                    rect_list = [natrag_rect, reset_rect]
                    upisi_igru()
                case 3:
                    rect_list = [natrag_rect]
                    generiraj_kolo_km()
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
        igre = open('igre.txt', 'w')
        for i in lista:
            ljestvica.write(f'{i:30}|{0:3}|{0:3}|\n') #valjda nitko nema ime duze od 30...
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
                rect = text.get_rect(center = (pos, 95+i*30))
                screen.blit(text, rect)
                pygame.draw.line(screen,'White', (0, 80+i*30), (1200, 80+i*30))
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

def ljestvica_sort(l):
    l = sorted(l, key = lambda t: t[1]) #sortiranje po bodovima
#    print('sortirano 1:', l)

    k = 1
    check = True
    while check: #sortiranje po pobjedama, doslovno samo bubble sort
        check = False
        for i in range(len(l)-k):
            if l[i][1] == l[i+1][1] and l[i][2] < l[i+1][2]:
                l[i], l[i+1] = l[i+1], l[i]
                check = False
        k += 1
    return l

def upisi_igru():
    '''mainloop za upisivanje nove igre'''
    global rect_list
    ljestvica = open('ljestvica.txt', 'r')
    print('upisi igru')

    s = ljestvica.read()
    print('vrlo vazan string kojeg trebam: ', s)
    ljestvica.seek(0)
    l = ljestvica.readlines()
    print('readlines prije', l)
    l = [i.split('|') for i in l]
    while ['\n'] in l:
        l.remove(['\n'])
    for i in l:
        i[0] = i[0].strip()
        i[1] = int(i[1])
        i[2] = int(i[2])
        del i[3]
        i = tuple(i)
    print('readlines kasnije', l)
    textinput = pygame_textinput.TextInputVisualizer(font_color = 'White', font_object = upis_font)
    pomak_x = 0
    pomak_y = -50
    blit_list = []
    counter = 0
    screen.fill((106, 106, 106))

    while True:
        screen.fill((106, 106, 106))
        events = pygame.event.get()
        textinput.update(events)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #pritisnut enter
                pomak_y *= -1
                if pomak_y < 0:
                    pomak_x += 400
                blit_list.append(textinput.value)
                textinput.value = ''
                counter += 1

                if counter == 6: #kad su 3 imena i 3 broja upisana...
                    igre = open('igre.txt', 'a')
                    ljestvica = open('ljestvica.txt', 'r+')

                    actual_list = [(blit_list[i], int(blit_list[i+1])) for i in range(0, 6, 2)]
                    actual_list = sorted(actual_list, key = lambda t: t[1], reverse = True)
                    actual_list = [[actual_list[i][0], actual_list[i][1], i] for i in range(0, 3)]
                    print(actual_list)
                    if actual_list[0][1] == actual_list[1][1] and actual_list[1][1] == actual_list[2][1]: #ako svi imaju isti broj bodova, svi dobe 1 bod za pobjedu
                        print('svi isto')
                        for i in range(3):
                            actual_list[i][2] = 1
                    elif actual_list[0][1] == actual_list[1][1]: #ako su zadnja 2 igraca isti po bodovima, dobe 1 pod za pobjedu dok 1. dobiva 2
                        print('druga 2 ista')
                        actual_list[0][2] = 1
                    elif actual_list[1][1] == actual_list[2][1]: #ako su prva 2 igraca isti po bodovima, dobe 1 bod za pobjedu dok 3. dobiva 0
                        print('prva 2 ista')
                        actual_list[2][2] = 1
                    print('actual list:', actual_list)
                    igre_string = ' '.join(blit_list)

                    igre.write(igre_string + '\n') #pisanje u igre.txt

                    for t in l: #azuriranje podataka iz acutal_list u l
                        for t1 in actual_list:
                            if t1[0] == t[0]:
                                t[1] += t1[1]
                                t[2] += t1[2]
                                del t1
                    ljestvica.seek(0)
#                    print(l)
                    l = ljestvica_sort(l)   
                    for t in l: #pisanje u ljestvica.txt
                        ljestvica.write(f'{t[0]:30}|{t[1]:3}|{t[2]:3}|\n')
                 
                    igre.close()
                    ljestvica.close()

                    screen.fill('black')
                    rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
                    main_menu()
        indx = whiletrue()
        match indx:
            case 0:
                screen.fill('black')
                rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
                main_menu()
            case 1:
                screen.fill((106, 106, 106))
                upisi_igru()
                
                    
                    

        for i in range(len(blit_list)): #crtanje vec upisanih stvari na njihova mjesta
            text = upis_font.render(str(blit_list[i]), True, 'white')
            check_y = i % 2
            check_x = int(i/2) #isto sto i floor(i/2)
            screen.blit(text, (400+400*check_x-upis_font.size(blit_list[i])[0]/2, 400+100*check_y))
        screen.blit(textinput.surface, (400+pomak_x-upis_font.size(textinput.value)[0]/2, 450+pomak_y)) #crtanje inputa
        pygame.draw.line(screen,'White', (200, 200), (200, 900)) #linije
        pygame.draw.line(screen,'White', (600, 200), (600, 900))
        pygame.draw.line(screen,'White', (1000, 200), (1000, 900))
        pygame.draw.line(screen,'White', (1400, 200), (1400, 900))
        pygame.draw.line(screen,'White', (0, 300), (1600, 300))
        blit_button(natrag_rect, natrag_text, screen, 1)
        blit_button(reset_rect, reset_text, screen, 1)


        pygame.display.update()
        clock.tick(60)
        
def swiss(l):
    '''funkcija uzima sortiranu listu imena i vraca listu 3-torki po swiss formatu turnira'''
    l1 = []
    step = 3
    i = -1
    error_check = True
    while i+step*2 != len(l)-1: #(1,4,7),(2,5,8),(3,6,9),(10,13,16)...
        try:
            i += 1
            if not i % 3 and i != 0 and error_check:
                i += 6
#            print(i, i+step, i+step*2, l[i], l[i+step], l[i+step*2])
            l1.append((l[i], l[i+step], l[i+step*2]))
            error_check = True
        except IndexError: #ako javi IndexError, znaci da su ili 6 ili 3 igraca ostali, npr ako ima 15 igraca i zadnje je bilo (3,6,9). onda mora ic (10,12,14) i (11,13,15)
            step -= 1
            i -= 1
            error_check = False
    return l1    

def generiraj_kolo_km():
    '''mainloop za generiranje novog kola'''
    global rect_list, n
    ljestvica = open('ljestvica.txt', 'r')
    print('generiraj kolo')

    l = ljestvica.readlines()
    l = [i.split('|') for i in l]
    for i in l:
        i[0] = i[0].strip()
        i[1] = int(i[1])
        i[2] = int(i[2])
        del i[3]

    indx = 0
    l_imena = []
    for i in l:
        l_imena.append(i[0])
    print('imena:', l_imena)
    l_imena = swiss(l_imena)
#    l1 = []
#    while indx+3 <= len(l):
#        l1.append((l[indx][0], l[indx+1][0], l[indx+2][0]))
#        indx += 3
#    print(l)
#    print('novo kolo:')
#    for i in range(len(l1)):
#        print(i, l1[i])

    screen.fill('black')
    kolo_text = kolo_font.render(f'{n}. kolo', True, 'White')
    kolo_rect = kolo_text.get_rect(center = (800, 100))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        indx = whiletrue()
        if indx == 0:
            screen.fill('black')
            rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
            main_menu()

                
        blit_button(natrag_rect, natrag_text, screen, 1)
        screen.blit(kolo_text, kolo_rect)
        for i in range(len(l_imena)):
            for j in range(3):
                text = leaderboard_font.render(str(l_imena[i][j]), True, 'White')
                screen.blit(text, (125+300*(i%5), 250+20*j+150*(i//5)))

        
        pygame.display.update()
        clock.tick(60)

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
