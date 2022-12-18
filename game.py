import random

print("sang kaqaz qeichi")

Player_1 = input("player 01 insert your name: ")
Player_2 = "system"

asl_game = 0

while asl_game >= 0:


    dast = input("insert set (3 , 5 , 9): ")

    print(f"Player_1 is: {Player_1}")
    print(f"Player_2 is: {Player_2}")
    print("-------game start-------")
    print("Game tutorial : s = sang , k = kaqaz , q = qeichi")

    P01 = 0
    P02 = 0
    score = int(dast)

    while P01 < score and P02 < score:

        print(f"{Player_1}= {P01} | {Player_2}= {P02}")

        bazi_1 = input("make your move ==> ")

        if bazi_1 == "s":
            bazi_1 = "sang"
        elif bazi_1 == "k":
            bazi_1 = "kaqaz"
        elif bazi_1 == "q":
            bazi_1 = "qeichi"
        elif bazi_1 == "l":
            break

        bazi_2 = random.randint(0, 2)

        if bazi_2 == 0:
            bazi_2 = "sang"
        elif bazi_2 == 1:
            bazi_2 = "kaqaz"
        elif bazi_2 == 2:
            bazi_2 = "qeichi"

        print("-----***-----")

        print(f"{Player_1} make:  {bazi_1}")
        print(f"{Player_2} make:  {bazi_2}")

        if bazi_1 == bazi_2:
            print("---same move---")
        elif bazi_1 == "sang":
            if bazi_2 == "kaqaz":
                print(f"{Player_2} win...")
                P02 += 1
            elif bazi_2 == "qeichi":
                print(f"{Player_1} win...")
                P01 += 1
        elif bazi_1 == "kaqaz":
            if bazi_2 == "qeichi":
                print(f"{Player_2} win...")
                P02 += 1
            elif bazi_2 == "sang":
                print(f"{Player_1} win...")
                P01 += 1
        elif bazi_1 == "qeichi":
            if bazi_2 == "sang":
                print(f"{Player_2} win...")
                P02 += 1
            elif bazi_2 == "kaqaz":
                print(f"{Player_1} win...")
                P01 += 1
        else:
            print("**wrong: please insert [s , k , q ]**")

    print(f"final scores: {Player_1}= {P01} | {Player_2}= {P02}")

    if P01 > P02:
        print(f"**-{Player_1}-** win the match #$#$#$#$#$#$#$#$#$#$# ")
    else:
        print(f"**-{Player_2}-** win the match #$#$#$#$#$#$#$#$#$#$# ")

    print("---------------------------------------------")
    asl_game += 1
    question001 = input("Do you like continue the match (press any key or 'no')? ")
    if question001 == "no":
        print("game done")
        break
    else:
        continue
