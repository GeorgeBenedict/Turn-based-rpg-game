import Hero
import random
def game(z,x,c,v,b,n,m,a,gameID,UN1,UN2,turn):
########################################################################################################
################################## READ THIS TABLE FIRST PLAESE ########################################
########################################################################################################
##    z = Player 1 slot 1       }   (HERO)                                                            ##
##    x = Player 1 slot 2       }   (HERO)                                                            ##
##    c = Player 1 slot 3       }   (HERO)                                                            ##
##    v = Player 2 slot 1       }   (HERO)                                                            ##
##    b = Player 2 slot 2       }   (HERO)                                                            ##
##    n = Player 2 slot 3       }   (HERO)                                                            ##
##    m = Player 1 hero list and name                                                                 ##
##    a = Plauer 2 hero list and name                                                                 ##
########################################################################################################
##    Hero command =                                                                                  ##
##    damage(x)       x = attack from enemy                                                           ##
##    attack()                                                                                        ##
########################################################################################################
##    Hero Data command list:                                                                         ##
##    HERO.MaxHealth[HERO.lvl - 1]    =   HERO's max health (can change base on lvl)(max health pool) ##
##    HERO.CurrentHealth  =   HERO's current health (number can change)                               ##
##    HERO.Attack[HERO.lvl - 1]   =   HERO's base attack (can change base on lvl)                     ##
##    HERO.Defense[HERO.lvl - 1]  =   HERO's defense (can change base on lvl)                         ##
##    HERO.Status =   HERO's current debuff status                                                    ##
##    HERO.lvl    =   HERO's current lvl                                                              ##
##    HERO.exp    =   HERO's current exp                                                              ##
##    Hero.PoisonDMG   =   HERO's poison DMG Format = Hero.Poison(Hero, Poison DMG)                   ##
##    HERO.Freeze =   unfreeze turn     Format = Hero.Freeze(HERO, turn)                              ##
########################################################################################################
    gameType = "Multi"
    print ("____________________")
    print ("Let the battle begin")
    print ("####################\n")
    while (z.CurrentHealth > 0 and x.CurrentHealth > 0  and c.CurrentHealth > 0) or (v.CurrentHealth > 0 and b.CurrentHealth > 0  and n.CurrentHealth > 0):
        if turn % 2 != 0:
            for turnloop in range (3):
                for checking_status in range(6):
                    if checking_status == 0:
                        HERO_CHECK = z
                    if checking_status == 1:
                        HERO_CHECK = x
                    if checking_status == 2:
                        HERO_CHECK = c
                    if checking_status == 3:
                        HERO_CHECK = v
                    if checking_status == 4:
                        HERO_CHECK = b
                    if checking_status == 5:
                        HERO_CHECK = n
                    if "Poison" in HERO_CHECK.Status or "Freeze" in HERO_CHECK.Status:
                        HERO_CHECK.Status = HERO_CHECK.Status.replace(" None", "")
                    if HERO_CHECK.Status == "" or HERO_CHECK.Status.isspace():
                        HERO_CHECK.Status += " None"
                    if HERO_CHECK.CurrentHealth <= 0:
                        HERO_CHECK.CurrentHealth = 0
                print("Game ID: ", gameID)
                print("TURN = ", turn)
                print("Player 1's slot 1: \n", z,"\nPlayer 1's slot 2 \n", x,"\nPlayer 1's slot 3 \n", c,"\nPlayer 2's slot 1 \n", v, "\nPlayer 2's slot 2\n", b,"\nPlayer 2's slot 3 \n", n)
                battle_in_turn(z,x,c,v,b,n,m,a,gameID,UN1,UN2,turn,turnloop)
                if z.CurrentHealth <= 0 and x.CurrentHealth <= 0 and c.CurrentHealth <= 0:
                    print(UN2," is the winner!!")
                    input("Press enter to return to EXIT")
                    exit()
                if v.CurrentHealth <= 0 and b.CurrentHealth <= 0 and n.CurrentHealth <= 0:
                    print(UN1," is the winner!!")
                    input("Press enter to return to EXIT")
                    exit()
                if turnloop == 2:
                    checking_status = 0
                    for checking_status in range(6):
                        if checking_status == 0:
                            HERO_CHECK = z
                        if checking_status == 1:
                            HERO_CHECK = x
                        if checking_status == 2:
                            HERO_CHECK = c
                        if checking_status == 3:
                            HERO_CHECK = v
                        if checking_status == 4:
                            HERO_CHECK = b
                        if checking_status == 5:
                            HERO_CHECK = n
                        if "Poison" in HERO_CHECK.Status or "Freeze" in HERO_CHECK.Status:
                            HERO_CHECK.Status = HERO_CHECK.Status.replace(" None", "")
                        if HERO_CHECK.Status == "" or HERO_CHECK.Status.isspace():
                            HERO_CHECK.Status += " None"
                        if HERO_CHECK.CurrentHealth <= 0:
                            HERO_CHECK.CurrentHealth = 0
                    turn += 1
                    printData(gameID, UN1, z, x, c, m, UN2, v, b, n, a, turn, gameType)
                    Save_exit = input("Press enter to continue\npress 's' to save and exit\n:")
                    if Save_exit.lower() == "s":
                        print("Exiting..")
                        exit()
############################################################################################################################################################################################

        if turn % 2 == 0:
            for turnloop in range(3):
                for checking_status in range(6):
                    if checking_status == 0:
                        HERO_CHECK = z
                    if checking_status == 1:
                        HERO_CHECK = x
                    if checking_status == 2:
                        HERO_CHECK = c
                    if checking_status == 3:
                        HERO_CHECK = v
                    if checking_status == 4:
                        HERO_CHECK = b
                    if checking_status == 5:
                        HERO_CHECK = n
                    if "Poison" in HERO_CHECK.Status or "Freeze" in HERO_CHECK.Status:
                        HERO_CHECK.Status = HERO_CHECK.Status.replace(" None", "")
                    if HERO_CHECK.Status == "" or HERO_CHECK.Status.isspace():
                        HERO_CHECK.Status += " None"
                    if HERO_CHECK.CurrentHealth <= 0:
                        HERO_CHECK.CurrentHealth = 0
                print("Game ID: ", gameID)
                print("TURN = ", turn)
                print("Player 1's slot 1: \n", z,"\nPlayer 1's slot 2 \n", x,"\nPlayer 1's slot 3 \n", c,"\nPlayer 2's slot 1 \n", v, "\nPlayer 2's slot 2\n", b,"\nPlayer 2's slot 3 \n", n)
                battle_in_turn(v,b,n,z,x,c,a,m,gameID,UN2,UN1,turn,turnloop)
                if z.CurrentHealth <= 0 and x.CurrentHealth <= 0 and c.CurrentHealth <= 0:
                    print(UN2," is the winner!!")
                    input("Press enter to return to main menu")
                    MainLOOP.main()
                if v.CurrentHealth <= 0 and b.CurrentHealth <= 0 and n.CurrentHealth <= 0:
                    print(UN1," is the winner!!")
                    input("Press enter to return to main menu")
                    MainLOOP.main()
                if turnloop == 2:
                    checking_status = 0
                    for checking_status in range(6):
                        if checking_status == 0:
                            HERO_CHECK = z
                        if checking_status == 1:
                            HERO_CHECK = x
                        if checking_status == 2:
                            HERO_CHECK = c
                        if checking_status == 3:
                            HERO_CHECK = v
                        if checking_status == 4:
                            HERO_CHECK = b
                        if checking_status == 5:
                            HERO_CHECK = n
                        if "Poison" in HERO_CHECK.Status or "Freeze" in HERO_CHECK.Status:
                            HERO_CHECK.Status = HERO_CHECK.Status.replace(" None", "")
                        if HERO_CHECK.Status == "" or HERO_CHECK.Status.isspace():
                            HERO_CHECK.Status += " None"
                        if HERO_CHECK.CurrentHealth <= 0:
                            HERO_CHECK.CurrentHealth = 0
                    turn += 1
                    printData(gameID, UN1, z, x, c, m, UN2, v, b, n, a, turn, gameType)
                    Save_exit = input("Press enter to continue\npress 's' to save and exit\n:")
                    if Save_exit.lower() == "s":
                        print("Exiting..")
                        exit()
########################################################################################################################################################################################
###########################################################################################################################################################################################  
def singleGame(z,x,c,v,b,n,m,a,gameID,UN1,UN2, turn):
    gameType = "Single"
    GID = gameID
    print ("____________________")
    print ("Let the battle begin")
    print ("####################\n")
    while (z.CurrentHealth > 0 and x.CurrentHealth > 0  and c.CurrentHealth > 0) or (v.CurrentHealth > 0 and b.CurrentHealth > 0  and n.CurrentHealth > 0):
        if turn % 2 != 0:
            for turnloop in range (3):
                for checking_status in range(6):
                    if checking_status == 0:
                        HERO_CHECK = z
                    if checking_status == 1:
                        HERO_CHECK = x
                    if checking_status == 2:
                        HERO_CHECK = c
                    if checking_status == 3:
                        HERO_CHECK = v
                    if checking_status == 4:
                        HERO_CHECK = b
                    if checking_status == 5:
                        HERO_CHECK = n
                    if "Poison" in HERO_CHECK.Status or "Freeze" in HERO_CHECK.Status:
                        HERO_CHECK.Status = HERO_CHECK.Status.replace(" None", "")
                    if HERO_CHECK.Status == "" or HERO_CHECK.Status.isspace():
                        HERO_CHECK.Status += " None"
                    if HERO_CHECK.CurrentHealth <= 0:
                        HERO_CHECK.CurrentHealth = 0
                print("Game ID: ", gameID)
                print("TURN = ", turn)
                print()
                #print("Player 1's slot 1: \n", z,"\nPlayer 1's slot 2: \n", x,"\nPlayer 1's slot 3: \n", c,"\nPlayer 2's slot 1: \n", v, "\nPlayer 2's slot 2:\n", b,"\nPlayer 2's slot 3: \n", n)
                battle_in_turn(z,x,c,v,b,n,m,a,gameID,UN1,UN2,turn,turnloop)
                if z.CurrentHealth <= 0 and x.CurrentHealth <= 0 and c.CurrentHealth <= 0:
                    print(UN2," is the winner!!")
                    input("Press enter to return to EXIT")
                    exit()
                if v.CurrentHealth <= 0 and b.CurrentHealth <= 0 and n.CurrentHealth <= 0:
                    print(UN1," is the winner!!")
                    input("Press enter to return to EXIT")
                    exit()
                if turnloop == 2:
                    checking_status = 0
                    for checking_status in range(6):
                        if checking_status == 0:
                            HERO_CHECK = z
                        if checking_status == 1:
                            HERO_CHECK = x
                        if checking_status == 2:
                            HERO_CHECK = c
                        if checking_status == 3:
                            HERO_CHECK = v
                        if checking_status == 4:
                            HERO_CHECK = b
                        if checking_status == 5:
                            HERO_CHECK = n
                        if "Poison" in HERO_CHECK.Status or "Freeze" in HERO_CHECK.Status:
                            HERO_CHECK.Status = HERO_CHECK.Status.replace(" None", "")
                        if HERO_CHECK.Status == "" or HERO_CHECK.Status.isspace():
                            HERO_CHECK.Status += " None"
                        if HERO_CHECK.CurrentHealth <= 0:
                            HERO_CHECK.CurrentHealth = 0
                    turn += 1
                    printData(gameID, UN1, z, x, c, m, UN2, v, b, n, a, turn, gameType)
                    Save_exit = input("Press enter to continue\npress 's' to save and exit\n:")
                    if Save_exit.lower() == "s":
                        print("Exiting..")
                        exit()
############################################################################################################################################################################################
###########################################################################################################################################################################################
        if turn % 2 == 0:
            for turnloop in range(3):
                for checking_status in range(6):
                    if checking_status == 0:
                        HERO_CHECK = z
                    if checking_status == 1:
                        HERO_CHECK = x
                    if checking_status == 2:
                        HERO_CHECK = c
                    if checking_status == 3:
                        HERO_CHECK = v
                    if checking_status == 4:
                        HERO_CHECK = b
                    if checking_status == 5:
                        HERO_CHECK = n
                    if "Poison" in HERO_CHECK.Status or "Freeze" in HERO_CHECK.Status:
                        HERO_CHECK.Status = HERO_CHECK.Status.replace(" None", "")
                    if HERO_CHECK.Status == "" or HERO_CHECK.Status.isspace():
                        HERO_CHECK.Status == " None"
                    if HERO_CHECK.CurrentHealth <= 0:
                        HERO_CHECK.CurrentHealth = 0
                print("Game ID: ", gameID)
                print("TURN = ", turn)
                print()
                #print("Player 1's slot 1: \n", z,"\nPlayer 1's slot 2: \n", x,"\nPlayer 1's slot 3: \n", c,"\nPlayer 2's slot 1: \n", v, "\nPlayer 2's slot 2:\n", b,"\nPlayer 2's slot 3: \n", n)
                battle_in_turn_com(v,b,n,z,x,c,a,m,gameID,UN2,UN1,turn,turnloop)
                if z.CurrentHealth <= 0 and x.CurrentHealth <= 0 and c.CurrentHealth <= 0:
                    print(UN2," is the winner!!")
                    input("Press enter to return to EXIT")
                    exit()
                if v.CurrentHealth <= 0 and b.CurrentHealth <= 0 and n.CurrentHealth <= 0:
                    print(UN1," is the winner!!")
                    input("Press enter to return to EXIT")
                    exit()
                if turnloop == 2:
                    checking_status = 0
                    for checking_status in range(6):
                        if checking_status == 0:
                            HERO_CHECK = z
                        if checking_status == 1:
                            HERO_CHECK = x
                        if checking_status == 2:
                            HERO_CHECK = c
                        if checking_status == 3:
                            HERO_CHECK = v
                        if checking_status == 4:
                            HERO_CHECK = b
                        if checking_status == 5:
                            HERO_CHECK = n
                        if "Poison" in HERO_CHECK.Status or "Freeze" in HERO_CHECK.Status:
                            HERO_CHECK.Status = HERO_CHECK.Status.replace(" None", "")
                        if HERO_CHECK.Status == "" or HERO_CHECK.Status.isspace():
                            HERO_CHECK.Status == " None"
                        if HERO_CHECK.CurrentHealth <= 0:
                            HERO_CHECK.CurrentHealth = 0
                    turn += 1
                    printData(gameID, UN1, z, x, c, m, UN2, v, b, n, a, turn, gameType)
                    Save_exit = input("Press enter to continue\npress 's' to save and exit\n:")
                    if Save_exit.lower() == "s":
                        print("Exiting..")
                        exit()
        
###############################################################################################################################################################################################
###################################################
def printFile(GID, Hero, CurrentHealth, MaxHealth, lvl, exp, status):
    file = open("Gamelog.txt", "a")
    file.write("ID:(")
    file.write(GID)
    file.write(")\t") # diisis manual sama gio ata james ya
    file.write(str(Hero))
    file.write("\tHealth: ")
    file.write(str(CurrentHealth))
    file.write("/")
    file.write(str(MaxHealth))
    file.write("\tlvl = ")
    file.write(str(lvl))
    file.write("\t\texp = ")
    file.write(str(exp))
    file.write("\t\tstatus: ")
    file.write(status)
    file.write("\n")
    file.close()
    return

###########################################################################################################################################################################################
def printAttack(GID, apapun, apapun2, ATTACK, DEFENSE):
    file = open("Gamelog.txt", "a")
    file.write("ID:(")
    file.write(GID)
    file.write(")\t")
    file.write(str(apapun))
    file.write("\tattack\t\t")
    file.write(str(apapun2))
    file.write("\tattack = ")
    file.write(str(ATTACK))
    file.write("\tdefense = ")
    file.write(str(DEFENSE))
    file.write("\n")
    file.close()
    return
    
#########################################################################################################################################################################################
def printData(GID, Player1, z, x, c, m, Player2, v, b, n, a, turn, TYPE):
    file = open("Gamelog.txt", "a")
    file.write("ID:(")
    file.write(GID)
    file.write(")\tTURN:")
    file.write(str(turn))
    file.write("\tType: ")
    file.write(TYPE)
    file.write("\t")
    file.write(str(Player1))
    file.write("\t")
    file.write(str(m[0]))
    file.write("\tHealth: ")
    file.write(str(z.CurrentHealth))
    file.write("/")
    file.write(str(z.MaxHealth[z.lvl - 1]))
    file.write("\tlvl: ")
    file.write(str(z.lvl))
    file.write("\texp: ")
    file.write(str(z.exp))
    file.write("\tFreezeTIME: ")
    file.write(str(z.FreezeTurn))
    file.write("\tPoisonDMG: ")
    file.write(str(z.PoisonDMG))
    file.write("\t")
    file.write(str(m[1]))
    file.write("\tHealth: ")
    file.write(str(x.CurrentHealth))
    file.write("/")
    file.write(str(x.MaxHealth[x.lvl - 1]))
    file.write("\tlvl: ")
    file.write(str(x.lvl))
    file.write("\texp: ")
    file.write(str(x.exp))
    file.write("\tFreezeTIME: ")
    file.write(str(x.FreezeTurn))
    file.write("\tPoisonDMG: ")
    file.write(str(x.PoisonDMG))
    file.write("\t")
    file.write(str(m[2]))
    file.write("\tHealth: ")
    file.write(str(c.CurrentHealth))
    file.write("/")
    file.write(str(c.MaxHealth[c.lvl - 1]))
    file.write("\tlvl: ")
    file.write(str(c.lvl))
    file.write("\texp: ")
    file.write(str(c.exp))
    file.write("\tFreezeTIME: ")
    file.write(str(c.FreezeTurn))
    file.write("\tPoisonDMG: ")
    file.write(str(c.PoisonDMG))
    file.write("\t\t")
    file.write(str(Player2))
    file.write("\t")
    file.write(str(a[0]))
    file.write("\tHealth: ")
    file.write(str(v.CurrentHealth))
    file.write("/")
    file.write(str(v.MaxHealth[v.lvl - 1]))
    file.write("\tlvl: ")
    file.write(str(v.lvl))
    file.write("\texp: ")
    file.write(str(v.exp))
    file.write("\tFreezeTIME: ")
    file.write(str(v.FreezeTurn))
    file.write("\tPoisonDMG: ")
    file.write(str(v.PoisonDMG))
    file.write("\t")
    file.write(str(a[1]))
    file.write("\tHealth: ")
    file.write(str(b.CurrentHealth))
    file.write("/")
    file.write(str(b.MaxHealth[b.lvl - 1]))
    file.write("\tlvl: ")
    file.write(str(b.lvl))
    file.write("\texp: ")
    file.write(str(b.exp))
    file.write("\tFreezeTIME: ")
    file.write(str(b.FreezeTurn))
    file.write("\tPoisonDMG: ")
    file.write(str(b.PoisonDMG))
    file.write("\t")
    file.write(str(a[2]))
    file.write("\tHealth: ")
    file.write(str(n.CurrentHealth))
    file.write("/")
    file.write(str(n.MaxHealth[n.lvl - 1]))
    file.write("\tlvl: ")
    file.write(str(n.lvl))
    file.write("\texp: ")
    file.write(str(n.exp))
    file.write("\tFreezeTIME: ")
    file.write(str(n.FreezeTurn))
    file.write("\tPoisonDMG: ")
    file.write(str(n.PoisonDMG))
    file.write("\n")
    file.close()
    return
def WRITING_SPELL(GID, apapun, apapun2, SPELL):
    file = open("Gamelog.txt", "a")
    file.write("ID:(")
    file.write(GID)
    file.write(")\t")
    file.write(str(apapun))
    file.write("\tCast:")
    file.write(str(SPELL))
    file.write("\to\t\t")
    file.write(str(apapun2))
    file.write("\n")
    file.close()
    return
##########################################################################################################################################################################################
def battle_in_turn(z,x,c,v,b,n,m,a,gameID,UN1,UN2, turn, turnloop):
    GID = gameID
    if turnloop == 0:
        HERO = z
        Other1 = x
        Other2 = c
        hero = m[0]
        other1 = m[1]
        other2 = m[2]
    if turnloop == 1:
        HERO = x
        Other1 = z
        Other2 = c
        hero = m[1]
        other1 = m[0]
        other2 = m[2]
    if turnloop == 2:
        HERO = c
        Other1 = z
        Other2 = x
        hero = m[2]
        other1 = m[0]
        other2 = m[1]
    if HERO.CurrentHealth > 0:
        #print(HERO.FreezeTurn)
        print("-" *35)
        print (m[turnloop],"HERO turn to move\nYour HERO Status: ", HERO.Status)
        print("-" *35)
        if "Poison" in HERO.Status:
            HERO.CurrentHealth -= HERO.PoisonDMG
            print(HERO.PoisonDMG,"DMG has been dealt to", m[turnloop], "due to poison!!")
        if "Freeze" in HERO.Status and HERO.FreezeTurn == turn:
            HERO.Status = HERO.Status.replace("Freeze", "")
            HERO.FreezeTurn = 0
        elif "Freeze" in HERO.Status and HERO.FreezeTurn != turn:
            print("Hero was freeze")
            input("'Enter' to continue")
            return
        if "wizard" in m[turnloop].lower():
            heroOption = ""
            while heroOption == "" or heroOption.lower() != "a" and heroOption.lower() != "s" or heroOption.isspace():
                heroOption = input("(a)ttack\n(s)kill\n")
            if heroOption.lower() == "a":
###########################################################################################################################################################################################
###########################################################################################################################################################################################
###########################################################################################################################################################################################
                print("Available targets:\n","\n1.", a[0], ":\n", v, "\n2.", a[1], ":\n", b, "\n3.", a[2], ":\n", n) #, UN2, "'s Hero List:\n", a,
                attackTarget = input("Select a target: ")
                while attackTarget != "1" and attackTarget != "2" and attackTarget != "3" or attackTarget.isspace() or attackTarget == "":
                    attackTarget = input("Please Select a tarrget [1, 2, 3] : ")
                while v.CurrentHealth <= 0 and attackTarget == "1":
                    attackTarget = input("Please input other hero (choose hero with more than 0 health): ")
                while b.CurrentHealth <= 0 and attackTarget == "2":
                    attackTarget = input("Please input other hero (choose hero with more than 0 health): ")
                while n.CurrentHealth <= 0 and attackTarget == "3":
                    attackTarget = input("Please input other hero (choose hero with more than 0 heakth): ")
                if attackTarget == "1":
                    ATTACK = HERO.attack()
                    DAMAGE = v.damage(ATTACK)
                    printAttack(gameID, m[turnloop], a[0], ATTACK, v.Defense[v.lvl-1])
                    print("####################")
                    print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                    print("____________________")
                    print(UN2, "'s Hero:\n", v)
                    print("####################")
                    printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                    printFile(gameID, a[0], v.CurrentHealth, v.MaxHealth[v.lvl - 1], v.lvl, v.exp, v.Status)
                if attackTarget == "2":
                    ATTACK = HERO.attack()
                    DAMAGE = b.damage(ATTACK)
                    printAttack(gameID, m[turnloop], a[1], ATTACK, b.Defense[b.lvl-1])
                    print("####################")
                    print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                    print("____________________")
                    print(UN2,"'s Hero:\n", b)
                    print("####################")
                    printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                    printFile(gameID, a[1], b.CurrentHealth, b.MaxHealth[b.lvl - 1], b.lvl, b.exp, b.Status)
                if attackTarget == "3":
                    ATTACK = HERO.attack()
                    DAMAGE = n.damage(ATTACK)
                    printAttack(gameID, m[turnloop], a[2], ATTACK, n.Defense[n.lvl-1])
                    print("####################")
                    print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                    print("____________________")
                    print(UN2, "'s Hero:\n", n)
                    print("####################")
                    printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                    printFile(gameID, a[2], n.CurrentHealth, n.MaxHealth[n.lvl - 1], n.lvl, n.exp, n.Status)
###########################################################################################################################################################################################
###########################################################################################################################################################################################
###########################################################################################################################################################################################
            if heroOption.lower() == "s":
                Spell = ""
                if Other1.CurrentHealth <= 0 or Other2.CurrentHealth <= 0:
                    while Spell == "" and Spell != "1" and Spell != "2" and Spell != "3" and Spell != "4" and Spell != "5" or Spell.isspace():
                        Spell = input("What skill do you want to use? (PLEASE INPUT THE NUMBERS)\n1. Heal\n2. Poison\n3. Cure\n4. Freeze\n5. Revive\n:")
                else:
                    while Spell == "" and Spell != "1" and Spell != "2" and Spell != "3" and Spell != "4" or Spell.isspace():
                        Spell = input("What skill do you want to use? (PLEASE INPUT THE NUMBERS)\n1. Heal\n2. Poison\n3. Cure\n4. Freeze\n:")
                if Spell == "1":
                    if  Other1.CurrentHealth <= 0 and Other2.CurrentHealth <= 0 and HERO.CurrentHealth > 0:
                        Hero.Heal(HERO, HERO)
                        SPELL = "HEAL"
                        WRITING_SPELL(GID, hero, hero, SPELL)
                        print("Current Health: ", HERO.CurrentHealth)
                        input("enter to continue")
                    if  Other1.CurrentHealth == Other1.MaxHealth and Other2.CurrentHealth == Other2.MaxHealth and HERO.CurrentHealth < HERO.MaxHealth:
                        Hero.Heal(HERO, HERO)
                        SPELL = "HEAL"
                        WRITING_SPELL(GID, hero, hero, SPELL)
                        print("Current Health: ", HERO.CurrentHealth)
                        input("enter to continue")
                    if  Other1.CurrentHealth < Other1.MaxHealth and Other2.CurrentHealth == Other2.MaxHealth and HERO.CurrentHealth == HERO.MaxHealth:
                        Hero.Heal(Other1, HERO)
                        SPELL = "HEAL"
                        WRITING_SPELL(GID, hero, other1, SPELL)
                        print("Current Health: ", Other1.CurrentHealth)
                        input("enter to continue")
                    if  Other1.CurrentHealth == Other1.MaxHealth and Other2.CurrentHealth < Other2.MaxHealth and HERO.CurrentHealth == HERO.MaxHealth:
                        Hero.Heal(Other2, HERO)
                        SPELL = "HEAL"
                        WRITING_SPELL(GID, hero, other2, SPELL)
                        print("Current Health: ", Other2.CurrentHealth)
                        input("enter to continue")
                    else:
                        print("Target your friendly hero\n1. ", m[0], ":\n", z, "\n2.", m[1], ':\n', x,"\n3.", m[2],":\n",c )
                        friendlyTarget = input(":")
                        while friendlyTarget.isspace() or friendlyTarget != "1" and friendlyTarget != "2" and friendlyTarget != "3" or friendlyTarget == "":
                            fiendlyTarget = input("Please enter either [1/2/3]: ")
                        if friendlyTarget == "1" and Other1.CurrentHealth <= 0:
                            friendlyTarget = input("please enter hero with more than 0 health: ")
                        if friendlyTarget == "2" and Otehr2.CurrentHealth <= 0:
                            friendlyTarget = input("please enter hero with more than 0 health: ")
                        if  friendlyTarget == "1":
                            Hero.Heal(Other1, HERO)
                            SPELL = "HEAL"
                            WRITING_SPELL(GID, hero, other1, SPELL)
                            print("Current Health: ", Other1.CurrentHealth)
                            input("enter to continue")
                        if friendlyTarget == "2":
                            Hero.Heal(Other2, HERO)
                            SPELL = "HEAL"
                            WRITING_SPELL(GID, hero, other2, SPELL)
                            print("Current Health: ", Other2.CurrentHealth)
                            input("enter to continue")
                        if firendlyTarget == "3":
                            Hero.Heal(HERO, HERO)
                            SPELL = "HEAL"
                            WRITING_SPELL(GID, hero, hero, SPELL)
                            print("Current Health: ", HERO.CurrentHealth)
                            input("enter to continue")
                if Spell == "2":
                    print("Select an enemy hero to target (1,2,3)\n", UN2, "'s Hero List:\t", a, "\n", a[0], ":\n", v, "\n", a[1], ":\n", b, "\n", a[2], ":\n", n)
                    enemyTarget = input(": ")
                    while enemyTarget.isspace() or enemyTarget != "1" and enemyTarget != "2" and enemyTarget != "3" or enemyTarget.isspace():
                        enemyTarget = input("Please enter either [1/2/3]: ")
                    while v.CurrentHealth <= 0 and enemyTarget == "1":
                        enemyTarget = input("Please input other hero (choose hero with more than 0 health): ")
                    while b.CurrentHealth <= 0 and enemyTarget == "2":
                        enemyTarget = input("Please input other hero (choose hero with more than 0 health): ")
                    while n.CurrentHealth <= 0 and enemyTarget == "3":
                        enemyTarget = input("Please input other hero (choose hero with more than 0 heakth): ")
                    if enemyTarget == "1":
                        if not "Poison" in v.Status:
                            v.Status += " Poison"
                        Hero.Poison(v, Hero.STATUS[HERO.lvl - 1], HERO)
                        SPELL = "POISON"
                        WRITING_SPELL(GID, hero, a[0], SPELL)
                    if enemyTarget == "2":
                        if not "Poison" in b.Status:
                            b.Status += " Poison"
                        Hero.Poison(b, Hero.STATUS[HERO.lvl - 1], HERO)
                        SPELL = "POISON"
                        WRITING_SPELL(GID, hero, a[1], SPELL)
                    if enemyTarget == "3":
                        if not "Poison" in n.Status:
                            n.Status += " Poison"
                        Hero.Poison(n, Hero.STATUS[HERO.lvl - 1], HERO)
                        SPELL = "POISON"
                        WRITING_SPELL(GID, HERO, a[2], SPELL)
                if Spell == "3":
                    if"Poison" in Other1.Status and not "Poison" in Other2.Status and not "Poison" in HERO.Status:
                        Hero.Cure(Other1, HERO)
                        SPELL = "CURE"
                        WRITING_SPELL(GID, hero, other1, SPELL)
                        print("Status: ", Other1.Status)
                        input("enter to continue")
                    if not "Poison" in Other1.Status and "Poison" in Other2.Status and not "Poison" in HERO.Status:
                        Hero.Cure(Other2, HERO)
                        SPELL = "CURE"
                        WRITING_SPELL(GID, hero, other1, SPELL)
                        print("Status: ", Other1.Status)
                        input("enter to continue")
                    if not "Poison" in Other1.Status and not "Poison" in Other2.Status and "Poison" in HERO.Status:
                        Hero.Cure(HERO, HERO)
                        SPELL = "CURE"
                        WRITING_SPELL(GID, hero, hero, SPELL)
                        print("Status: ", Other1.Status)
                        input("enter to continue")
                    if "Poison" in HERO.Status and "Poison" in Other1.Status and "Poison" in Other2.Status:
                        print("Target your friendly hero\n1. ", m[0], ":\n", z, "\n2.", m[1], ':\n', x,"\n3.", m[2],":\n",c )
                        friendlyTarget = input(":")
                        while friendlyTarget.isspace() or fiendlyTarget != "1" and friendlyTarget != "2" and friendlyTarget != "3" or friendlyTarget.isspace():
                            fiendlyTarget = input("Please enter either [1/2/3]: ")
                            if friendlyTarget == "1" and not "Poison" in z.Status:
                                friendlyTarget = input("Please Choose Hero with POISON: ")
                            if friendlyTarget == "2" and not "Poison" in x.Status:
                                friendlyTarget = input("Please Choose Hero with POISON: ")
                            if friendlyTarget == "1" and not "Poison" in c.Status:
                                friendlyTarget = input("Please Choose Hero with POISON: ")
                        if  friendlyTarget == "1":
                            Hero.Cure(Other1, HERO)
                            SPELL = "CURE"
                            WRITING_SPELL(GID, hero, other1, SPELL)
                            print("Status: ", Other1.Status)
                            input("enter to continue")
                        if friendlyTarget == "2":
                            Hero.Cure(Other2, HERO)
                            SPELL = "CURE"
                            WRITING_SPELL(GID, hero, other2, SPELL)
                            print("Status: ", Other2.Status)
                            input("enter to continue")
                        if firendlyTarget == "3":
                            Hero.Cure(HERO, HERO)
                            SPELL = "CURE"
                            WRITING_SPELL(GID, hero, hero, SPELL)
                            print("Status: ", HERO.Status)
                            input("enter to continue")
                if Spell == "4":
                    print("Select an enemy hero to target (1,2,3)\n", UN2, "'s Hero List:\n", a, "\n", a[0], ":\n", v, "\n", a[1], ":\n", b, "\n", a[2], ":\n", n)
                    enemyTarget = input(": ")
                    while enemyTarget.isspace() or enemyTarget != "1" and enemyTarget != "2" and enemyTarget != "3" or enemyTarget.isspace():
                        enemyTarget = input("Please enter either [1/2/3]: ")
                    while v.CurrentHealth <= 0 and enemyTarget == "1":
                        enemyTarget = input("Please input other hero (choose hero with more than 0 health): ")
                    while b.CurrentHealth <= 0 and enemyTarget == "2":
                        enemyTarget = input("Please input other hero (choose hero with more than 0 health): ")
                    while n.CurrentHealth <= 0 and enemyTarget == "3":
                        enemyTarget = input("Please input other hero (choose hero with more than 0 heakth): ")
                    if enemyTarget == "1":
                        if not "Freeze" in v.Status:
                            v.Status += " Freeze"
                        Hero.Freeze(v, turn, HERO)
                        SPELL = "FREEZE"
                        WRITING_SPELL(GID, hero, a[0], SPELL)
                    if enemyTarget == "2":
                        if not "Freeze" in b.Status:
                            b.Status += " Freeze"
                        Hero.Freeze(b, turn, HERO)
                        SPELL = "FREEZE"
                        WRITING_SPELL(GID, hero, a[1], SPELL)
                    if enemyTarget == "3":
                        if not "Freeze" in n.Status:
                            n.Status += " Freeze"
                        Hero.Poison(n, turn, HERO)
                        SPELL = "FREEZE"
                        WRITING_SPELL(GID, hero, a[2], SPELL)
                if Spell == "5":
                    if Other1.CurrentHealth == 0 and Other2.CurrentHealth == 0:
                        if HERO == z:
                            print("Choose Hero to revive:\n1. ", m[1],":\n", Other1, m[2],":\n", Other2.replace("\n", ""))
                            Input = input(": ")
                            if Input == 1:
                                Hero.Revive(Other1)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other1, SPELL)
                                print ("REVIVED:\n", other1, ":\t", Other1)
                                input("enter to continue")
                            if Input == 2:
                                Hero.Revive(Other2)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other2, SPELL)
                                print ("REVIVED:\n", other2, ":\t", Other2)
                                input("enter to continue")
                        if HERO == x:
                            print("Choose Hero to revive:\n1. ", m[0],":\n", Other1, m[2],":\n", Other2.replace("\n", ""))
                            Input = input(": ")
                            if Input == 1:
                                Hero.Revive(Other1)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other1, SPELL)
                                print ("REVIVED:\n", other1, ":\t", Other1)
                                input("enter to continue")
                            if Input == 2:
                                Hero.Revive(Other2)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other2, SPELL)
                                print ("REVIVED:\n", other2, ":\t", Other2)
                                input("enter to continue")
                        if HERO == c:
                            print("Choose Hero to revive:\n1. ", m[0],":\n", Other1, m[1],":\n", Other2.replace("\n", ""))
                            Input = input(": ")
                            if Input == 1:
                                Hero.Revive(Other1)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other1, SPELL)
                                print ("REVIVED:\n",other1, ":\t", Other1)
                                input("enter to continue")
                            if Input == 2:
                                Hero.Revive(Other2)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other2, SPELL)
                                print ("REVIVED:\n", other2, ":\t", Other2)
                                input("enter to continue")
                    elif Other1.CurrentHealth == 0 and Other2.CurrentHeakth != 0:
                        Hero.Revive(Other1)
                        SPELL = "REVIVE"
                        WRITING_SPELL(GID, hero, other1, SPELL)
                        print ("REVIVED:\n", other1, ":\t", Other1)
                        input("enter to continue")
                    elif Other1.CurrentHealth != 0 and Other2.CurrentHealth == 0:
                        Hero.Revive(Other2)
                        SPELL = "REVIVE"
                        WRITING_SPELL(GID, hero, other2, SPELL)
                        print ("REVIVED:\n", other2, ":\t", Other2)
                        input("enter to continue")
########################################################################################################################################################################################
        if "warrior" in m[turnloop].lower():
            print()
            print("Available targets:\n","\n1.", a[0], ":\n", v, "\n2.", a[1], ":\n", b, "\n3.", a[2], ":\n", n) #, UN2, "'s Hero List:\n", a,
            attackTarget = input("Select a target: ")
            while attackTarget != "1" and attackTarget != "2" and attackTarget != "3" or attackTarget.isspace() or attackTarget == "":
                attackTarget = input("Please Select a tarrget [1, 2, 3] : ")
            while v.CurrentHealth <= 0 and attackTarget == "1":
                attackTarget = input("Please input other hero (choose hero with more than 0 health): ")
            while b.CurrentHealth <= 0 and attackTarget == "2":
                attackTarget = input("Please input other hero (choose hero with more than 0 health): ")
            while n.CurrentHealth <= 0 and attackTarget == "3":
                attackTarget = input("Please input other hero (choose hero with more than 0 heakth): ")
            if attackTarget == "1":
                ATTACK = HERO.attack()
                DAMAGE = v.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[0], ATTACK, v.Defense[v.lvl-1])
                print("####################")
                print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print(UN2, "'s Hero:\n", v)
                print("####################")
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[0], v.CurrentHealth, v.MaxHealth[v.lvl - 1], v.lvl, v.exp, v.Status)
            if attackTarget == "2":
                ATTACK = HERO.attack()
                DAMAGE = b.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[1], ATTACK, b.Defense[b.lvl-1])
                print("####################")
                print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print(UN2,"'s Hero:\n", b)
                print("####################")
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[1], b.CurrentHealth, b.MaxHealth[b.lvl - 1], b.lvl, b.exp, b.Status)
            if attackTarget == "3":
                ATTACK = HERO.attack()
                DAMAGE = n.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[2], ATTACK, n.Defense[n.lvl-1])
                print("####################")
                print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print(UN2, "'s Hero:\n", n)
                print("####################")
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[2], n.CurrentHealth, n.MaxHealth[n.lvl - 1], n.lvl, n.exp, n.Status)
######################################################################################################################################################################################
        if "tanker" in m[turnloop].lower():
            print("Available targets:\n","\n1.", a[0], ":\n", v, "\n2.", a[1], ":\n", b, "\n3.", a[2], ":\n", n) #, UN2, "'s Hero List:\n", a,
            attackTarget = input("Select a target: ")
            while attackTarget != "1" and attackTarget != "2" and attackTarget != "3" or attackTarget.isspace() or attackTarget == "":
                attackTarget = input("Please Select a tarrget [1, 2, 3] : ")
            while v.CurrentHealth <= 0 and attackTarget == "1":
                attackTarget = input("Please input other hero (choose hero with more than 0 health): ")
            while b.CurrentHealth <= 0 and attackTarget == "2":
                attackTarget = input("Please input other hero (choose hero with more than 0 health): ")
            while n.CurrentHealth <= 0 and attackTarget == "3":
                attackTarget = input("Please input other hero (choose hero with more than 0 heakth): ")
            if attackTarget == "1":
                ATTACK = HERO.attack()
                DAMAGE = v.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[0], ATTACK, v.Defense[v.lvl-1])
                print("####################")
                print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print(UN2, "'s Hero:\n", v)
                print("####################")
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[0], v.CurrentHealth, v.MaxHealth[v.lvl - 1], v.lvl, v.exp, v.Status)
            if attackTarget == "2":
                ATTACK = HERO.attack()
                DAMAGE = b.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[1], ATTACK, b.Defense[b.lvl-1])
                print("####################")
                print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print(UN2,"'s Hero:\n", b)
                print("####################")
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[1], b.CurrentHealth, b.MaxHealth[b.lvl - 1], b.lvl, b.exp, b.Status)
            if attackTarget == "3":
                ATTACK = HERO.attack()
                DAMAGE = n.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[2], ATTACK, n.Defense[n.lvl-1])
                print("####################")
                print("Your Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print(UN2, "'s Hero:\n", n)
                print("####################")
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[2], n.CurrentHealth, n.MaxHealth[n.lvl - 1], n.lvl, n.exp, n.Status)
    if HERO.CurrentHealth == 0:
        print("HERO Can't move (DEAD)")
        input("Press enter to continue")
    return gameID,z,x,c,v,b,n,m,a,UN1,UN2,turn
########################################################################################################################################################################################
########################################################################################################################################################################################
def battle_in_turn_com(z,x,c,v,b,n,m,a,gameID,UN1,UN2, turn, turnloop):
    if turnloop == 0:
        HERO = z
        Other1 = x
        Other2 = c
        hero = m[0]
        other1 = m[1]
        other2 = m[2]
    if turnloop == 1:
        HERO = x
        Other1 = z
        Other2 = c
        hero = m[1]
        other1 = m[0]
        other2 = m[2]
    if turnloop == 2:
        HERO = c
        Other1 = z
        Other2 = x
        hero = m[2]
        other1 = m[0]
        other2 = m[1]
    if HERO.CurrentHealth > 0:
        #print(HERO.FreezeTurn)
        print (m[turnloop],"HERO turn to move\nTHE HERO Status: ", HERO.Status)
        if "Poison" in HERO.Status:
            HERO.CurrentHealth -= HERO.PoisonDMG
            print(HERO.PoisonDMG,"DMG has been dealt to hero due to poison!!")
        if "Freeze" in HERO.Status and HERO.FreezeTurn == turn:
            HERO.Status = HERO.Status.replace("Freeze", "")
            HERO.FreezeTurn = 0
        elif "Freeze" in HERO.Status and HERO.FreezeTurn != turn:
            print("Hero was freeze")
            input("press enter to continue")
            return
        if "wizard" in m[turnloop].lower():    #if player slot is a wizard
            heroOption = random.randint(1,2)
            if heroOption == 1:
                attackTarget = random.randint(1,3)
                if attackTarget == 1:
                    ATTACK = HERO.attack()
                    DAMAGE = v.damage(ATTACK)
                    printAttack(gameID, m[turnloop], a[0], ATTACK, v.Defense[v.lvl-1])
                    print()
                    print(hero, " attack ", a[0])
                    print("####################")
                    print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                    print("____________________")
                    print("Your Hero:\n", v)
                    print("####################")
                    print()
                    printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                    printFile(gameID, a[0], v.CurrentHealth, v.MaxHealth[v.lvl - 1], v.lvl, v.exp, v.Status)
                    input("press 'enter' to continue")
                if attackTarget == 2:
                    ATTACK = HERO.attack()
                    DAMAGE = b.damage(ATTACK)
                    printAttack(gameID, m[turnloop], a[1], ATTACK, b.Defense[b.lvl-1])
                    print()
                    print(hero, " attack ", a[1])
                    print("####################")
                    print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                    print("____________________")
                    print("Your Hero:\n", b)
                    print("####################")
                    print()
                    printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                    printFile(gameID, a[1], b.CurrentHealth, b.MaxHealth[b.lvl - 1], b.lvl, b.exp, b.Status)
                    input("press 'enter' to continue")
                if attackTarget == 3:
                    ATTACK = HERO.attack()
                    DAMAGE = n.damage(ATTACK)
                    printAttack(gameID, m[turnloop], a[2], ATTACK, n.Defense[n.lvl-1])
                    print()
                    print(hero, " attack ", a[2])
                    print("####################")
                    print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                    print("____________________")
                    print("Your Hero:\n", n)
                    print("####################")
                    print()
                    printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                    printFile(gameID, a[2], n.CurrentHealth, n.MaxHealth[n.lvl - 1], n.lvl, n.exp, n.Status)
                    input("press 'enter' to continue")
            if heroOption == 2:
                if Other1.CurrentHealth == 0 or Other2.CurrentHealth == 0:
                    Spell = random.randint(1, 5)
                else:
                    Spell = random.randint(1, 4)
                if Spell == 1:
                    if Other1.CurrentHealth != Other1.MaxHealth and Other2.CurrentHealth == Other2.MaxHealth:
                        Hero.Heal(Other1, HERO)
                        SPELL = "HEAL"
                        WRITING_SPELL(GID, hero, other1, SPELL)
                        print("Health: ", Other1.CurrentHealth)
                        input("press enter to continue")
                    if Other1.CurrentHealth == Other1.MaxHealth and Other2.CurrentHealth != Other2.MaxHealth:
                        Hero.Heal(Other2, HERO)
                        SPELL = "HEAL"
                        WRITING_SPELL(GID, hero, other2, SPELL)
                        print("Health: ", Other2.CurrentHealth)
                        input("press enter to continue")
                    else:
                        Other1_HEALTH = Other1.MaxHealth[Other1.lvl - 1] - Other1.CurrentHealth
                        Other2_HEALTH = Other2.MaxHealth[Other2.lvl - 1] - Other2.CurrentHealth
                        if Other1_HEALTH > Other2_HEALTH:
                            Hero.Heal(Other1,HERO)
                            SPELL = "HEAL"
                            WRITING_SPELL(GID, hero, other1, SPELL)
                            print("Health: ", Other1.CurrentHealth)
                            input("press enter to continue")
                        if Other2_HEALTH > Other1_HEALTH:
                            Hero.Heal(Other2,HERO)
                            SPELL = "HEAL"
                            WRITING_SPELL(GID, hero, other2, SPELL)
                            print("Health: ", Other2.CurrentHealth)
                            input("press enter to continue")
                        else:
                            if  Other1.CurrentHealth <= 0 and Other2.CurrentHealth <= 0 and HERO.CurrentHealth > 0:
                                Hero.Heal(HERO, HERO)
                                SPELL = "HEAL"
                                WRITING_SPELL(GID, hero, hero, SPELL)
                                print("Current Health: ", HERO.CurrentHealth)
                                input("enter to continue")
                            else:
                                friendlyTarget = random.randint(1, 2, 3)
                                if friendlyTarget == 1 and Other1.CurrentHealth <= 0:
                                    friendlyTarget = random.randint(2,3)
                                if friendlyTarget == 2 and Otehr2.CurrentHealth <= 0:
                                    friendlyTarget = random.randint(1,3)
                                if  friendlyTarget == 1:
                                    Hero.Heal(Other1, HERO)
                                    SPELL = "HEAL"
                                    WRITING_SPELL(GID, hero, other1, SPELL)
                                    print("Current Health: ", Other1.CurrentHealth)
                                    input("enter to continue")
                                if friendlyTarget == 2:
                                    Hero.Heal(Other2, HERO)
                                    SPELL = "HEAL"
                                    WRITING_SPELL(GID, hero, other2, SPELL)
                                    print("Current Health: ", Other2.CurrentHealth)
                                    input("enter to continue")
                                if firendlyTarget == 3:
                                    Hero.Heal(HERO, HERO)
                                    SPELL = "HEAL"
                                    WRITING_SPELL(GID, hero, hero, SPELL)
                                    print("Current Health: ", HERO.CurrentHealth)
                                    input("enter to continue")
                if Spell == 2:
                    enemyTarget = random.randint(1,3)
                    if enemyTarget == "1":
                        if not "Poison" in v.Status:
                            v.Status += " Poison"
                        Hero.Poison(v, Hero.STATUS[HERO.lvl - 1], HERO)
                        SPELL = "POISON"
                        WRITING_SPELL(GID, hero, a[0], SPELL) 
                        print(a[0], "'s Status: ",v.Status)
                        input("press enter to continue")
                    if enemyTarget == "2":
                        if not "Poison" in b.Status:
                            b.Status += " Poison"
                        Hero.Poison(b, Hero.STATUS[HERO.lvl - 1], HERO)
                        SPELL = "POISON"
                        WRITING_SPELL(GID, hero, a[1], SPELL) 
                        print(a[1], "'s Status: ",b.Status)
                        input("press enter to continue")
                    if enemyTarget == "3":
                        if not "Poison" in n.Status:
                            n.Status += " Poison"
                        Hero.Poison(n, Hero.STATUS[HERO.lvl - 1], HERO)
                        SPELL = "POISON"
                        WRITING_SPELL(GID, HERO, n, SPELL) 
                        print(a[2], "'s Status: ",n.Status)
                        input("press enter to continue")
                if Spell == 3:
                    if"Poison" in Other1.Status and not "Poison" in Other2.Status and not "Poison" in HERO.Status:
                        Hero.Cure(Other1, HERO)
                        print(hero, " CURE ", other1)
                        SPELL = "CURE"
                        WRITING_SPELL(GID, hero, other1, SPELL)
                        input("press enter to continue")
                    if not "Poison" in Other1.Status and "Poison" in Other2.Status and not "Poison" in HERO.Status:
                        Hero.Cure(Other2, HERO)
                        print(hero, "CURE", other2)
                        SPELL = "CURE"
                        WRITING_SPELL(GID, hero, other1, SPELL)
                        input("press enter to continue")
                    if not "Poison" in Other1.Status and not "Poison" in Other2.Status and "Poison" in HERO.Status:
                        Hero.Cure(HERO, HERO)
                        print(hero, "CURE", hero)
                        SPELL = "CURE"
                        WRITING_SPELL(GID, hero, hero, SPELL)
                        input("press enter to continue")
                    if "Poison" in HERO.Status and "Poison" in Other1.Status and "Poison" in Other2.Status:
                        friendlyTarget = random.randint(1,3)
                        if friendlyTarget == 1:
                            Hero.Cure(Other1, HERO)
                            print(hero, "CURE", other1)
                            SPELL = "CURE"
                            WRITING_SPELL(GID, hero, other1, SPELL)
                            input("press enter to continue")
                        if friendlyTarget == 2:
                            Hero.Cure(Other2, HERO)
                            print(hero, "CURE", other2)
                            SPELL = "CURE"
                            WRITING_SPELL(GID, hero, other1, SPELL)
                            input("press enter to continue")
                        if firendlyTarget == 3:
                            Hero.Cure(HERO, HERO)
                            print(hero, "CURE", hero)
                            SPELL = "CURE"
                            WRITING_SPELL(GID, hero, hero, SPELL)   
                            input("press enter to continue")             
                if Spell == 4:
                    enemyTarget = random.randint(1,3)
                    if enemyTarget == 1:
                        if not "Freeze" in v.Status:
                            v.Status += " Freeze"
                        Hero.Freeze(v, turn, HERO)
                        SPELL = "FREEZE"
                        WRITING_SPELL(GID, hero, v, SPELL)
                        print(a[0], "Status: ", v.Status)
                        input("press enter to continue")
                    if enemyTarget == 2:
                        if not "Freeze" in b.Status:
                            b.Status += " Freeze"
                        Hero.Freeze(b, turn, HERO)
                        SPELL = "FREEZE"
                        WRITING_SPELL(GID, hero, b, SPELL)
                        print(a[1], "Status: ", b.Status)
                        input("press enter to continue")
                    if enemyTarget == 3:
                        if not "Freeze" in n.Status:
                            n.Status += " Freeze"
                        Hero.Poison(n, turn, HERO)
                        SPELL = "FREEZE"
                        WRITING_SPELL(GID, hero, n, SPELL)
                        print(a[2], "Status: ", n.Status)
                        input("press enter to continue")
                if Spell == 5:
                    if Other1.CurrentHealth == 0 and Other2.CurrentHealth == 0:
                        if HERO == z:
                            Input = random.randint(1,2)
                            if Input == 1:
                                Hero.Revive(Other1)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other1, SPELL)
                                print (other1, " REVIVED:\n", Other1)
                                input("Press enter to continue")
                            if Input == 2:
                                Hero.Revive(Other2)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other2, SPELL)
                                print (other2, " REVIVED:\n", Other2)
                                input("Press enter to continue")
                        if HERO == x:
                            Input = random.randint(1,2)
                            if Input == 1:
                                Hero.Revive(Other1)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, Other1, SPELL)
                                print (other1, " REVIVED:\n", Other1)
                                input("Press enter to continue")
                            if Input == 2:
                                Hero.Revive(Other2)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, Other2, SPELL)
                                print (other2, " REVIVED:\n", Other2)
                                input("Press enter to continue")
                        if HERO == c:
                            Input = random.randint(1,2)
                            if Input == 1:
                                Hero.Revive(Other1)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other1, SPELL)
                                print (other1, " REVIVED:\n", Other1)
                                input("Press enter to continue")
                            if Input == 2:
                                Hero.Revive(Other2)
                                SPELL = "REVIVE"
                                WRITING_SPELL(GID, hero, other2, SPELL)
                                print (other2, " REVIVED:\n", Other2)
                                input("Press enter to continue")
                    elif Other1.CurrentHealth == 0 and Other2.CurrentHeakth != 0:
                        Hero.Revive(Other1)
                        SPELL = "REVIVE"
                        WRITING_SPELL(GID, hero, other1, SPELL)
                        print (other1, " REVIVED:\n", Other1)
                        input("Press enter to continue")
                    elif Other1.CurrentHealth != 0 and Other2.CurrentHealth == 0:
                        Hero.Revive(Other2)
                        SPELL = "REVIVE"
                        WRITING_SPELL(GID, hero, other2, SPELL)
                        print (other2, " REVIVED:\n", Other2)
                        input("Press enter to continue")
#########################################################################################################################################################################################
        if "warrior" in m[turnloop].lower():
            attackTarget = random.randint(1,3)
            if attackTarget == 1:
                ATTACK = HERO.attack()
                DAMAGE = v.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[0], ATTACK, v.Defense[v.lvl-1])
                print()
                print(hero, " attack ", a[0])
                print("####################")
                print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print("Your Hero:\n", v)
                print("####################")
                print()
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[0], v.CurrentHealth, v.MaxHealth[v.lvl - 1], v.lvl, v.exp, v.Status)
                input("Press enter to continue")
            if attackTarget == 2:
                ATTACK = HERO.attack()
                DAMAGE = b.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[1], ATTACK, b.Defense[b.lvl-1])
                print()
                print(hero, " attack ", a[1])
                print("####################")
                print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print("Your Hero:\n", b)
                print("####################")
                print()
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[1], b.CurrentHealth, b.MaxHealth[b.lvl - 1], b.lvl, b.exp, b.Status)
                input("Press enter to continue")
            if attackTarget == 3:
                ATTACK = HERO.attack()
                DAMAGE = n.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[2], ATTACK, n.Defense[n.lvl-1])
                print()
                print(hero, " attack ", a[2])
                print("####################")
                print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print("Your Hero:\n", n)
                print("####################")
                print()
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[2], n.CurrentHealth, n.MaxHealth[n.lvl - 1], n.lvl, n.exp, n.Status)
                input("Press enter to continue")
########################################################################################################################################################################################
        if "tanker" in m[turnloop].lower():
            attackTarget = random.randint(1,3)
            if attackTarget == 1:
                ATTACK = HERO.attack()
                DAMAGE = v.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[0], ATTACK, v.Defense[v.lvl-1])
                print()
                print(hero, " attack ", a[0])
                print("####################")
                print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print("Your Hero:\n", v)
                print("####################")
                print()
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[0], v.CurrentHealth, v.MaxHealth[v.lvl - 1], v.lvl, v.exp, v.Status)
                input("Press enter to continue")
            if attackTarget == 2:
                ATTACK = HERO.attack()
                DAMAGE = b.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[1], ATTACK, b.Defense[b.lvl-1])
                print()
                print(hero, " attack ", a[1])
                print("####################")
                print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print("Your Hero:\n", b)
                print("####################")
                print()
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[1], b.CurrentHealth, b.MaxHealth[b.lvl - 1], b.lvl, b.exp, b.Status)
                input("Press enter to continue")
            if attackTarget == 3:
                ATTACK = HERO.attack()
                DAMAGE = n.damage(ATTACK)
                printAttack(gameID, m[turnloop], a[2], ATTACK, n.Defense[n.lvl-1])
                print()
                print(hero, " attack ", a[0])
                print("####################")
                print(UN1, "'s Hero:\n", HERO,"Damage: ", DAMAGE)
                print("____________________")
                print("Your Hero:\n", n)
                print("####################")
                print()
                printFile(gameID, m[turnloop], HERO.CurrentHealth, HERO.MaxHealth[HERO.lvl - 1], HERO.lvl, HERO.exp, HERO.Status)
                printFile(gameID, a[2], n.CurrentHealth, n.MaxHealth[n.lvl - 1], n.lvl, n.exp, n.Status)
                input("Press enter to continue")
    if HERO.CurrentHealth == 0:
        print("HERO Can't move (DEAD)")
        input("Press enter to continue")
    return gameID,z,x,c,v,b,n,m,a,UN1,UN2,turn
#############################################################################################################
###### GIO, ALBERT, LIU
######### INI KURANG WRITE INFILE HABIS CAST SKILL, DEAL SPELL EFFECT
######### KALIAN TINGGAL TAMBAH ATTACK DI WARRIOR IKUTIN CARA AKU TULIS ATTACK DI BAGIAN WIZZARD UTK TANK SAMA WARRIOR
########## ALBERT: WHAT?
