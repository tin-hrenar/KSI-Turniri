import pygame
import pygame_textinput
from sys import exit
import treseta_popup as popup

pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Trešeta turnir')
clock = pygame.time.Clock()
pygame.key.set_repeat(200, 25)

start_font = pygame.font.SysFont('Times New Roman', 80)
kolo_font = pygame.font.SysFont('Times New Roman', 120, bold=True, italic=True)
natrag_font = pygame.font.SysFont('Comic Sans MS', 50)
leaderboard_font = pygame.font.SysFont('Comic Sans MS', 15)
credit_font = pygame.font.SysFont('Comic Sans MS', 15)
upis_font = pygame.font.SysFont('Times New Roman', 30)
n_font = pygame.font.SysFont('Times New Roman', 40)

'''ovo sve se mora definirati na pocetku zbog toga kako program radi, jer se koristi u svakoj funkciji'''

#main_menu()
noviturnir_text = start_font.render('Novi turnir', False, 'white')
noviturnir_rect = noviturnir_text.get_rect(center = (800, 200))
ljestvica_text = start_font.render('Ljestvica', False, 'white')
ljestvica_rect = ljestvica_text.get_rect(center = (800, 400))
upisi_igru_text = start_font.render('Upiši igru', False, 'white')
upisi_igru_rect = upisi_igru_text.get_rect(center = (800, 600))
genkolo_text = start_font.render('Generiraj kolo', False, 'white')
genkolo_rect = genkolo_text.get_rect(center = (800, 800))
credit_text = credit_font.render('Program napravio Tin Hrenar', True, 'white')
credit_rect = credit_text.get_rect(topleft = (0, 878))

#ljestvica()
natrag_text = natrag_font.render('Natrag', True, 'white')
natrag_rect = natrag_text.get_rect(center = (1500, 100))
imeigraca_text = natrag_font.render('Ime igrača', True, 'white')
imeigraca_rect = imeigraca_text.get_rect(center = (525, 40))
bodovi_text = leaderboard_font.render('Bodovi', True, 'white')
bodovi_rect = bodovi_text.get_rect(center = (800, 40))
punti_text = leaderboard_font.render('Pobjede', True, 'white')
punti_rect = punti_text.get_rect(center = (900, 40))

#generiraj_kolo_t()
novokolo_text = natrag_font.render('Novo kolo', True, 'white')
novokolo_rect = novokolo_text.get_rect(center = (200, 100))
n = 1 #redni broj kola
nincrease_text = n_font.render('n+', True, 'white')
nincrease_rect = nincrease_text.get_rect(topleft = (90, 150))
ndecrease_text = n_font.render('n- ', True, 'white')
ndecrease_rect = ndecrease_text.get_rect(topleft = (140, 150))
kolo_check = True

#upisi_igru()
reset_text = natrag_font.render('Reset', True, 'white')
reset_rect = reset_text.get_rect(center = (1500, 200))
tim1_text = start_font.render('1. tim', True, 'white')
tim1_rect = tim1_text.get_rect(center = (750, 350))
tim2_text = start_font.render('2. tim', True, 'white')
tim2_rect = tim2_text.get_rect(center = (1150, 350))
imetima_text = natrag_font.render('Ime tima', True, 'white')
imetima_rect = imetima_text.get_rect(center = (400, 450))
Bodovi_text = natrag_font.render('Bodovi', True, 'white') #bodovi_text je u ljestvica()
Bodovi_rect = Bodovi_text.get_rect(center = (400, 560))
rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]

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

    screen.fill((0, 5, 80))
    while True:
        indx = whiletrue()             
        if indx != -1:
            match indx: #nova sintaksa: match/case
                case 0:
#                    print('noviturnir')
                    noviturnir()
                case 1:
#                    print('ljestvica')
                    rect_list = [natrag_rect]
                    ljestvica()
                case 2:
                    rect_list = [natrag_rect, reset_rect]
                    upisi_igru()
                case 3:
                    rect_list = [natrag_rect, novokolo_rect, nincrease_rect, ndecrease_rect]
                    generiraj_kolo_t()
        blit_button(noviturnir_rect, noviturnir_text, screen, 1)
        blit_button(ljestvica_rect, ljestvica_text, screen, 1)
        blit_button(upisi_igru_rect, upisi_igru_text, screen, 1)
        blit_button(genkolo_rect, genkolo_text, screen, 1)
        screen.blit(credit_text, credit_rect)
        pygame.display.update()
        clock.tick(60)
                
def noviturnir():
    global n
    '''mainloop za upisivanje novog turnira i brisanje podataka'''
    #podaci se obrisu samo nakon drugog popupa, radi sigurnosti podataka
    da = popup.popup()
    
    if da:
        print('da')
        

        lista = popup.popup2()
        print(lista)
        ljestvica = open('ljestvica_t.txt', 'w', encoding = 'utf-8')
        igre = open('igre_t.txt', 'w', encoding = 'utf-8')
        kolo = open('kolo_t.txt', 'w', encoding = 'utf-8')
        for i in lista:
            ljestvica.write(f'{i:30}|{0:3}|{0:3}|\n') #valjda nitko nema ime duze od 30...
        ljestvica.close()
        n = 1

        for i in range(0, len(lista)//2):
            print(i, 2*i, 2*i+1)
            kolo.write(f'{lista[2*i]}|{lista[2*i+1]}\n')
        kolo.close()
        
#    else:
#        print('ne')

    pygame.quit()
    exit()

def ljestvica():
    '''mainloop za prikazivanje ljestvice'''
    global rect_list
    screen.fill('black')
    ljestvica = open('ljestvica_t.txt', 'r', encoding = 'utf-8')
    l = ljestvica.readlines()
    pos_lista = [525, 800, 900]
    
    pygame.draw.line(screen,'White', (300, 80+len(l)*30), (950, 80+len(l)*30))
    pygame.draw.line(screen,'White', (300, 80), (950, 80))
    pygame.draw.line(screen,'White', (300, 0), (300, 1200))
    pygame.draw.line(screen,'White', (750, 0), (750, 1200))
    pygame.draw.line(screen,'White', (850, 0), (850, 1200))
    pygame.draw.line(screen,'White', (950, 0), (950, 1200))
    screen.blit(imeigraca_text, imeigraca_rect)
    screen.blit(bodovi_text, bodovi_rect)
    screen.blit(punti_text, punti_rect)
    screen.blit(credit_text, credit_rect)
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
                pygame.draw.line(screen,'White', (300, 80+i*30), (950, 80+i*30))

        pygame.display.update()
        clock.tick(60)

def ljestvica_sort(l): #treseta verzija
    l = sorted(l, key = lambda t: t[2], reverse = True) #sortiranje po pobjedama
#    for i in l:
#        print(i[2])
#    print('sortirano 1:', l, '\n')

    k = 1
    check = True
    while check: #sortiranje po bodovima, doslovno samo bubble sort ali s extra uvjetom
        check = False
        for i in range(len(l)-k):
            if l[i][2] == l[i+1][2] and l[i][1] < l[i+1][1]:
                l[i], l[i+1] = l[i+1], l[i]
                check = True
        k += 1
    return l

def upisi_igru():
    '''mainloop za upisivanje nove igre'''
    global rect_list
    ljestvica = open('ljestvica_t.txt', 'r', encoding = 'utf-8')
#    print('upisi igru')

    s = ljestvica.read()
#    print('vrlo vazan string kojeg trebam: ', s)
    ljestvica.seek(0)
    l = ljestvica.readlines()
#    print('readlines prije', l)
    l = [i.split('|') for i in l]
    while ['\n'] in l:
        l.remove(['\n'])
    for i in l:
        i[0] = i[0].strip()
        i[1] = int(i[1])
        i[2] = int(i[2])
        del i[3]
        i = tuple(i)
#    print('readlines kasnije', l)
    textinput = pygame_textinput.TextInputVisualizer(font_color = 'White', font_object = upis_font) #objekt koji se bavi inputom i crta ga na ekran, no ja moram odredit gdje ce se tekst nacrtat
    pomak_x = 0
    pomak_y = -50
    blit_list = []
    counter = 0
    screen.fill((0, 10, 100))

    change_x = 200 #varijable koje pomicu sve, za testiranje (a mozda i ostanu)
    change_y = 200

    while True:
        screen.fill((0, 10, 100))
        events = pygame.event.get()
        textinput.update(events)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #pritisnut enter
                pomak_y *= -1 # -50 --> 50 i obratno
                if pomak_y < 0:
                    pomak_x += 400
                blit_list.append(textinput.value)
                textinput.value = ''
                counter += 1

                if counter == 4: #kad su 2 imena i 2 broja upisana...
                    igre = open('igre_t.txt', 'a', encoding = 'utf-8')
                    ljestvica = open('ljestvica_t.txt', 'r+', encoding = 'utf-8')

                    actual_list = [[blit_list[i], int(blit_list[i+1]), 0] for i in range(0, 4, 2)]
                    if actual_list[0][1] > actual_list[1][1]: #ako prvi veci od drugog, zamijeni tako da uvijek bude prvi manji a drugi veci
                        actual_list[0], actual_list[1] = actual_list[1], actual_list[0]
                    actual_list[1][2] = 1 #bod za pobjedu!!!! (congrats)
                    gol_razlika = actual_list[1][1] - actual_list[0][1] #razlika izmedu bodova. npr ako su bodovi 41-35, prvi tim treba dobit +6 a drugi -6
                    actual_list[0][1] = -gol_razlika
                    actual_list[1][1] = gol_razlika
#                    print(actual_list)

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
            case 0: #natrag
                screen.fill('black')
                rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
                main_menu()
            case 1: #reset
                screen.fill((106, 106, 106))
                upisi_igru()
                
                    
                    

        for i in range(len(blit_list)): #crtanje vec upisanih stvari na njihova mjesta
            text = upis_font.render(str(blit_list[i]), True, 'white')
            check_y = 50 - 100 * (not i%2)
            check_x = 400 * int(i/2) #isto sto i floor(i/2)
            screen.blit(text, (750+check_x-upis_font.size(blit_list[i])[0]/2, 485+check_y))
        screen.blit(textinput.surface, (750+pomak_x-upis_font.size(textinput.value)[0]/2, 485+pomak_y)) #crtanje inputa (.size() vraca (width, height), zato ima [0])
        pygame.draw.line(screen,'White', (550, 300), (550, 615))
        pygame.draw.line(screen,'White', (950, 300), (950, 615))
        pygame.draw.line(screen,'White', (1350, 300), (1350, 615))

        pygame.draw.line(screen,'White', (250, 300), (1350, 300))
        pygame.draw.line(screen,'White', (250, 400), (1350, 400))
        pygame.draw.line(screen,'White', (250, 515), (1350, 515))
        pygame.draw.line(screen,'White', (250, 615), (1350, 615))
        pygame.draw.line(screen, 'White', (250, 300), (250, 615))
        blit_button(natrag_rect, natrag_text, screen, 1)
        blit_button(reset_rect, reset_text, screen, 1)
        screen.blit(tim1_text, tim1_rect)
        screen.blit(tim2_text, tim2_rect)
        screen.blit(credit_text, credit_rect)
        screen.blit(imetima_text, imetima_rect)
        screen.blit(Bodovi_text, Bodovi_rect)

        

        pygame.display.update()
        clock.tick(60)
        
def swiss(l): #algoritam pretpostavlja da ima paran broj igraca
    l1 = []
    for i in range(0,len(l),2):
        l1.append((l[i], l[i+1]))
    return l1    

def generiraj_kolo_t():
    '''mainloop za generiranje novog kola'''
    global rect_list, n, kolo_check
    ljestvica = open('ljestvica_t.txt', 'r', encoding = 'utf-8')
    kolo = open('kolo_t.txt', 'r', encoding = 'utf-8')
#    print('generiraj kolo')

    l = ljestvica.readlines()
    l = [i.split('|') for i in l]
    for i in l:
        i[0] = i[0].strip()
        i[1] = int(i[1])
        i[2] = int(i[2])
        del i[3]
#    print('l:', l)

    indx = 0
#    l_imena = []
#    for i in l:
#        l_imena.append(i[0])

    l_imena1 = kolo.readlines()
#    print(l_imena1)
    l_imena1 = [i.strip('\n').split('|') for i in l_imena1]
#    print('imena1:', l_imena1)
#    l_imena = swiss(l_imena)
#    print('imena:', l_imena)

    screen.fill('black')
    kolo_text = kolo_font.render(f'{n}. kolo', True, 'White')
    kolo_rect = kolo_text.get_rect(center = (800, 100))
    counter = 0
#    kolo_check = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if counter > 60:
            kolo_check = True
            counter = 0
        indx = whiletrue()
        match indx:
            case 0:
                screen.fill('black')
                rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
                main_menu()
            case 1:
                if kolo_check:
#                    print('novo kolo aktivirano')
                    n += 1
                    kolo_text = kolo_font.render(f'{n}. kolo', True, 'White')
                    kolo_check = False
                    ljestvica.seek(0)
                    l = ljestvica.readlines()
                    l = [i.split('|') for i in l]
                    for i in l:
                        i[0] = i[0].strip()
                        i[1] = int(i[1])
                        i[2] = int(i[2])
                        del i[3]
                    

                    l_i = [i[0] for i in l]
                    l_i = swiss(l_i)
#                    print(l_i)
                    kolo = open('kolo_t.txt', 'w', encoding = 'utf-8')
                    for i in l_i:
                        kolo.write(f'{i[0]}|{i[1]}\n')

                    kolo.close()
                    generiraj_kolo_t()
            case 2:
                if kolo_check:
                    n += 1
                    kolo_text = kolo_font.render(f'{n}. kolo', True, 'White')
                    kolo_check = False
            case 3:
                if kolo_check:
                    n -= 1
                    kolo_text = kolo_font.render(f'{n}. kolo', True, 'White')
                    kolo_check = False


        screen.fill((0, 5, 50))
        blit_button(natrag_rect, natrag_text, screen, 1)
        blit_button(novokolo_rect, novokolo_text, screen, 1)
        blit_button(nincrease_rect, nincrease_text, screen, 1)
        blit_button(ndecrease_rect, ndecrease_text, screen, 1)
        screen.blit(kolo_text, kolo_rect)
        screen.blit(credit_text, credit_rect)
        for i in range(len(l_imena1)):
            for j in range(2):
                text = leaderboard_font.render(str(l_imena1[i][j]), True, 'White')
                screen.blit(text, (125+300*(i%5), 250+20*j+150*(i//5)))

        if not kolo_check:
            counter += 1
#        print(kolo_check, counter)
        pygame.display.update()
        clock.tick(60)

##def main():
##    '''mainloop begin'''
##    global rect_list
##    while True:
##        indx = whiletrue()
##        if indx == 0:
##            screen.fill('black')
##            rect_list = [noviturnir_rect, ljestvica_rect, upisi_igru_rect, genkolo_rect]
##            main_menu()
##
##        
##        pygame.display.update()
##        clock.tick(60)

if __name__ == '__main__':
    main_menu()
