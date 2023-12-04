# # DAY 2 PART ONE
# checkset = {'red':12, 'green':13, 'blue': 14}
# data = open('input2.txt', 'r')
# totalnumber = 0
# while True:
#     content=data.readline()
#     if not content:
#         break
#     gameinfo = content.split(':')
#     game = gameinfo[0]
#     game = game.split(' ')
#     gamenum = int(game[1])
#     possible = True

#     draws = gameinfo[1].split(';')
#     for x in range(len(draws)):
#         picks = draws[x].split(',')
#         for y in range(len(picks)):
#             single_picks = picks[y].split()
#             print('single picks: ', single_picks)
#             for key in checkset.keys():
#                 if key in single_picks[1]:
#                     if checkset[key] < int(single_picks[0]):
#                         possible = False
#         print('picks: ', picks)
#     if possible:
#         print("This game number ", gamenum, " is possible")
#         totalnumber = totalnumber + gamenum
#     else:
#         print("This game number ", gamenum, " is not possible")
#     print(game)
#     print(gamenum)
#     print(draws)

# data.close()

# print("The total number is: ", totalnumber)

# DAY 2 PART TWO
data = open('input2.txt', 'r')
totalnumber = 0
while True:
    content=data.readline()
    if not content:
        break
    gameinfo = content.split(':')
    game = gameinfo[0]
    game = game.split(' ')
    gamenum = int(game[1])
    checkset = {'red':0, 'green':0, 'blue': 0}
    draws = gameinfo[1].split(';')
    for x in range(len(draws)):
        picks = draws[x].split(',')
        for y in range(len(picks)):
            single_picks = picks[y].split()
            print('single picks: ', single_picks)
            for key in checkset.keys():
                if key in single_picks[1]:
                    if checkset[key] < int(single_picks[0]):
                        checkset[key] = int(single_picks[0])
        print('picks: ', picks)

    print(game)
    print(gamenum)
    print(draws)
    print("Minimum Reds Needed: ", checkset['red'])
    print("Minimum Greens Needed: ", checkset['green'])
    print("Minimum Blues Needed: ", checkset['blue'])
    gamepower = checkset['red']*checkset['green']*checkset['blue']
    print("Power of this game is: ", gamepower)
    totalnumber = totalnumber + gamepower

data.close()

print("The total number is: ", totalnumber)
