"""เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""

def cal(money, w_bottle,snack1):
    """Input"""
    result = money-w_bottle
    result1 = result%3
    if result1 == 0:
        snack = 10
    elif result1 == 1:
        snack = 15
    elif result1 == 2:
        snack = 20
    moneyleft = result - (snack*snack1)
    return moneyleft

def cal2(moneyleft, snack2):
    """Input"""
    result = moneyleft % 3
    if result == 0:
        nsnack = 12
    elif result == 1:
        nsnack = 15
    elif result == 2:
        nsnack = 18
    moneyleft = result - (nsnack*snack2)
    return moneyleft

def cal3(moneyleft, snack3):
    """Input"""
    result = moneyleft % 3
    if result == 0:
        msnack = 5
    elif result == 1:
        msnack = 7
    elif result == 2:
        msnack = 9
    moneyleft = result - (msnack*snack3)
    return moneyleft

def main():
    money = int(input())
    w_bottle = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    moneyleft = cal(money, w_bottle,snack1)
    x = cal2(moneyleft, snack2)
    y = cal3(x, snack3)
    if y < 0:
        print("Now you have 50 left.")
        print("You don't have enough money!")

main()









def xxx():
    money = int(input())
    w_bottle = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    calwater = (money-w_bottle) % 3 
    mleft = (money-w_bottle) // 3
    if calwater == 0:
        csnack1 = 10
        if mleft - (snack1*csnack1) > 0:
            mleft1 = (mleft-(snack1*csnack1))
            calwater = (mleft1) % 3
            mleft = (mleft1) // 3
            if mleft - (snack1*csnack1) > 0:
                mleft1 = (mleft-(snack1*csnack1))
                calwater = (mleft1) % 3
                mleft = (mleft1) // 3 
