from random import random

def printBoard(idx):
    agentPos = [" " for i in range(10)]
    agentPos[0] = "○"
    agentPos[9] = "♕"
    agentPos[idx] = "P"
    print("┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓")
    print("┃ "+agentPos[0]+" ┃ "+agentPos[1]+" ┃ "+agentPos[2]+" ┃ "+agentPos[3]+" ┃ "+agentPos[4]+" ┃ "+agentPos[5]+" ┃ "+agentPos[6]+" ┃ "+agentPos[7]+" ┃ "+agentPos[8]+" ┃ "+agentPos[9]+" ┃")
    print("┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛")

def learn(qTable, currPos):
    # update q value table
    qTable[currPos][0] = qValue(qTable, currPos, -1)
    qTable[currPos][0] = qValue(qTable, currPos, -1)
    print(qTable)

def qValue(qtable, state, action, discount):
    if(state == 8 and action == 1): # nilai pisang
        return 10
    elif(state == 1 and action == -1): # nilai zonk
        return -10
    else:
        return qtable[state, action] + discount*max(qtable[state+action, -1], qtable[state+action, 1])

def bellmanEquation(lr, disc):
    print("awokaowk")

def main(epsilon):
    # initialize current player location
    playerPosIdx = 2

    # 2 x 10 soalnya 10 possible states and 2 possible moves
    # index 0 kiri, indeks 1 kanan
    qTable = [[0,0] for i in range(10)]

    # update table and print out
    learn(qTable, playerPosIdx)
    printBoard(playerPosIdx)

    while(0 < playerPosIdx and playerPosIdx < 9):
        # explore or exploit berd random
        r = random()
        if(r < epsilon): # random
            m = random()
            if(m <= 0.5):
                playerPosIdx -= 1
            else:
                playerPosIdx += 1
        else: # berd. tabel, q value yg paling tinggi
            if(qTable[playerPosIdx][0] > qTable[playerPosIdx][1]):
                playerPosIdx -= 1
            else:
                playerPosIdx += 1
        printBoard(playerPosIdx)
    
    if(playerPosIdx == 9):
        print("Menang!")
    else:
        print("Wait, this got printed?")

# main()
printBoard(3)