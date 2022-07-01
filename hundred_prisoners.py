import random
from tqdm import tqdm

def each_game(number_of_prisoners,random_flag):
    # assigning prisoners random numbers
    temp_list = [i for i in range(number_of_prisoners)]
    prisoners = []
    for i in range(number_of_prisoners):
        temp = random.choice(temp_list)
        prisoners.append(temp)
        temp_list.remove(temp)
    
    # assigning boxes random numbers
    temp_list = [i for i in range(number_of_prisoners)]
    boxes = []
    for i in range(number_of_prisoners):
        temp = random.choice(temp_list)
        boxes.append(temp)
        temp_list.remove(temp)

    if random_flag:
        # random run
        for prisoner in prisoners:
            temp_list = [i for i in range(number_of_prisoners)]
            found = False
            for i in range(number_of_prisoners//2):
                choice = random.choice(temp_list)
                if prisoner == boxes[choice]:
                    found = True
                    break
                temp_list.remove(choice)
            if not found:
                return False
        # not that rare for small number of prisoners say 10... but almost never wins for bigger number even say 20
        print('\n\n\n<<<<<<<<<< Made history!!! won from random picking >>>>>>>>>>\n\n\n')
        return True
    else:
        # startegy run
        for prisoner in prisoners:
            found = False
            choice = prisoner
            for i in range(number_of_prisoners//2):
                if prisoner == boxes[choice]:
                    found = True
                    break
                choice = boxes[choice]
            if not found:
                return False
        return True

# changeable parameters
number_of_prisoners = 100
number_of_random_pick_games = 10000
number_of_strategic_pick_games = 10000

# dont change below parameters
games_won_from_random_pick = 0
games_won_from_strategic_pick = 0
# playing random pick games
for i in tqdm(range(number_of_random_pick_games),desc='Playing Random Pick Games'):
    if each_game(number_of_prisoners,True):
        games_won_from_random_pick += 1
# playing strategic pick games
for i in tqdm(range(number_of_strategic_pick_games),desc='Playing Strategic Pick Games'):
    if each_game(number_of_prisoners,False):
        games_won_from_strategic_pick+=1

print('Number of prisoners =',number_of_prisoners)
print('Number of random pick games=',number_of_random_pick_games)
print('Number of strategic pick games=',number_of_strategic_pick_games)
print('Number of random pick wins =',games_won_from_random_pick,' ',(games_won_from_random_pick/number_of_random_pick_games)*100,'%')
print('Number of strategic pick wins =',games_won_from_strategic_pick,' ',(games_won_from_strategic_pick/number_of_strategic_pick_games)*100,'%')