
import random

points = [1000]*5

def one():
    return random.random()

def uniform(centre,range):
    return centre + (one()-0.5)*range

def flip():
    return one() < 0.5
# False is heads and True is Tails
def bot1(prev):
    return (round(uniform(60,12),2),one() < 0.5)

def bot2(prev):
    return (round(uniform(50,5),2),not prev)

def bot3(prev):
    return (round(uniform(50,5)),one() < 0.5)

def bot4(prev):
    return (50,False)

bots = [bot1,bot2,bot3,bot4]

def print_scores(points):
    for i in range(5):
        print("Player " + str(i+1),":",points[i])

def coin_choice():
    global y
    while(y not in ["Heads","Tails"]):
        y = input("Enter Heads or Tails : ")
    if(y == "Tails"):
        return True
    return False

def one_round(inputs,points,coin):
    h,t = 0,0
    H,T = [],[]
    c = 0
    for i in inputs:
        if(i[1]):
            t += i[0]
            T.append(c)
        else:
            h += i[0]
            H.append(c)
        c += 1
    points_new = []
    c = 0
    for i in inputs:
        if(coin == True):
            if(i[1] == coin):
                points_new.append(points[c] + round(i[0]*h/t,2))
            else:
                points_new.append(points[c] -i[0])
        else:
            if(i[1] == coin):
                points_new.append(points[c] + round(i[0]*t/h,2))
            else:
                points_new.append(points[c] -i[0])
        c+= 1
    return points_new

def coin_val(f):
    if(f):
        return "Tails"
    else:
        return "Heads"

def print_inputs(inputs,points):
    print("Player Name ,  Points ,   Bid   , Face")
    for i in range(5):
        print("Player " + str(i+1),"   :",round(points[i]+0.00001,1),"    ",round(inputs[i][0]+0.0001,1),"   ",coin_val(inputs[i][1]))
    


coin = True
print('Enter "Heads" or "Tails",(case sensitive) for the flip choice') 
print_scores(points)
y = 0
while(True):
    x = input("Enter bid amount :")
    try:
        x = int(x)
        if(x > points[0]):
            print("error")
            break
    except:
        print("Error")
        break
    y = coin_choice()
    prev = coin
    coin = flip()
    if(coin):
        print("Coin landed on Tails")
    else:
        print("Coin landed on Heads")
    
    inputs = [(round(x,2),y)]
    for i in bots:
        inputs.append(i(prev))
    #print(inputs)
    points = one_round(inputs,points,coin)
    print_inputs(inputs,points)
    print()

