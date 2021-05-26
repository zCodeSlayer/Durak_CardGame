import pygame
import random
from M_spClasses import TCard, TCcherv, TCbubi, TCkresti, TCpiki


pygame.init()
Green = (0,240, 20)
fon = pygame.image.load('kasino.jpg')
fon = fon.subsurface(100, 40, 600, 400)

window = pygame.display.set_mode((600, 400))

window.fill(Green)
window.blit(fon, (0, 0))
pygame.display.set_caption("Карточная игра 'Дурак'")

pic = pygame.image.load('card.jpeg')
pic = pic.subsurface(18, 2, 64, 97)
pic.set_colorkey((255,255,255))

window.blit(pic, (500, 150))

pygame.display.update()


rand = random.randint(1, 4)
if rand == 1:
    TCbubi.powerup()
    print("Козырь: БУБИ")
elif rand == 2:
    TCcherv.powerup()
    print("Козырь: ЧЕРВИ")
elif rand == 3:
    TCkresti.powerup()
    print('Козырь: КРЕСТИ')
else:
    TCpiki.powerup()
    print("Козырь: ПИКИ") 

#Колода карт
CardList = []
CardList.append(TCcherv(14,0,0, 'CardList.jpg', 0, 0, 56.6153846154, 79.25))
CardList.append(TCbubi(14,78,0, 'CardList.jpg', 0, 79.25*2, 56.6153846154, 79.25))
CardList.append(TCkresti(14,156,0, 'CardList.jpg', 0, 79.25*3, 56.6153846154, 79.25))
CardList.append(TCpiki(14,234,0, 'CardList.jpg', 0, 79.25, 56.6153846154, 79.25))

for j in range(6, 14):
    CardList.append(TCcherv(j,0,0, 'CardList.jpg', 56.6153846154*(j-1), 0, 56.6153846154, 79.25))
    CardList.append(TCbubi(j,0,0, 'CardList.jpg', 56.6153846154*(j-1), 79.25*2, 56.6153846154, 79.25))
    CardList.append(TCkresti(j,0,0, 'CardList.jpg', 56.6153846154*(j-1), 79.25*3, 56.6153846154, 79.25))
    CardList.append(TCpiki(j,0,0, 'CardList.jpg', 56.6153846154*(j-1), 79.25, 56.6153846154, 79.25))
random.shuffle(CardList) #тусуем карты      
#Колода карт

myTurn = 0
table =[]
myhand = []
opponent_hand = []
listOtvet = []

for i in range(6):
    myhand.append(CardList[len(CardList)-1])
    del CardList[len(CardList)-1]
    opponent_hand.append(CardList[len(CardList)-1])
    del CardList[len(CardList)-1]

for i in opponent_hand:
    if i.__class__.power == True:
        first = i   
        myTurn = False
        for j in myhand:
            if (j.__class__.power == True) and (j.status < i.status): 
                myTurn = True

if (myTurn == False):
    min = opponent_hand[0]
    power_count = 0
    for i in opponent_hand:
        if i.status < min.status and i.__class__.power == False: 
            min = i
        else:
            power_count += 1
    if power_count == 6:
        for i in opponent_hand:  
            if i.status < min.status:
                min = i
    myTurn = True
    del power_count
    opponent_hand.remove(min)
    
    table.append(min)  
    del min


count = 0 
def paint_hand(index):  
    z= 300 - ((20*(len(myhand)+1))/2)  
    z1 = 300 - ((20*(len(myhand)+1))/2)
    if len(myhand) > 0:
        for i in myhand:
            i.x = z
            i.y = 320
            z += 20
            i.render(window)
    if len(opponent_hand) > 0:    
            for i in opponent_hand:
                i.x = z1
                i.y = 0
                z1 += 20
                window.blit(pic, (i.x, i.y))
 
index = 0
position = ((300 - 28.3076923077, 200 - 39.625), #0
            (250 - 28.3076923077,200 - 39.625), (350 - 28.3076923077,200 - 39.625), #1,2 
            (150 - 28.3076923077,200 - 39.625), (250 - 28.3076923077,200 - 39.625), (350 - 28.3076923077,200 - 39.625), #3,4,5
            (150 - 28.3076923077,120 - 39.625), (250 - 28.3076923077,120 - 39.625), (350 - 28.3076923077,120 - 39.625), #\|/
            (150 - 28.3076923077,240 - 39.625), (250 - 28.3076923077,240 - 39.625), (350 - 28.3076923077,240 - 39.625))#6, 7, 8, 9, 10, 11  
# for i in range(11):
#    table.append(CardList[len(CardList)-1])
#    CardList.remove(table[len(table)-1])
# print("table len:", len(table))
def CardOnTable(*pos):
    index = 0
    for i in table:
        if (table.index(i)+1)%2 != 0: window.blit(i.picture, pos[index])
        else: 
            window.blit(i.picture, (pos[index][0]+10, pos[index][1]+10))
            index +=1
    
def Razdacha(ochered1, ochered2):
    for i in CardList:
        if (len(CardList) > 0) and (len(ochered1) < 6):
            ochered1.append(i)
            CardList.remove(i)
        if (len(CardList) > 0) and (len(ochered2) < 6):
            if i in CardList:
                ochered2.append(i)
                CardList.remove(i)
            else: 
                continue

def bita(o1, o2):
    table.clear()
    listOtvet.clear()
    Razdacha(o1, o2)

def TableON():
    if len(table) > 0:
        if len(table) <= 2:
            if len(table) == 2:
                window.blit(table[0].picture, position[0])
                window.blit(table[1].picture, (position[0][0] + 10, position[0][1] + 10))
            else:
                window.blit(table[0].picture, position[0])
        elif len(table) <= 4:
            CardOnTable(position[1], position[2])
        elif len(table) <= 6: 
            CardOnTable(position[3], position[4], position[5])
        elif len(table) <= 8: 
            CardOnTable(position[6], position[7], position[8], position[9])
        elif len(table) <= 10: 
            CardOnTable(position[6], position[7], position[8], position[9], position[10])
        elif len(table) <= 12: 
            CardOnTable(position[6], position[7], position[8], position[9], position[10], position[11])

WORK = True
while WORK:
    pygame.time.delay(100)

    if len(CardList) != 0:
        window.blit(pic, (500, 150))

    if count != 1:
        paint_hand(index)
        count = 1

    keys = pygame.key.get_pressed()
    if index < 0:
        index = 0
    elif index > len(myhand)-1:
        index = len(myhand)-1
    if keys[pygame.K_LEFT] and (index > -1):
        window.fill(Green)
        window.blit(fon, (0, 0))
        if len(CardList) != 0:
            window.blit(pic, (500, 150))
        count = 0
        paint_hand(index)
        count = 1
        if len(myhand) > 0: myhand[index].y = 320
        if index != 0: index -= 1
        myhand[index].y -= 40
    if keys[pygame.K_RIGHT] and (index != len(myhand)-1):
        window.fill(Green)
        window.blit(fon, (0, 0))
        if len(CardList) != 0:
            window.blit(pic, (500, 150))
        count = 0
        paint_hand(index)
        count = 1
        if len(myhand) > 0: myhand[index].y = 320
        index += 1
        myhand[index].y -= 40
    if (index > (len(myhand)-1)):
        index = len(myhand)-1

    if (keys[pygame.K_LCTRL]) and (myTurn == True) and (len(table) != 0) and (len(table)%2 == 0):
        bita(myhand, opponent_hand)
        myTurn = False

    if (keys[pygame.K_LSHIFT]) and (myTurn == True) and (len(table)%2 != 0):
        myhand += table
        table.clear()
        Razdacha(opponent_hand, myhand)
        myTurn = False
    
    if index > (len(myhand)-1):
        index = (len(myhand)-1)
    if (keys[pygame.K_TAB]):
        #Мой ход
        if myTurn == True:
            if len(table) == 0:
                table.append(myhand[index])
                myhand.remove(myhand[index])
                myTurn = False
            elif (table[len(table)-1].__class__.power == True) and (myhand[index].status > table[len(table)-1].status) and (myhand[index].__class__.power == True) and (len(table)%2 != 0):
                table.append(myhand[index])
                myhand.remove(myhand[index])
                myTurn = False
            elif (table[len(table)-1].__class__.power == False) and (((table[len(table)-1].name == myhand[index].name) and (myhand[index].status > table[len(table)-1].status)) 
            or myhand[index].__class__.power == True) and (len(table)%2 != 0):
                table.append(myhand[index])
                myhand.remove(myhand[index])
                myTurn = False
            elif (len(table) != 0) and (len(table)%2 == 0):
                for i in table:
                    if myhand[index].status == i.status:
                        table.append(myhand[index])
                        myhand.remove(myhand[index])
                    myTurn = not myTurn
    
    if myTurn == False:
        if len(table) == 0:
            min = opponent_hand[0]
            for i in opponent_hand:
                if (i.__class__.power == False):
                    min = i
            if (min.__class__.power == True):
                for i in opponent_hand:
                    if (i.__class__.power == True) and (i.status < min.status):
                        min = i
            else:
                for i in opponent_hand:
                    if (i.__class__.power == False) and (i.status < min.status):
                        min = i
            table.append(min)
            opponent_hand.remove(min)
            del min 
        elif (len(table) % 2 != 0) and (table[len(table)-1].__class__.power == True):
            polotenchik = 1
            for i in opponent_hand:
                if (i.status > table[len(table)-1].status) and (i.__class__.power == True):
                    table.append(i)
                    opponent_hand.remove(i)
                    polotenchik = 0
                    break
            if polotenchik == 1:
                opponent_hand += table
                Razdacha(myhand, opponent_hand)    
                table.clear()

        elif (len(table) % 2 != 0): # and (len(table) != 0): #ответ на карту (отбивается) 
            for i in opponent_hand:
                if ((table[len(table)-1].name == i.name) and (i.status > table[len(table)-1].status)) or (i.__class__.power == True):
                    # в listOtvet может войти карта той же масти или козырная!
                    listOtvet.append(i)
            if (len(listOtvet) > 0):
                min = listOtvet[0] ### min существует только в этой ветви кода
                if (min.__class__.power == True):
                    for i in listOtvet:
                        if (i.status < min.status): 
                            min = i
                            if (i.__class__.power == False):
                                min = i
                                break
                    if (min.__class__.power == False):
                        for i in listOtvet:
                            if (i.status < min.status):
                                min = i
                else:
                    for i in listOtvet:
                        if (i.status < min.status):
                            min = i    
                table.append(min)
                for i in opponent_hand:
                    if i == min: opponent_hand.remove(i)
                del min
                listOtvet.clear()      
            else:
                opponent_hand += table
                Razdacha(opponent_hand, myhand)
                table.clear()
            listOtvet.clear()
        elif (len(table) % 2 == 0): # ходит на нас
            podkid = 'zero'
            for i in opponent_hand:
                for j in table:
                    if (i.status == j.status) and (i.__class__.power == False):
                        podkid = i
                        break
                if podkid != 'zero': 
                    break
            if podkid != 'zero':
                table.append(podkid)
                opponent_hand.remove(podkid) 
            else:
                bita(opponent_hand, myhand)
                myTurn = True   
            del podkid
        count = 0
        paint_hand(index)
        count = 1
        TableON()  
        pygame.time.delay(1000)      
        myTurn = True        



    TableON()
    if (index == len(myhand)): 
        index -= 1   
    if (len(myhand) > 0):
        myhand[index].render(window)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WORK = False
    
    if (len(CardList) == 0) and (len(myhand) == 0) and (len(opponent_hand) == 0):
        print('Ничья!')
        WORK = False            
    elif (len(myhand) == 0) and (len(CardList) == 0):
        print('Вы выиграли!')
        WORK = False
    elif (len(opponent_hand) == 0) and (len(CardList) == 0):
        print('Вы проиграли!')
        WORK = False
pygame.quit()