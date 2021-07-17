from random import random
import time

def printBoard(idx):
    agentPos = [" " for i in range(10)]
    agentPos[0] = "○"
    agentPos[9] = "♕"
    agentPos[idx] = "P"
    print("┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓")
    print("┃ "+agentPos[0]+" ┃ "+agentPos[1]+" ┃ "+agentPos[2]+" ┃ "+agentPos[3]+" ┃ "+agentPos[4]+" ┃ "+agentPos[5]+" ┃ "+agentPos[6]+" ┃ "+agentPos[7]+" ┃ "+agentPos[8]+" ┃ "+agentPos[9]+" ┃")
    print("┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛")

def learn(qTable, sqWeight, currPos, action):
    # learning rate 1, berarti langsung update q value
    # ugly code ik :()
    if(action == 1):
        idex = 1
    else:
        idex = 0
    try:
        qTable[currPos][idex] = sqWeight[currPos] + max(qTable[currPos+action][0], qTable[currPos+action][1])
    except:
        print(idex)
        print(currPos)
        print(action)
    

def main(learnSteps):
    # initialize current player location, original learnSteps value
    orLearn = learnSteps
    playerPosIdx = 2

    # square weight
    # mendekat hole dari posisi awal -1, mendekat banana 1
    sqWeight = [-10, -1, 0, 1, 2, 3, 4, 5, 6, 10]

    # 2 x 10 soalnya 10 possible states and 2 possible moves
    # index 0 kiri, indeks 1 kanan
    qTable = [[0,0] for i in range(10)]

    # initialize epsilon to 1 awalnya, lama lama ngurang
    epsilon = 1

    #selama blm sampe goal
    print("learning...")
    while(0 < learnSteps):
        # random dan inisialisasi epsilon
        epsilon = 0.5
        action = 0
        r = random()

        # explore
        if(r < epsilon):
            m = random()
            if(m <= 0.5):
                if(playerPosIdx == 0):
                    action = 1
                else:
                    action = -1
            elif(0.5 < m):
                if(playerPosIdx == 9):
                    action = -1
                else:
                    action = 1
        # exploit
        else:
            if(qTable[playerPosIdx][0] > qTable[playerPosIdx][1]):
                action = -1
            else:
                action = 1
        
        # move and learn by ngupdate qtable nya
        learn(qTable, sqWeight,  playerPosIdx, action)
        playerPosIdx += action
        
        # printing hihi
        # print(qTable)
        # printBoard(playerPosIdx)
        # time.sleep(1)

        # updating values
        epsilon -= 0.05
        learnSteps -= 1
    
    print(qTable)
    print("I've learnt enough time to explore")
    # if(playerPosIdx == 9):
    #     print("Menang!")
    # else:
    #     print("Wait, this got printed?")

main(20)