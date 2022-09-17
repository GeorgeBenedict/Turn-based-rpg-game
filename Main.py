import Hero
import StartGame
import datetime
import random

def printtitle(text):
    print()
    print("-" * 35)
    print(text)
    print("-" * 35)

def printsub(text):
    print()
    print("-" * 25)
    print(text)
    print("-" * 25)
    
def main():
    printtitle("GAME TITLE")
    print("(P)lay\n(C)ontinue\n(R)eplay\n(N)ew Player\n")
    ASK = ""
    while ASK == "" or ASK.lower() != "p" and ASK.lower() != "c" and ASK.lower() != "r" and ASK.lower() != "e" and ASK.lower() != "n" or ASK.isspace():
        ASK = input("Selection: ")
    if ASK.upper() == "R":
        REPLAY()
    if ASK.upper() == "C":
        CONTINUE()
    if ASK.upper() == "P":
        print()
        print("(S)ingle player\n(M)ulti player")
        GameStyle = ""
        while GameStyle == "" or GameStyle.lower() != "s" and GameStyle.lower() != "m" or GameStyle.isspace():
            GameStyle = input("Selection: ")
        if GameStyle.lower() == "s":
            SinglePlayer()
        if GameStyle.lower() == "m":
            MultiPlayer()
    if ASK.upper() == "N":
        register_new()
    if ASK.lower() == "e":
        exit()
###########################################################################################################################################################################################
########################################################### MULTI PLAYER ##################################################################################################################
def MultiPlayer():
    global gameID
    gameID = Game_ID()
    Player1_UN()
def Player1_UN():
    UN1 = input ("Please enter you username\npress enter to return to main menu\n:")
    if not UN1.isspace():
        File = open("Game.txt", "r")
        Line = File.readline()
        while Line != "" and not Line.isspace():
            Scan_line = Line.replace('UN: ', '')
            if Scan_line.lower().strip() == UN1.lower().strip():
                File.close()
                print("Welcome,", UN1)
                UN1 = Scan_line.strip() + '.txt'
                player_1_choose(UN1)
            else:
                Line = File.readline()
                continue
        else:
            File.close()
            print("Your username is not registered!\n\n1. try again\n2. Register new\nPress enter to return to main menu")
            check = input(": ")
            while check != "" and check.lower() != "1" and check.lower() != "2" and check.isspace():
                check = input("Please input either 1/2\n press enter to return to main menu\n: ")
            if check == "" or check.isspace():
                main()
            if check == "1":
                Player1_UN()
            if check == "2":
                register_new()
    
    else:
        print("Returning to main menu")
        main()
def player_1_choose(x):
    player_1 = []
    global Player1_1, Player1_2, Player1_3
    for number in range (3):
        p1 = x.replace(".txt", "").strip() + "Select your heroes"
        printsub(p1)
        print("1.Warrior\t2.Tanker\t3.Wizard\t4.Main Menu")
        print()
        Input = input("P1: ")
        if Input != '1' and Input != '2' and Input != '3' or Input == "" or Input.isspace():
            print("Invalid input, returning to main menu")
            main()
        else:
            if Input == "1":
                player_1.append("Warrior")
            if Input == "2":
                player_1.append("Tanker")
            if Input == "3":
                player_1.append("Wizard")
    for z in range(3):
        print()
        name = input("Please enter your hero name: ")
        while name == "" or name.isspace():
            name = input("INVALID NAME! Please enter a valid hero name (cannot be blank): ")
        if player_1[z] == "Warrior":
            if z == 0:
                Player1_1 = Hero.Hero(Hero.Warrior)
                player_1[z] = name
                player_1[z] += "(Warrior)"
            if z == 1:
                Player1_2 = Hero.Hero(Hero.Warrior)
                player_1[z] = name
                player_1[z] += "(Warrior)"
            if z == 2:
                Player1_3 = Hero.Hero(Hero.Warrior)
                player_1[z] = name
                player_1[z] += "(Warrior)"
        if player_1[z] == "Tanker":
            if z == 0:
                Player1_1 = Hero.Hero(Hero.Tanker)
                player_1[z] = name
                player_1[z] += "(Tanker)"
            if z == 1:
                Player1_2 = Hero.Hero(Hero.Tanker)
                player_1[z] = name
                player_1[z] += "(Tanker)"
            if z == 2:
                Player1_3 = Hero.Hero(Hero.Tanker)
                player_1[z] = name
                player_1[z] += "(Tanker)"
        if player_1[z] == "Wizard":
            if z == 0:
                Player1_1 = Hero.Hero(Hero.Wizard)
                player_1[z] = name
                player_1[z] += "(Wizard)"
            if z == 1:
                Player1_2 = Hero.Hero(Hero.Wizard)
                player_1[z] = name
                player_1[z] += "(Wizard)"
            if z == 2:
                Player1_3 = Hero.Hero(Hero.Wizard)
                player_1[z] = name
                player_1[z] += "(Wizard)"
    time = datetime.datetime.now()
    File = open(x, "a")
    File.writelines(str(time))
    File.write(" \t\t ")
    File.write("Player 1")
    File.write("\t\t")
    File.write(player_1[0])
    File.write("\t\t")
    File.write(player_1[1])
    File.write("\t\t")
    File.write(player_1[2])
    File.write("\tGameID(")
    File.write(str(gameID))
    File.write(")\n")
    File.close()
    print("Your Hero: ", player_1)
    Player2_UN(x.replace(".txt", "").strip(), player_1)
def Player2_UN(UnCheck,xyz):
    UN2 = input ("Hi! please enter you username\n:")
    while UN2.lower() == UnCheck.lower():
        UN2 = input("Please enter other username\n:")
    if UN2 != UnCheck:
        File = open("Game.txt", "r")
        Line = File.readline()
        while Line != "" and not Line.isspace():
            Scan_line = Line.replace('UN: ', '')
            if Scan_line.lower().strip() == UN2.lower().strip():
                print("Welcome,", UN2)
                UN2 = Scan_line.strip() + '.txt'
                File.close
                player_2_choose(UN2.strip(), xyz, UnCheck.replace(".txt", "").strip())
            else:
                Line = File.readline()
                continue
        else:
            File.close()
            print("Your username is not registered!\n\n1. try again\n2. Register new\nPress enter to return to main menu")
            check = input(": ")
            while check != "" and check.lower() != "1" and check.lower() != "2" and check.isspace():
                check = input("Please input either 1/2\n press enter to return to main menu\n: ")
            if check == "" or check.isspace():
                main()
            if check.upper() == "1":
                Player2_UN()
            if check.upper() == "2":
                register_new()
def player_2_choose(UN2,player_1,UN1):
    player_2 = []
    global Player2_1, Player2_2, Player2_3
    for number in range (3):
        p2 = UN2.replace(".txt", "").strip() + "Select your heroes"
        printsub(p2)
        print("1.Warrior\t2.Tanker\t3.Wizard\t4.Main Menu")
        print()
        Input = input("P2: ")
        if Input != '1' and Input != '2' and Input != '3' or Input == "" or Input.isspace():
            print("Invalid input, returning to main menu")
            main()
        else:
            if Input == "1":
                player_2.append("Warrior")
            if Input == "2":
                player_2.append("Tanker")
            if Input == "3":
                player_2.append("Wizard")
    for z in range(3):
        print()
        name = input("Please enter your hero name: ")
        while name == "" or name.isspace():
            name = input("INVALID NAME! Please enter a valid hero name (cannot be blank): ")
        if player_2[z] == "Warrior":
            if z == 0:
                Player2_1 = Hero.Hero(Hero.Warrior)
                player_2[z] = name
                player_2[z] += "(Warrior)"
            if z == 1:
                Player2_2 = Hero.Hero(Hero.Warrior)
                player_2[z] = name
                player_2[z] += "(Warrior)"
            if z == 2:
                Player2_3 = Hero.Hero(Hero.Warrior)
                player_2[z] = name
                player_2[z] += "(Warrior)"
        if player_2[z] == "Tanker":
            if z == 0:
                Player2_1 = Hero.Hero(Hero.Tanker)
                player_2[z] = name
                player_2[z] += "(Tanker)"
            if z == 1:
                Player2_2 = Hero.Hero(Hero.Tanker)
                player_2[z] = name
                player_2[z] += "(Tanker)"
            if z == 2:
                Player2_3 = Hero.Hero(Hero.Tanker)
                player_2[z] = name
                player_2[z] += "(Tanker)"
        if player_2[z] == "Wizard":
            if z == 0:
                Player2_1 = Hero.Hero(Hero.Wizard)
                player_2[z] = name
                player_2[z] += "(Wizard)"
            if z == 1:
                Player2_2 = Hero.Hero(Hero.Wizard)
                player_2[z] = name
                player_2[z] += "(Wizard)"
            if z == 2:
                Player2_3 = Hero.Hero(Hero.Wizard)
                player_2[z] = name
                player_2[z] += "(Wizard)"
    time = datetime.datetime.now()
    File = open(UN2, "a")
    File.writelines(str(time))
    File.write(" \t\t ")
    File.write("Player 2")
    File.write("\t\t")
    File.write(player_2[0])
    File.write("\t\t")
    File.write(player_2[1])
    File.write("\t\t")
    File.write(player_2[2])
    File.write("\tGameID(")
    File.write(str(gameID))
    File.write(")\n")
    File.close
    turn = 1
    print("Your Hero: ", player_2)
    StartGame.game(Player1_1, Player1_2, Player1_3, Player2_1, Player2_2, Player2_3, player_1, player_2, gameID, UN1.replace(".txt", "").strip(), UN2.replace(".txt", "").strip(), turn)

#########################################################################################################################################################################################
####################################################    Single PLayer ###################################################################################################################
def SinglePlayer():
    global gameID
    gameID = Game_ID()
    Player1_UN_SINGLE()
def Player1_UN_SINGLE():
    UN1 = input ("Please enter you username\npress enter to return to main menu\n:")
    if not UN1.isspace():
        print()
        File = open("Game.txt", "r")
        Line = File.readline()
        while Line != "" and not Line.isspace():
            Scan_line = Line.replace('UN: ', '')
            if Scan_line.lower().strip() == UN1.lower().strip():
                File.close()
                print("Welcome,", UN1)
                UN1 = Scan_line.strip() + '.txt'
                player_1_choose_SINGLE(UN1)
            else:
                Line = File.readline()
                continue
        else:
            File.close()
            print("Your username is not registered!\n\n1. try again\n2. Register new\nPress enter to return to main menu")
            check = input(": ")
            while check != "" and check.lower() != "1" and check.lower() != "2" and check.isspace():
                check = input("Please input either 1/2\n press enter to return to main menu\n: ")
            if check == "" or check.isspace():
                main()
            if check.upper() == "1":
                Player1_UN_SINGLE()
            if check.upper() == "2":
                register_new()
    else:
        print("Retruning to main menu")
        main()
def player_1_choose_SINGLE(x):
    player_1 = []
    global Player1_1, Player1_2, Player1_3
    for number in range (3):
        printsub("P1 Select your heroes")   
        print("1.Warrior\t2.Tanker\t3.Wizard\t4.Main Menu")
        print()
        Input = input("P1: ")
        if Input != '1' and Input != '2' and Input != '3' or Input == "" or Input.isspace():
            print("Invalid input, returning to main menu")
            main()
        else:
            if Input == "1":
                player_1.append("Warrior")
            if Input == "2":
                player_1.append("Tanker")
            if Input == "3":
                player_1.append("Wizard")
    for z in range(3):
        print()
        name = input("Please enter your hero name: ")
        while name == "" or name.isspace():
            name = input("INVALID NAME! Please enter a valid hero name (cannot be blank): ")
        if player_1[z] == "Warrior":
            if z == 0:
                Player1_1 = Hero.Hero(Hero.Warrior)
                player_1[z] = name
                player_1[z] += "(Warrior)"
            if z == 1:
                Player1_2 = Hero.Hero(Hero.Warrior)
                player_1[z] = name
                player_1[z] += "(Warrior)"
            if z == 2:
                Player1_3 = Hero.Hero(Hero.Warrior)
                player_1[z] = name
                player_1[z] += "(Warrior)"
        if player_1[z] == "Tanker":
            if z == 0:
                Player1_1 = Hero.Hero(Hero.Tanker)
                player_1[z] = name
                player_1[z] += "(Tanker)"
            if z == 1:
                Player1_2 = Hero.Hero(Hero.Tanker)
                player_1[z] = name
                player_1[z] += "(Tanker)"
            if z == 2:
                Player1_3 = Hero.Hero(Hero.Tanker)
                player_1[z] = name
                player_1[z] += "(Tanker)"
        if player_1[z] == "Wizard":
            if z == 0:
                Player1_1 = Hero.Hero(Hero.Wizard)
                player_1[z] = name
                player_1[z] += "(Wizard)"
            if z == 1:
                Player1_2 = Hero.Hero(Hero.Wizard)
                player_1[z] = name
                player_1[z] += "(Wizard)"
            if z == 2:
                Player1_3 = Hero.Hero(Hero.Wizard)
                player_1[z] = name
                player_1[z] += "(Wizard)"
    time = datetime.datetime.now()
    File = open(x, "a")
    File.writelines(str(time))
    File.write(" \t\t ")
    File.write("Player 1")
    File.write("\t\t")
    File.write(player_1[0])
    File.write("\t\t")
    File.write(player_1[1])
    File.write("\t\t")
    File.write(player_1[2])
    File.write("\tGameID(")
    File.write(str(gameID))
    File.write(")\n")
    File.close()
    print()
    print("Your Hero: ", player_1)
    print()
    Player2_UN_SINGLE(x.replace(".txt", "").strip(), player_1)
def Player2_UN_SINGLE(UnCheck,xyz):
    UN2 = "COMPUTER.txt"
    player_2_choose_SINGLE(UN2.strip(), xyz, UnCheck.replace(".txt", "").strip())
def player_2_choose_SINGLE(UN2,player_1,UN1):
    player_2 = []
    input("Press 'Enter' for the computer to choose heroes...")
    print()
    print("Computer is choosing 3 heroes")
    global Player2_1, Player2_2, Player2_3
    for number in range (3):
        Input = random.randint(1, 3)
        if Input == 1:
            player_2.append("Warrior")
        if Input == 2:
            player_2.append("Tanker")
        if Input == 3:
            player_2.append("Wizard")
    for z in range(3):
        if player_2[z] == "Warrior":
            if z == 0:
                Player2_1 = Hero.Hero(Hero.Warrior)
                player_2[z] = "Computer 1"
                player_2[z] += "(Warrior)"
            if z == 1:
                Player2_2 = Hero.Hero(Hero.Warrior)
                player_2[z] = "Computer 2"
                player_2[z] += "(Warrior)"
            if z == 2:
                Player2_3 = Hero.Hero(Hero.Warrior)
                player_2[z] = "Computer 3"
                player_2[z] += "(Warrior)"
        if player_2[z] == "Tanker":
            if z == 0:
                Player2_1 = Hero.Hero(Hero.Tanker)
                player_2[z] = "Computer 1"
                player_2[z] += "(Tanker)"
            if z == 1:
                Player2_2 = Hero.Hero(Hero.Tanker)
                player_2[z] = "Computer 2"
                player_2[z] += "(Tanker)"
            if z == 2:
                Player2_3 = Hero.Hero(Hero.Tanker)
                player_2[z] = "Computer 3"
                player_2[z] += "(Tanker)"
        if player_2[z] == "Wizard":
            if z == 0:
                Player2_1 = Hero.Hero(Hero.Wizard)
                player_2[z] = "Computer 1"
                player_2[z] += "(Wizard)"
            if z == 1:
                Player2_2 = Hero.Hero(Hero.Wizard)
                player_2[z] = "Computer 2"
                player_2[z] += "(Wizard)"
            if z == 2:
                Player2_3 = Hero.Hero(Hero.Wizard)
                player_2[z] = "Computer 3"
                player_2[z] += "(Wizard)"
    time = datetime.datetime.now()
    File = open(UN2, "a")
    File.writelines(str(time))
    File.write(" \t\t ")
    File.write("Player2(COM)")
    File.write("\t\t")
    File.write(player_2[0])
    File.write("\t\t")
    File.write(player_2[1])
    File.write("\t\t")
    File.write(player_2[2])
    File.write("\tGameID(")
    File.write(str(gameID))
    File.write(")\n")
    File.close()
    print()
    print("Computer's Hero: ", player_2)
    print()
    input("Press 'Enter' to start the battle...")
    print()
    turn = 1
    StartGame.singleGame(Player1_1, Player1_2, Player1_3, Player2_1, Player2_2, Player2_3, player_1, player_2, gameID, UN1.replace(".txt", "").strip(), UN2.replace(".txt", "").strip(), turn)


############################################################################################################################################################################################
######################################################  USER CHECK #########################################################################################################################

def register_new():
    File = open("Game.txt", "r")
    print()
    Input = input("Please enter a unique username or Press 'Enter' to return to main menu: ")
    if Input == "" or Input.isspace():
        main()
    if Input.upper == "COMPUTER":
        File.close()
        register_new_taken()
    else:
        for line in File:
            if Input in line:
                register_new_taken()
        File.close()
        write_new(Input)
def register_new_taken():
    file = open("Game.txt", "r")
    print()
    Input = ""
    while Input == "COMPUTER":
        Input = input("The username is taken! (not case sen.)\nPress 'Enter' to return to main menu(Computer is not allowed): ")
    if Input == "" or Input.isspace():
        main()
    else:
        for line in file:
            if Input in line:
                file.close()
                register_new_taken()
        file.close()
        write_new(Input)
def write_new(Input):
    File = open("Game.txt", "a")
    Input = "UN: " + Input
    File.write(Input)
    File.write("\n")
    File.close()
    a = "{}.txt"
    a = a.format(Input). replace("UN: ", "")
    File = open(a, "a")
    File.writelines("Date and Time \t\t\t\t Player Slot \t\t Hero 1 \t\t Hero 2 \t\t Hero 3\n")
    File.close()
    print()
    print("SUCCESS!")
    main()
def Game_ID():
    gameID = ""
    for Range in range (6):
        new = random.randint(0, 9)
        new = str(new)
        gameID += new
    FILE = open("Gamelog.txt", "r")
    for LINE in FILE:
        if gameID in LINE:
            FILE.close()
            Game_ID()
    FILE.close()
    return gameID
###############################################################################################################################################################################################
###############################################################################################################################################################################################
#########################   COPNTINUE AND REPLAY #############################################################################################################################################
##############################################################################################################################################################################################
def CONTINUE():
    print("CONTINUE")
    UN1 = input("UN: ")
    File = open("Game.txt", "r")
    Line = File.readline()
    while Line != "" and not Line.isspace():
        Scan_line = Line.replace('UN: ', '')
        if Scan_line.lower().strip() == UN1.lower().strip():
            File.close()
            UN1 = Scan_line.strip() + '.txt'
            OPEN_FILE_CONTINUE(UN1)
        else:
            Line = File.readline()
            continue
    else:
        File.close()
        check = input("Your username is not registered!\nPress 'enter' to return to main menu\nPress N to Create new")
        if check == "" or check.isspace():
            main()
        if check.upper() == "N":
            register_new()
        else:
            print("Error , returning to maine menu")
def OPEN_FILE_CONTINUE(UN):
    UN1 = UN
    file = open(UN1, "r")
    for line in file:
        print(line)
    file.close()
    x = input("Game ID: ")
    file = open("Gamelog.txt", "r")
    for line in file:
        if x in line:
            line2 = file.readlines()
    if line2 == "" or line2 == " ":
        file.close()
        print("file was not found")
        input("press enter to return to main menu")
        main()
    if line2 != "" or line2 != " ":
        file.close()
        last_turn = line2[len(line2) - 1].split()
    #########################################################################################################################################################################################
    #########################################################################################################################################################################################
    #[0'ID:(099132)', 1'TURN:3', 2'Type:', 3'Single',
    #4'Jonathan',
    #5'name(Warrior)',             6'Health:',  7 '35/50', 8 'lvl:', 9'1', 10'exp:', 11'20', 12'FreezeTIME:', 13'0', 14'PoisonDMG:', 15'0',
    #16'name(Tanker)',            17'Health:', 18'60/60', 19'lvl:', 20'1', 21'exp:', 22'9',  23'FreezeTIME:', 24'0', 25'PoisonDMG:', 26'0',
    #27'name(Wizard)',            28'Health:', 29'34/40', 30'lvl:', 31'1', 32'exp:', 33'7',  34'FreezeTIME:', 35'0', 36'PoisonDMG:', 37'0',
    #38'COMPUTER',
    #39'Computer', 40'1(Wizard)', 41'Health:', 42'28/40', 43'lvl:', 44'1', 45'exp:', 46'7',  47'FreezeTIME:', 48'0', 49'PoisonDMG:', 50'0',
    #51'Computer', 52'2(Tanker)', 53'Health:', 54'56/60', 55'lvl:', 56'1', 57'exp:', 58'13', 59'FreezeTIME:', 60'0', 61'PoisonDMG:', 62'0',
    #63'Computer', 64'3(Warrior)',65'Health:', 66'48/50', 67'lvl:', 68'1', 69'exp:', 70'19', 71'FreezeTIME:', 72'0', 73'PoisonDMG:', 74'0']
    player_1 = ["","",""]
    player_2 = ["","",""]
    gameMode = last_turn[3]
    if gameMode == "Single":
        gameID = last_turn[0].replace("ID:(", "").replace(")", "")
        turn = int(str(last_turn[1].replace("TURN:", "")))
        Type = last_turn[3]
        UN1 = last_turn[4]
        UN2 = last_turn[38]
        player_1[0] = last_turn[5]
        player_1[1] = last_turn[16]
        player_1[2] = last_turn[27]
        if UN2.upper() == "COMPUTER":
            player_2[0] = last_turn[39] + " " + last_turn[40]
            player_2[1] = last_turn[51] + " " + last_turn[52]
            player_2[2] = last_turn[63] + " " + last_turn[64]
        for z in range(3):
            if "Warrior" in player_1[z]:
                if z == 0:
                    Player1_1 = Hero.Hero(Hero.Warrior)
                if z == 1:
                    Player1_2 = Hero.Hero(Hero.Warrior)
                if z == 2:
                    Player1_3 = Hero.Hero(Hero.Warrior)
            if "Tanker" in player_1[z]:
                if z == 0:
                    Player1_1 = Hero.Hero(Hero.Tanker)
                if z == 1:
                    Player1_2 = Hero.Hero(Hero.Tanker)
                if z == 2:
                    Player1_3 = Hero.Hero(Hero.Tanker)
            if "Wizard" in player_1[z]:
                if z == 0:
                    Player1_1 = Hero.Hero(Hero.Wizard)
                if z == 1:
                    Player1_2 = Hero.Hero(Hero.Wizard)
                if z == 2:
                    Player1_3 = Hero.Hero(Hero.Wizard)
        z = 0
        for z in range(3):
            if "Warrior" in player_2[z]:
                if z == 0:
                    Player2_1 = Hero.Hero(Hero.Warrior)
                if z == 1:
                    Player2_2 = Hero.Hero(Hero.Warrior)
                if z == 2:
                    Player2_3 = Hero.Hero(Hero.Warrior)
            if "Tanker" in player_2[z]:
                if z == 0:
                    Player2_1 = Hero.Hero(Hero.Tanker)
                if z == 1:
                    Player2_2 = Hero.Hero(Hero.Tanker)
                if z == 2:
                    Player2_3 = Hero.Hero(Hero.Tanker)
            if "Wizard" in player_2[z]:
                if z == 0:
                    Player2_1 = Hero.Hero(Hero.Wizard)
                if z == 1:
                    Player2_2 = Hero.Hero(Hero.Wizard)
                if z == 2:
                    Player2_3 = Hero.Hero(Hero.Wizard)
        #########################################################################################################################################################################################
        #########################################################################################################################################################################################
        #[0'ID:(099132)', 1'TURN:3', 2'Type:', 3'Single',
        #4'Jonathan',
        #5'name(Warrior)',             6'Health:',  7 '35/50', 8 'lvl:', 9'1', 10'exp:', 11'20', 12'FreezeTIME:', 13'0', 14'PoisonDMG:', 15'0',
        #16'name(Tanker)',            17'Health:', 18'60/60', 19'lvl:', 20'1', 21'exp:', 22'9',  23'FreezeTIME:', 24'0', 25'PoisonDMG:', 26'0',
        #27'name(Wizard)',            28'Health:', 29'34/40', 30'lvl:', 31'1', 32'exp:', 33'7',  34'FreezeTIME:', 35'0', 36'PoisonDMG:', 37'0',
        #38'COMPUTER',
        #39'Computer', 40'1(Wizard)', 41'Health:', 42'28/40', 43'lvl:', 44'1', 45'exp:', 46'7',  47'FreezeTIME:', 48'0', 49'PoisonDMG:', 50'0',
        #51'Computer', 52'2(Tanker)', 53'Health:', 54'56/60', 55'lvl:', 56'1', 57'exp:', 58'13', 59'FreezeTIME:', 60'0', 61'PoisonDMG:', 62'0',
        #63'Computer', 64'3(Warrior)',65'Health:', 66'48/50', 67'lvl:', 68'1', 69'exp:', 70'19', 71'FreezeTIME:', 72'0', 73'PoisonDMG:', 74'0']
        Player1_1.lvl = int(last_turn[9])
        Player1_2.lvl = int(last_turn[20])
        Player1_3.lvl = int(last_turn[31])
        if UN2.upper() == "COMPUTER":
            Player2_1.lvl = int(last_turn[44])
            Player2_2.lvl = int(last_turn[56])
            Player2_3.lvl = int(last_turn[68])
        ##################################
        Player1_1.exp = int(last_turn[11])
        Player1_2.exp = int(last_turn[22])
        Player1_3.exp = int(last_turn[33])
        if UN2.upper() == "COMPUTER":
            Player2_1.exp = int(last_turn[46])
            Player2_2.exo = int(last_turn[58])
            Player2_3.exp = int(last_turn[70])
        ##################################
        Player1_1.CurrentHealth = int(str(last_turn[7]).replace("/" + str(Player1_1.MaxHealth[Player1_1.lvl - 1]), ""))
        Player1_2.CurrentHealth = int(str(last_turn[18]).replace("/" + str(Player1_2.MaxHealth[Player1_2.lvl - 1]), ""))
        Player1_3.CurrentHealth = int(str(last_turn[29]).replace("/" + str(Player1_3.MaxHealth[Player1_3.lvl - 1]), ""))
        if UN2.upper() == "COMPUTER":
            Player2_1.CurrentHealth = int(str(last_turn[42]).replace("/" + str(Player2_1.MaxHealth[Player2_1.lvl - 1]), ""))
            Player2_2.CurrentHealth = int(str(last_turn[54]).replace("/" + str(Player2_2.MaxHealth[Player2_2.lvl - 1]), ""))
            Player2_3.CurrentHealth = int(str(last_turn[66]).replace("/" + str(Player2_3.MaxHealth[Player2_3.lvl - 1]), ""))
        ################################
        Player1_1.FreezeTurn = int(last_turn[13])
        Player1_2.FreezeTurn = int(last_turn[24])
        Player1_3.FreezeTurn = int(last_turn[35])
        if UN2.upper() == "COMPUTER":
            Player2_1.FreezeTurn = int(last_turn[48])
            Player2_2.FreezeTurn = int(last_turn[60])
            Player2_3.FreezeTurn = int(last_turn[72])
        #################################
        Player1_1.PoisonDMG = int(last_turn[15])
        Player1_2.PoisonDMG = int(last_turn[26])
        Player1_3.PoisonDMG = int(last_turn[37])
        if UN2.upper() == "COMPUTER":
            Player2_1.PoisonDMG = int(last_turn[50])
            Player2_2.PoisonDMG = int(last_turn[62])
            Player2_3.PoisonDMG = int(last_turn[74])
        ################################
        if Player1_1.PoisonDMG != 0:
            Player1_1.Status += " Poison"
        if Player1_1.FreezeTurn != 0:
            Player1_1.Status += " Freeze"
        if Player1_2.PoisonDMG != 0:
            Player1_2.Status += " Poison"
        if Player1_2.FreezeTurn != 0:
            Player1_2.Status += " Freeze"
        if Player1_3.PoisonDMG != 0:
            Player1_3.Status += " Poison"
        if Player1_3.FreezeTurn != 0:
            Player1_3.Status += " Freeze"
        if Player2_1.PoisonDMG != 0:
            Player2_1.Status += " Poison"
        if Player2_1.FreezeTurn != 0:
            Player2_1.Status += " Freeze"
        if Player2_2.PoisonDMG != 0:
            Player2_2.Status += " Poison"
        if Player2_2.FreezeTurn != 0:
            Player2_2.Status += " Freeze"
        if Player2_3.PoisonDMG != 0:
            Player2_3.Status += " Poison"
        if Player2_3.FreezeTurn != 0:
            Player2_3.Status += " Freeze"
        ################################
        StartGame.singleGame(Player1_1, Player1_2, Player1_3, Player2_1, Player2_2, Player2_3, player_1, player_2, gameID, UN1.replace(".txt", "").strip(), UN2.replace(".txt", "").strip(), turn)
    #########################################################################################################################################################################################
    #########################################################################################################################################################################################
    #[0'ID:(099132)', 1'TURN:3', 2'Type:', 3'Single',
    #4'Jonathan',
    #5'name(Warrior)',             6'Health:',  7 '35/50', 8 'lvl:', 9'1', 10'exp:', 11'20', 12'FreezeTIME:', 13'0', 14'PoisonDMG:', 15'0',
    #16'name(Tanker)',            17'Health:', 18'60/60', 19'lvl:', 20'1', 21'exp:', 22'9',  23'FreezeTIME:', 24'0', 25'PoisonDMG:', 26'0',
    #27'name(Wizard)',            28'Health:', 29'34/40', 30'lvl:', 31'1', 32'exp:', 33'7',  34'FreezeTIME:', 35'0', 36'PoisonDMG:', 37'0',
    #38'COMPUTER',
    #39'Computer',                40'Health:', 41'28/40', 42'lvl:', 43'1', 44'exp:', 45'7',  46'FreezeTIME:', 47'0', 48'PoisonDMG:', 49'0',
    #50'Computer',                51'Health:', 52'56/60', 53'lvl:', 54'1', 55'exp:', 56'13', 57'FreezeTIME:', 58'0', 59'PoisonDMG:', 60'0',
    #61'Computer',                62'Health:', 63'48/50', 64'lvl:', 65'1', 66'exp:', 67'19', 68'FreezeTIME:', 69'0', 73'PoisonDMG:', 70'0']
    player_1 = ["","",""]
    player_2 = ["","",""]
    gameMode = last_turn[3]
    if gameMode == "Multi":
        gameID = last_turn[0].replace("ID:(", "").replace(")", "")
        turn = int(str(last_turn[1].replace("TURN:", "")))
        Type = last_turn[3]
        UN1 = last_turn[4]
        UN2 = last_turn[38]
        player_1[0] = last_turn[5]
        player_1[1] = last_turn[16]
        player_1[2] = last_turn[27]
        player_2[0] = last_turn[39]
        player_2[1] = last_turn[51]
        player_2[2] = last_turn[63]
        for z in range(3):
            if "Warrior" in player_1[z]:
                if z == 0:
                    Player1_1 = Hero.Hero(Hero.Warrior)
                if z == 1:
                    Player1_2 = Hero.Hero(Hero.Warrior)
                if z == 2:
                    Player1_3 = Hero.Hero(Hero.Warrior)
            if "Tanker" in player_1[z]:
                if z == 0:
                    Player1_1 = Hero.Hero(Hero.Tanker)
                if z == 1:
                    Player1_2 = Hero.Hero(Hero.Tanker)
                if z == 2:
                    Player1_3 = Hero.Hero(Hero.Tanker)
            if "Wizard" in player_1[z]:
                if z == 0:
                    Player1_1 = Hero.Hero(Hero.Wizard)
                if z == 1:
                    Player1_2 = Hero.Hero(Hero.Wizard)
                if z == 2:
                    Player1_3 = Hero.Hero(Hero.Wizard)
        z = 0
        for z in range(3):
            if "Warrior" in player_2[z]:
                if z == 0:
                    Player2_1 = Hero.Hero(Hero.Warrior)
                if z == 1:
                    Player2_2 = Hero.Hero(Hero.Warrior)
                if z == 2:
                    Player2_3 = Hero.Hero(Hero.Warrior)
            if "Tanker" in player_2[z]:
                if z == 0:
                    Player2_1 = Hero.Hero(Hero.Tanker)
                if z == 1:
                    Player2_2 = Hero.Hero(Hero.Tanker)
                if z == 2:
                    Player2_3 = Hero.Hero(Hero.Tanker)
            if "Wizard" in player_2[z]:
                if z == 0:
                    Player2_1 = Hero.Hero(Hero.Wizard)
                if z == 1:
                    Player2_2 = Hero.Hero(Hero.Wizard)
                if z == 2:
                    Player2_3 = Hero.Hero(Hero.Wizard)
    #########################################################################################################################################################################################
    #########################################################################################################################################################################################
    #[0'ID:(099132)', 1'TURN:3', 2'Type:', 3'Single',
    #4'Jonathan',
    #5'name(Warrior)',             6'Health:',  7 '35/50', 8 'lvl:', 9'1', 10'exp:', 11'20', 12'FreezeTIME:', 13'0', 14'PoisonDMG:', 15'0',
    #16'name(Tanker)',            17'Health:', 18'60/60', 19'lvl:', 20'1', 21'exp:', 22'9',  23'FreezeTIME:', 24'0', 25'PoisonDMG:', 26'0',
    #27'name(Wizard)',            28'Health:', 29'34/40', 30'lvl:', 31'1', 32'exp:', 33'7',  34'FreezeTIME:', 35'0', 36'PoisonDMG:', 37'0',
    #38'COMPUTER',
    #39'Computer',                40'Health:', 41'28/40', 42'lvl:', 43'1', 44'exp:', 45'7',  46'FreezeTIME:', 47'0', 48'PoisonDMG:', 49'0',
    #50'Computer',                51'Health:', 52'56/60', 53'lvl:', 54'1', 55'exp:', 56'13', 57'FreezeTIME:', 58'0', 59'PoisonDMG:', 60'0',
    #61'Computer',                62'Health:', 63'48/50', 64'lvl:', 65'1', 66'exp:', 67'19', 68'FreezeTIME:', 69'0', 73'PoisonDMG:', 70'0']
        Player1_1.lvl = int(last_turn[9])
        Player1_2.lvl = int(last_turn[20])
        Player1_3.lvl = int(last_turn[31])
        Player2_1.lvl = int(last_turn[43])
        Player2_2.lvl = int(last_turn[54])
        Player2_3.lvl = int(last_turn[65])
        ##################################
        Player1_1.exp = int(last_turn[11])
        Player1_2.exp = int(last_turn[22])
        Player1_3.exp = int(last_turn[33])
        Player2_1.exp = int(last_turn[45])
        Player2_2.exo = int(last_turn[56])
        Player2_3.exp = int(last_turn[67])
        ##################################
        Player1_1.CurrentHealth = int(str(last_turn[7]).replace("/" + str(Player1_1.MaxHealth[Player1_1.lvl - 1]), ""))
        Player1_2.CurrentHealth = int(str(last_turn[18]).replace("/" + str(Player1_2.MaxHealth[Player1_2.lvl - 1]), ""))
        Player1_3.CurrentHealth = int(str(last_turn[29]).replace("/" + str(Player1_3.MaxHealth[Player1_3.lvl - 1]), ""))
        Player2_1.CurrentHealth = int(str(last_turn[41]).replace("/" + str(Player2_1.MaxHealth[Player2_1.lvl - 1]), ""))
        Player2_2.CurrentHealth = int(str(last_turn[52]).replace("/" + str(Player2_2.MaxHealth[Player2_2.lvl - 1]), ""))
        Player2_3.CurrentHealth = int(str(last_turn[63]).replace("/" + str(Player2_3.MaxHealth[Player2_3.lvl - 1]), ""))
        ################################
        Player1_1.FreezeTurn = int(last_turn[13])
        Player1_2.FreezeTurn = int(last_turn[24])
        Player1_3.FreezeTurn = int(last_turn[35])
        Player2_1.FreezeTurn = int(last_turn[47])
        Player2_2.FreezeTurn = int(last_turn[58])
        Player2_3.FreezeTurn = int(last_turn[69])
        #################################
        Player1_1.PoisonDMG = int(last_turn[15])
        Player1_2.PoisonDMG = int(last_turn[26])
        Player1_3.PoisonDMG = int(last_turn[37])
        Player2_1.PoisonDMG = int(last_turn[49])
        Player2_2.PoisonDMG = int(last_turn[60])
        Player2_3.PoisonDMG = int(last_turn[70])
        ################################
        if Player1_1.PoisonDMG != 0:
            Player1_1.Status += " Poison"
        if Player1_1.FreezeTurn != 0:
            Player1_1.Status += " Freeze"
        if Player1_2.PoisonDMG != 0:
            Player1_2.Status += " Poison"
        if Player1_2.FreezeTurn != 0:
            Player1_2.Status += " Freeze"
        if Player1_3.PoisonDMG != 0:
            Player1_3.Status += " Poison"
        if Player1_3.FreezeTurn != 0:
            Player1_3.Status += " Freeze"
        if Player2_1.PoisonDMG != 0:
            Player2_1.Status += " Poison"
        if Player2_1.FreezeTurn != 0:
            Player2_1.Status += " Freeze"
        if Player2_2.PoisonDMG != 0:
            Player2_2.Status += " Poison"
        if Player2_2.FreezeTurn != 0:
            Player2_2.Status += " Freeze"
        if Player2_3.PoisonDMG != 0:
            Player2_3.Status += " Poison"
        if Player2_3.FreezeTurn != 0:
            Player2_3.Status += " Freeze"
        ################################
        StartGame.game(Player1_1, Player1_2, Player1_3, Player2_1, Player2_2, Player2_3, player_1, player_2, gameID, UN1.replace(".txt", "").strip(), UN2.replace(".txt", "").strip(), turn)
        
    input("Press 'enter' to return to main menu")
    main()
def REPLAY():
    print("REPLAY")
    UN1 = input("UN: ")
    File = open("Game.txt", "r")
    Line = File.readline()
    while Line != "" and not Line.isspace():
        Scan_line = Line.replace('UN: ', '')
        if Scan_line.lower().strip() == UN1.lower().strip():
            File.close()
            UN1 = Scan_line.strip() + '.txt'
            OPEN_FILE_REPLAY(UN1)
        else:
            Line = File.readline()
            continue
    else:
        File.close()
        check = input("Your username is not registered!\nPress 'enter' to return to main menu\nPress N to Create new")
        if check == "" or check.isspace():
            main()
        if check.upper() == "N":
            register_new()
        else:
            print("Error , returning to maine menu")
def OPEN_FILE_REPLAY(UN):
    UN1 = UN
    file = open(UN1 , "r")
    for line in file:
        print(line)
    file.close()
    file = open("Gamelog.txt", "r")
    x = input("GameID: ")
    for line in file:
        if x in line and len(line) <= 400:
            line2 = line
            print(line2)
    if line2 == "" or line2.isspace():
        print("file was not found")
    input("Press 'enter' to return to main menu")
    main()
    
main()
