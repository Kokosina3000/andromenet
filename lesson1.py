from random import randint,choice
inv=[]
def play_cat():
    print('robot play cat')
def cook(food):
    print(f'robot cooked{food}')
    return food
def eat(food):
    print(f'robot ate {food}')
def give_food(money):
    choice = input('1-cheaps(45),2-cola(67),3-dushes(108)')
    packet = ''
    change=money
    if choice=='1' and money >= 45:
        packet = 'cheaps'
        change=money-45
    elif choice == '2' and money >= 67:
        packet = 'cola'
        change=money-67
    elif choice == '3' and money >= 108:
        packet = 'dushes'
        change=money-108
    return packet,change
def robot_scan():
    things_to_find=['almac','stone','iron','derevo','palka']
    thing=choice(things_to_find)
    if randint(1,2) == 1:
        return thing
    else:
        return'zaskamili mamonta'
def keep_in_inv(thing):
    if thing == 'zaskamili mamonta':
        print(thing)
    else:
        inv.append(thing)
        print(f'Vot wam podgonchik, + {thing}')
def kill_dragon():
    print('you tp to end')
    answer = input('1-cdoxnut,2-nachat fight')
    if answer =='1':
        inv.clear()
        print('you die')
        exit()
    chance = 0
    if 'derevo'  and 'sword' in inv:
        chance = randint(1,100) in range (1,76)
        print('75')
    elif 'derevo' in inv:
        chance = randint(1,100) in range (1,51)
        print('50')
    answer = input('PLS ENTER')
    if chance:
        print('you win,pls give box')
        inv.append('яйцо')
    else:
        print('you die')
        exit()
def craft():
    recept0 = ['almac','almac','derevo']
    recept1=['iron','iron','iron','palka']
    recept2 = ['almac','almac','palka']
    names=['sword','kirka','motiga']
    all_recepts = [recept0,recept1,recept2]
    l = len(names)
    for i in range(l):
        print(f'{i+1}.{names[i]}-{all_recepts[i]}')
    choices = int(input('number: '))-1
    if not (0 <= choices < l):
        print('idi otcuda poka ne podno')
        return None
    choicen_name = names[choices]
    choicen_ings = all_recepts[choices]
    print(f'wash wibor{choicen_name}')
    print(f'wam nado {choicen_ings}')
    weight = len(inv)
    nes = len(choicen_ings)
    for ing in choicen_ings:
        print(ing)
        if ing in inv:
            inv.remove(ing)
    if weight - nes == len(inv):
        print(F'INVENTORY{choicen_name}')
        inv.append(choicen_name)
    else:
        print('XAXAXAXAXAXA YA TEBAY ZASKAMIL')
def delete():
    item = input('ckin resi')
    if item in inv:
        inv.remove(item)
        print(f'ydaleno {item}')
# buy,change = give_food(100)
# if buy == '': 
#     print('you dont buy')
# else:
#     print(f'you buy {buy}')
#play_cat()
#cook(food='eat')
#plat=cook('poop')
#eat(plat)
#plat2=input('what cook a robot')
#eat(plat2)
while True:
    print('''
          robot:
          1-play with cat
          2-cook
          3-sell food
          d-kill dragon
          e-search mamants
          z-show inventory
          x-delete mamonts
          c-craft
          ```
          0-stop
          ''')
    key=input('choice: ')
    if key == '1':
        print('play with cat')
    elif key == '2':
        food=input('eat: ')
        cook(food)
    elif key == '3':
        money= int(input('money goni'))
        buy,change = give_food(money)
        if buy == '':
            print('you dont buy')
        else:
            print(f'you buy {buy}')
    elif key =='0':
        break
    elif key =='e':
        item=robot_scan()
        keep_in_inv(item)
    elif key =='z':
        print(inv)
    elif key == 'c':
        craft()   
    elif key== 'd':
        kill_dragon()
    elif key == 'x':
        delete()
    else:
        print('no')
    input('press entrer to continue')
    