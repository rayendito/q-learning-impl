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

def learn(qTable, rewards, lr, gamma, currPos, action):
    # learning rate 1, berarti langsung update q value
    if(action == 1):
        idex = 1
    else:
        idex = 0
    try:
        qTable[currPos][idex] = qTable[currPos][idex] + lr*(rewards[currPos+action] + gamma*(max(qTable[currPos+action])) - qTable[currPos][idex])
    except:
        print(idex)
        print(currPos)
        print(action)
    

def main():
    # initializations
    playerPosIdx = 2
    sqWeight = [-15000, -1, 0, 1, 10, 100, 1000, 5000, 10000, 15000]
    qTable = [[0,0] for i in range(10)]
    epsilon  = 0.2
    score = 0
    lr = 0.2
    gamma = 0.8

    #selama blm sampe goal
    print("learning...")
    while(-5 < score and score < 5):
        # print current states to the screen
        print("Current Q table :")
        print(qTable)
        printBoard(playerPosIdx)

        # random to decide expolore apa exploit
        r = random()

        # explore
        if(r < epsilon):
            print("Exploring!")
            # random ke kanan apa ke kiri
            m = random()
            # ke kiri
            if(m <= 0.5):
                action = -1
            # ke kanan
            elif(0.5 < m):
                action = 1
        # exploit
        else:
            print("Exploiting!")
            if(qTable[playerPosIdx][0] <= qTable[playerPosIdx][1]):
                action = 1
            else:
                action = -1
        
        #learn regardless
        learn(qTable, sqWeight, lr, gamma, playerPosIdx, action)
        playerPosIdx += action
        
        # check if at pojokan
        if(playerPosIdx == 0 or playerPosIdx == 9):
            if(playerPosIdx == 0):
                score -= 1
            else:
                score += 1
            playerPosIdx = 2

        # sleep so we can see
        time.sleep(1.5)
    
    if(score == 5):
        print("Menang! :D")
    else:
        print("Kalah.. :(")

main()