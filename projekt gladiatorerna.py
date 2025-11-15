import random
from colorama import Style, Fore, Back 
import os
#from playsound3 import playsound   

#---------------------------------------VARIABLER-----------------------------------------#

antal_kämpade_strider = 0
antal_guldmynt = 0

rank_nummer = 1  #rank 1 = tiggare, rank 2 = legosoldat, rank 3 = glaidator
rank_namn = "tiggare" #Start rank#

ingen_rustning = True
läderrustning = False
järnrustning = False

drako_hp = 26
maximus_hp =34
dominous_aurelius_valcar_hp = 50

besegrad_drako = False
besegrad_maximus = False
besegrad_dominous = False


spelarens_attacker = ["näve", "spark"]
motståndarens_attacker = ["näve", "spark"]


rustning = ["1", "läder", "läderrustning", "2", "järn", "järnrustning", "3", "kortsvärd", "4", "kniv", "5", "stridssvärd", "6", "falx", "0", "nej"] #läder = 32hp, järn = 48hp


#-----------------------------------------------------------------------------------------#


#----------------------------------------------INTRO-------------------------------------------#

print(f"===========\n{Fore.RED}GLADIATORER{Style.RESET_ALL}\n===========")

print("Välkommen till spelet gladiatorer!")
spelarens_namn = input("Ange din gladiators namn: ").capitalize()

groteskt_val = input("Vill du ha blodiga beskrivningar under striden? (ja/nej): ").lower()

if groteskt_val == "ja":
    groteskt = True
    print("\nDu har valt en blodig strid!")
elif groteskt_val == "nej":
    groteskt = False
    print("\nDu har valt en vanlig strid.")
else:
    groteskt_val = input("Skriv rätt val (ja/nej).").lower()
    if groteskt_val == "ja":
        groteskt = True
        print("\nDu har valt en blodig strid!")
    elif groteskt_val == "nej":
        groteskt = False
        print("\nDu har valt en vanlig strid.")
    else:
        print("FEL INPUT!\n" \
        "SPELET AVSLUTAS.")
        exit()

input("\nTryck enter för att fortsätta.\n")



#------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------FUNKTIONER----------------------------------------------------------#

def visa_hp():
    print(f"Din hp är {Fore.BLUE}{spelarens_hp}.{Style.RESET_ALL}")
    print(f"Fiendens hp är {Fore.RED}{motståndarens_hp}.{Style.RESET_ALL}")

def drako_val_av_attack(): # I funktionen väljer drako fram slumpmässigt en attack
    return random.choice(motståndarens_attacker)

def maximus_val_av_attack(): # Här väljer maxmimus fram en attack baserad på spelarens och sin hp.
    if spelarens_hp < 7 and ingen_rustning == True:
        return "kortsvärd"
    elif spelarens_hp < 6 and läderrustning == True:
        return "kortsvärd"
    elif spelarens_hp < 5.5 and järnrustning == True:
        return "kortsvärd"
    elif motståndarens_hp < 10 and läderrustning == True:
        return random.choice(["kortsvärd", "kortsvärd", "kortsvärd", "spark", "spark", "näve"])
    elif motståndarens_hp < 10 and järnrustning == True:
        return random.choice(["kortsvärd", "kortsvärd", "kortsvärd", "kortsvärd", "näve", "näve"])
    elif läderrustning == True or ingen_rustning == True:
        return random.choice(motståndarens_attacker)
    elif järnrustning == True:
        return random.choice(["näve", "näve", "kortsvärd", "kortsvärd", "kortsvärd"])
    

    #EJ FÄRDIG ÄN
def dominous_aurelius_valcar_val_av_attack():
    if spelarens_hp <= 8 and ingen_rustning == True:
        return "morgonstjärna"
    elif spelarens_hp <= 7.5 and läderrustning == True:
        return "morgonstjärna"
    elif spelarens_hp <= 6.5 and järnrustning == True:
        return "morgonstjärna"
    elif motståndarens_hp < 10 and spelarens_hp > motståndarens_hp and (ingen_rustning == True or läderrustning == True):
        return random.choice(["morgonstjärna", "morgonstjärna", "morgonstjärna", "morgonstjärna","näve", "näve", "spark"])
    elif motståndarens_hp < 10 and spelarens_hp > motståndarens_hp and järnrustning == True:
        return random.choice(["morgonstjärna", "morgonstjärna", "morgonstjärna", "morgonstjärna", "näve", "näve"])
    elif järnrustning == True:
        return random.choice(["morgonstjärna", "morgonstjärna", "morgonstjärna", "näve", ])
    elif läderrustning == True or ingen_rustning == True:
        return random.choice(["morgonstjärna", "morgonstjärna", "morgonstjärna", "näve", "spark"])

    ######################
    
#Funktionen nedan rensar kärmet.#
def rensa_skärm():              
    os.system("cls")            
#################################


def träffchans_näve():
     return random.choice(["träff","träff","miss"])

def träffchans_spark():
    return random.choice(["träff","träff","träff","träff","miss"])
   
def träffchans_yxa():   
    return random.choice(["träff","träff","träff","miss"])
    
def träffchans_kniv():   
    return random.choice(["träff","träff","träff","miss","miss"])
    
def träffchans_klubba():    
    return random.choice(["träff","träff","träff","miss"])
 
def träffchans_kortsvärd():
    if val_av_motståndare == "Drako":    
        return "träff"
    else: 
        return random.choice(["träff", "träff", "träff", "träff", "träff", "träff", "träff", "träff", "miss", "miss"])

def träffchans_morgonstjärna():
    return random.choice(["träff", "träff", "träff", "träff", "träff", "träff", "träff", "träff", "träff", "miss", "miss", "miss"])

def träffchans_stridssvärd():
    return random.choice(["träff", "träff", "träff", "träff", "träff", "träff", "träff", "miss", "miss", "miss"])

def träffchans_flax():
    return random.choice(["träff", "träff", "träff", "träff", "träff", "träff", "träff", "träff", "miss", "miss", "miss"])


#---#FUNKTIONEN NEDAN HANTERAR ALLA ATTACKER, SKADA OCH SKRIVER UT OM SPELAREN HAR VUNNIT ELLER INTE#---#

def träffskada(spelarens_attack):
    global rank_nummer
    global rank_namn
    global spelarens_hp
    global motståndarens_hp
    global besegrad_drako
    global besegrad_maximus
    global besegrad_dominous
    global antal_kämpade_strider
    global antal_guldmynt

    if val_av_motståndare == "Drako" or val_av_motståndare == "1":
        motståndarens_attack = drako_val_av_attack()
    elif val_av_motståndare == "Maximus" or val_av_motståndare == "2":
        motståndarens_attack = maximus_val_av_attack()
    elif val_av_motståndare == "Dominous" or val_av_motståndare == "3":
        motståndarens_attack = dominous_aurelius_valcar_val_av_attack()

    spelarens_träffchans_näve = träffchans_näve()
    spelarens_träffchans_spark = träffchans_spark()
    spelarens_träffchans_yxa = träffchans_yxa()
    spelarens_träffchans_kniv = träffchans_kniv()
    spelarens_träffchans_klubba = träffchans_klubba()
    spelarens_träffchans_kortsvärd = träffchans_kortsvärd()
    spelarens_träffchans_stridssvärd = träffchans_stridssvärd()
    spelarens_träffchans_flax = träffchans_flax()

    motståndarens_träffchans_näve = träffchans_näve()
    motståndarens_träffchans_spark = träffchans_spark()
    motståndarens_träffchans_yxa = träffchans_yxa()
    motståndarens_träffchans_kniv = träffchans_kniv()
    motståndarens_träffchans_klubba = träffchans_klubba()
    motståndarens_träffchans_kortsvärd = träffchans_kortsvärd()
    motståndarens_träffchans_morgonstjärna = träffchans_morgonstjärna()


    if spelarens_attack == "näve" and spelarens_träffchans_näve == "träff":
        if groteskt == False:
            print(f"\nDin näve träffar {val_av_motståndare} i magen.")
        elif groteskt == True:
            print(f"\nDin järnhård näve träffar {val_av_motståndare} så hårt i magen att han börjar spitta blod.")
        if val_av_motståndare == "Drako":
            motståndarens_hp -= random.randint(2,3)
        elif val_av_motståndare == "Maximus":
            motståndarens_hp -= random.randint(1,2)
        elif val_av_motståndare == "Dominous":
            motståndarens_hp -= random.randint(0,1)
    elif spelarens_attack == "näve" and spelarens_träffchans_näve == "miss":
        print("Du missar.")  

    elif spelarens_attack == "spark" and spelarens_träffchans_spark == "träff":
        if groteskt == False:
            print(f"\nDin spark träffar {val_av_motståndare}.")
        elif groteskt == True:
            print(f"\nDin kraftfull spark träffar {val_av_motståndare} i sidan av magen och han tappade nästan ballansen. ")
        if val_av_motståndare == "Drako":
            motståndarens_hp -= random.randint(1,2)
        elif val_av_motståndare == "Maximus":
            motståndarens_hp -= random.randint(0,1)
        elif val_av_motståndare == "Dominous":
            motståndarens_hp -= 0
    elif spelarens_attack == "spark" and spelarens_träffchans_spark == "miss":
        print("Du missar.")     

    elif spelarens_attack == "yxa" and spelarens_träffchans_yxa == "träff":
        if groteskt == False:
            print(f"\nDu träffar {val_av_motståndare} med yxan.")
        elif groteskt == True:
            print(f"\nDu träffar {val_av_motståndare} i axeln och sanden blir fylld av blod.")
        if val_av_motståndare == "Drako":
            motståndarens_hp -= 5
        elif val_av_motståndare == "Maximus":
            motståndarens_hp -= 4
        elif val_av_motståndare == "Dominous":
            motståndarens_hp -= 3
    elif spelarens_attack == "yxa" and spelarens_träffchans_yxa == "miss":
        print("Du missar.") 

    elif spelarens_attack == "kniv" and spelarens_träffchans_kniv == "träff":
        if groteskt == False:
            print(f"\nDu träffar {val_av_motståndare} med knivet.")
        elif groteskt == True:
            if val_av_motståndare == "Dominous" and (motståndarens_hp - spelarens_hp) > 14:
                print("Du hugger Dominous rakt i magen men han tar ut kniven som om ingenting hänt.")
            elif val_av_motståndare == "Dominous":
                print("Du hugger Dominous rakt i magen och han stirrar på dig med lömsk blick")
            else:
                print(f"\nDu hugger {val_av_motståndare} rakt i magen medan han skriker av smärta.")
        if val_av_motståndare == "Drako":
            motståndarens_hp -= 4
        elif val_av_motståndare == "Maximus":
            motståndarens_hp -= 3
        elif val_av_motståndare == "Dominous":
            motståndarens_hp -= 2
    elif spelarens_attack == "kniv" and spelarens_träffchans_kniv == "miss":
        print("Du missar.") 

    elif spelarens_attack == "klubba" and spelarens_träffchans_klubba == "träff":
        if groteskt == False:
            print(f"\nDu träffar {val_av_motståndare} i huvudet med klubban.")
        elif groteskt == True:
            print(f"\nDu träffar {val_av_motståndare} rakt i huvudet med klubban.")
        if val_av_motståndare == "Drako":
            motståndarens_hp -= 3
        elif val_av_motståndare == "Maximus":
            motståndarens_hp -= 2
        elif val_av_motståndare == "Dominous":
            motståndarens_hp -= 1
    elif spelarens_attack == "klubba" and spelarens_träffchans_klubba == "miss":
        print("Du missar.") 

    elif spelarens_attack == "kortsvärd" and spelarens_träffchans_kortsvärd == "träff":
        if groteskt == False:
            print(f"\nDu träffar {val_av_motståndare} med kortsvärdet.")
        elif groteskt == True:
            if motståndarens_hp < 7 and val_av_motståndare == "Drako":
                print(f"\nDu huggar av {val_av_motståndare}'s huvud och sanden blir rött fylld av blod.")
            elif motståndarens_hp < 6 and val_av_motståndare == "Maximus":
                print(f"\nDu huggar av {val_av_motståndare}'s huvud och sanden blir rött fylld av blod.")
            elif motståndarens_hp < 5 and val_av_motståndare == "Dominous":
                print(f"\nDu huggar av {val_av_motståndare}'s huvud och sanden blir rött fylld av blod.")   
            else:
                if val_av_motståndare == "Dominous":
                    print(random.choice(["Ditt kortsvärd genomborrar Dominous rustning och träffar honom i sidan av magen", "Ditt svärd genomborrar Dominous rustning och träffar honom."]))
                else:
                    print(f"\nDu träffar {val_av_motståndare} rakt i magen och blodet rinner snabbt från såret.")
        if val_av_motståndare == "Drako":
            motståndarens_hp -= random.randint(6,7)
        elif val_av_motståndare == "Maximus":
            motståndarens_hp -= random.randint(5,6)
        elif val_av_motståndare == "Dominous":
            motståndarens_hp -= random.randint(4,5)

        if val_av_motståndare == "Drako":
            spelarens_attacker.remove("kortsvärd")
    elif spelarens_attack == "kortsvärd" and spelarens_träffchans_kortsvärd == "miss":
        print("Du missar.")

    if spelarens_attack == "striddsvärd" and spelarens_träffchans_stridssvärd == "träff":
        if groteskt == False:
            print(f"Du huggar {val_av_motståndare} med stridssvärdet.")
        elif groteskt == True:
            if val_av_motståndare == "Dominous" and motståndarens_hp < 6:
                print(random.choice(["Ditt striddsvärd genomborrar Dominous's rustning och du träffar honom rakt i magen. Han skrek av smärtan", "Du huggar av Dominous's huvud och sanden blir rött fylld av blod."]))
            else:
                if val_av_motståndare == "Dominous" and groteskt == True:
                    print(random.choice(["Ditt stridssvärd genomborrar Dominous's rustning och träffar honom i sidan av magen.", "Ditt stridssvärd genomborrar Dominous's rustning och träffar honom vid axeln, blod rinner snabbt från hans axel."]))
            if val_av_motståndare == "Dominous": #Jag har bara subtraherat Dominous hp eftersom vapnet går endast och köpa på rank 3, och då har man besegrat alla andra.
                motståndarens_hp -= random.randint([5,6])
    elif spelarens_attack == "stridssvärd" and träffchans_stridssvärd == "miss":
        print("Du missar.")
                                                                            ####  Attack beskrivningen för falx och striddsvärd kan förbättras #### ## fortsätta senare ##
    if spelarens_attack == "falx" and träffchans_flax == "träff":
        if groteskt == False:
            print(f"Du huggar {val_av_motståndare} med falxet.")
        elif groteskt == True:
            print(f"Du hugger {val_av_motståndare} med falxet och blod rinner. {val_av_motståndare} stirrar på dig med lömsk blick.")
        if val_av_motståndare == "Dominous": #Jag har bara subtraherat Dominous hp eftersom vapnet går endast och köpa på rank 3, och då har man besegrat alla andra.
            motståndarens_hp -= 3
    elif spelarens_attack == "falx" and spelarens_träffchans_flax == "miss":
        print("Du missar.")


    if motståndarens_hp < 1: 
        print(f"{val_av_motståndare} faller till marken.")
        print("╔══════════════════════════╗\n"
              "║  ⚔️  D U   V A N N  ⚔️  ║\n" 
              "╚══════════════════════════╝\n")
        if val_av_motståndare == "Drako":
            besegrad_drako = True 
            rank_nummer = 2
            rank_namn = "Legosoldat"
            print("\nGrattis, du har blivit befordrad till rank 2: Legosoldat\n")
        elif val_av_motståndare == "Maximus":
            besegrad_maximus = True
            rank_namn = 3
            rank_namn = "Gladiator"
            print("Grattis, du har blivit befordrad till rank 3: Gladiator")
        elif val_av_motståndare == "Dominous":
            besegrad_dominous = True
            #-----Nedan får spelaren guldmynt-----# 
        if val_av_motståndare == "Drako" and (spelarens_hp - motståndarens_hp) > 9:
            print("\nDu fick 18 guldmynt från publiken eftersom alla var riktigt nöjda med din presterande.")
            antal_guldmynt += 18
        elif val_av_motståndare == "Drako" and (spelarens_hp - motståndarens_hp) > 4:
            print("\nDu fick 15 guldmynt från publiken.")
            antal_guldmynt += 15
        elif val_av_motståndare == "Drako":
            print("\nDu fick 10 guldmynt från publiken.")
            antal_guldmynt += 10
        elif val_av_motståndare == "Maximus" and (spelarens_hp - motståndarens_hp) > 9:
            print("\nDu fick 20 guldmynt från kungen och 10 från publiken eftersom alla var riktigt nöjda med din presterande.")
            antal_guldmynt += 30
        elif val_av_motståndare == "Maximus" and (spelarens_hp - motståndarens_hp) > 4:
            print("Du fick 17 guldmynt från kungen och 8 från publiken.")
            antal_guldmynt += 25
        elif val_av_motståndare == "Maximus":
            print("Du fick 15 guldmynt från kungen.")
            antal_guldmynt += 15
        elif val_av_motståndare == "Dominous" and (spelarens_hp - motståndarens_hp) > 9:
            print("Du fick 50 guldmynt från kungen och 15 från publiken")
            antal_guldmynt += 65
        elif val_av_motståndare == "Dominous" and (spelarens_hp - motståndarens_hp) > 4:
            print("Du fick 45 guldmynt från kungen och 10 från publiken.")
            antal_guldmynt += 55
        elif val_av_motståndare == "Dominous":
            print("Du fick 50 guldmynt från kungen.")
            antal_guldmynt += 50

        antal_kämpade_strider += 1
        input("Tryck enter för att fortsätta.")
        return


    if motståndarens_attack == "näve" and motståndarens_träffchans_näve == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i magen.")
        elif groteskt == True:
            print(f"{val_av_motståndare} träffar dig rakt i magen och du börjar att spitta blod.")
        if ingen_rustning == True:
            spelarens_hp -= random.randint(2,3)
        elif läderrustning == True:
            spelarens_hp -= random.choice([1.5, 2.5])
        elif järnrustning == True:
            spelarens_hp -= random.choice([0.5, 1.5])
    elif motståndarens_attack == "näve" and motståndarens_träffchans_näve == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "spark" and motståndarens_träffchans_spark == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i benet.")
        elif groteskt == True:
            print(f"{val_av_motståndare} träffar dig rakt i magen och du skrek av smärtan.")
        if ingen_rustning == True:
            spelarens_hp -= random.randint(1,2)
        elif läderrustning == True:
            spelarens_hp -= random.choice([0.5, 1.5])
        elif järnrustning == True:
            spelarens_hp -= random.choice([0, 0.5])
    elif motståndarens_attack == "spark" and motståndarens_träffchans_spark == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "yxa" and motståndarens_träffchans_yxa == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i axeln med en yxa.")
        elif groteskt == True:
            print(f"{val_av_motståndare} träffar dig vid axeln och blodet rinner snabbt från såret.")
        if ingen_rustning == True:
            spelarens_hp -= 5
        elif läderrustning == True:
            spelarens_hp -= 4.5
        elif järnrustning == True:
            spelarens_hp -= 3.5
    elif motståndarens_attack == "yxa" and motståndarens_träffchans_yxa == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "kniv" and motståndarens_träffchans_kniv == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i magen med en kniv.")
        elif groteskt == True:
            print(f"{val_av_motståndare} huggar dig i magen och blod börjar rinna väldigt snabbt från såret.")
        if ingen_rustning == True:
            spelarens_hp -= 4
        elif läderrustning == True:
            spelarens_hp -= 3.5
        elif järnrustning == True:
            spelarens_hp -= 2.5
    elif motståndarens_attack == "kniv" and motståndarens_träffchans_kniv == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "klubba" and motståndarens_träffchans_klubba == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i huvudet med en klubba.")
        elif groteskt == True:
            print(f"{val_av_motståndare} träffar dig rakt i ansiktet med klubban.")
        if ingen_rustning == True:
            spelarens_hp -= 3
        elif läderrustning == True:
            spelarens_hp -= 2.5
        elif järnrustning == True:
            spelarens_hp -= 1.5
    elif motståndarens_attack == "klubba" and motståndarens_träffchans_klubba == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "kortsvärd" and motståndarens_träffchans_kortsvärd == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig.")
        elif groteskt == True:
            if spelarens_hp > 7:
                print(f"{val_av_motståndare} huggar dig i magen.")
            elif  spelarens_hp < 7:
                print(f"{val_av_motståndare} huggar av din huvud och sanden blir rött fylld av blod.")
            else:
                print(f"{val_av_motståndare} träffar dig rakt i magen och blodet rinner snabbt från såret.")
        if ingen_rustning == True:
            spelarens_hp -= random.randint(6,7)
        elif läderrustning == True:
            spelarens_hp -= random.choice([5.5, 6.5])
        elif järnrustning == True:
            spelarens_hp -= random.choice([4.5, 5.5])
        if val_av_motståndare == "Drako":
            motståndarens_attacker.remove("kortsvärd")
    elif motståndarens_attack == "kortsvärd" and motståndarens_träffchans_kortsvärd == "miss":
        print(f"{val_av_motståndare} missar.")
        
    elif motståndarens_attack == "morgonstjärna" and träffchans_morgonstjärna == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig med morgonstjärnan.")
        elif groteskt == True:
            if spelarens_hp < 8 and  ingen_rustning == True:
                print(f"{val_av_motståndare} svingar morgonstjärnan och träffar dig riktigt hårt i ansiktet vilket gör att din käke flyger iväg.")
            elif spelarens_hp < 7.5 and läderrustning == True:
                print(f"{val_av_motståndare} svingar morgonstjärnan och träffar dig riktigt hårt i ansiktet vilket gör att din käke flyger iväg.")
            elif spelarens_hp < 6.5 and järnrustning == True:
                print(f"{val_av_motståndare} svingar morgonstjärnan och träffar dig riktigt hårt i ansiktet vilket gör att din käke flyger iväg.")
            elif spelarens_hp > 10 and (läderrustning == True or ingen_rustning == True):
                print(f"{val_av_motståndare} träffar dig i bröstet med morgonstjärnan vilket får blod att stänka överallt.")
            else: 
                print("Morgonstjärnan träffar dig riktigt hårt i ansiktet vilket gör att du börjar att spitta blod.")
        if ingen_rustning == True:
            spelarens_hp -= 8
        elif läderrustning == True:
            spelarens_hp -= 7.5
        elif järnrustning == True:
            spelarens_hp -= 6.5
    elif motståndarens_attack == "morgonstjärna" and träffchans_morgonstjärna == "miss":
        print(f"{val_av_motståndare} missar.")

    if spelarens_hp < 1:
        print("Du faller til marken.")
        print("╔══════════════════════════════════╗\n"
              "║  ☠️       D U   D Ö R       ☠️  ║\n"
              "╚══════════════════════════════════╝\n")
        exit()

###--------------------Nedan ligger funktuionen till smeden--------------------###
def smeden():
    global vill_gå_till_smeden
    global handel_med_smeden
    global antal_guldmynt
    global spelarens_hp
    global spelarens_attacker
    global ingen_rustning
    global läderrustning
    global järnrustning

    while True:                           
        vill_köpa_eller_sälja = input("Vill du köpa eller sälja något? ").lower()
        if vill_köpa_eller_sälja in ["köpa", "sälja"]:
            break
        else: 
            print("Fel input!\n")
    if vill_köpa_eller_sälja == "köpa":
        rensa_skärm()
        print("Hos smeden John finns följande rustningar och vapen.")
        print("1. Läderrustning: -0.5 skada och totala hp'n ökar till 32. Kostar 5 guldmynt. (erforderlig rank >= 2: Legosoldat)\n"
            "2. Järnrustning: -1.5 skada och totala hp'n ökar till 48. Kostar 10 guldmynt. (erforderlig rank = 3: Gladiator)")
        print("3. Kortsvärd: Gör 6-7 skada och har träffchansen 8 av 10. Kostar 7 guldmynt. (erforderlig rank >= 2: Legosoldat)\n" \
        "4. Kniv: Gör 4 skada och har träffchansen 3 av 5. Kostar 3 guldmynt. (erforderlig rank >= 2: Legosoldat)\n" \
        "5. Stridssvärd: Gör 7-8 skada och har träffchansen 7 av 10. Kostar 9 guldmynt. (erforderlig rank = 3: Gladiator) \n" \
        "6. Falx: En lång böjd kniv. Gör 5 skada och har träffchansen 8 av 11. Kostar 4 guldmynt. (erforderlig rank = 3: Gladiator)")
        print(f"Just nu har du {antal_guldmynt} guldmynt.")
        while True:
            val_av_rustning_eller_vapen = input("Här kan du skriva ditt val av rustning/vapen, om du vill köpa ingenting kan du skriva nej eller 0: ").lower()
            if val_av_rustning_eller_vapen in rustning and (val_av_rustning_eller_vapen != "nej" and val_av_rustning_eller_vapen != "0"):
                #läderrustning
                if val_av_rustning_eller_vapen in ["läderrustning", "läder", "1"] and ingen_rustning == True and järnrustning == False  and läderrustning == False and antal_guldmynt >= 5:
                    print("Du valde att köpa ett par läderrustning.\n")
                    ingen_rustning = False
                    läderrustning = True
                    järnrustning = False
                    spelarens_hp = 32 
                    antal_guldmynt -= 5
                    break
                elif val_av_rustning_eller_vapen in ["läderrustning", "läder", "1"] and (järnrustning == True or läderrustning == True) and antal_guldmynt >= 5:
                    print("Du har redan rustning.")
                    print("För att köpa en annan rustning måste du först sälja din nuvarande rustning.\n")
                    break
                elif val_av_rustning_eller_vapen in ["läderrustning", "läder", "1"] and ingen_rustning == True and järnrustning == False  and läderrustning == False and antal_guldmynt < 5:
                    print("Du har tyvärr inte tillräckligt med guldmynt.\n")
                    break
                #------------------------läderrustning-------------------#
                #järnrustning
                elif val_av_rustning_eller_vapen in ["järnrustning", "järn", "2"] and ingen_rustning == True and läderrustning == False and järnrustning == False and antal_guldmynt >= 10:
                    print("Du valde att köpa ett par järnrustning.\n")
                    ingen_rustning = False
                    läderrustning = False
                    järnrustning = True
                    spelarens_hp = 48
                    antal_guldmynt -= 10
                    break
                elif val_av_rustning_eller_vapen in ["järnrustning", "järn", "2"] and ingen_rustning == False and (läderrustning == True or järnrustning == True) and antal_guldmynt >= 10:
                    print("Du har redan rustning.")
                    print("För att köpa en annan rustning måste du först sälja din nuvarande rustning.\n")
                    break
                elif val_av_rustning_eller_vapen in ["järnrustning", "järn", "2"] and ingen_rustning == True and läderrustning == False and järnrustning == False and antal_guldmynt < 10: 
                    print("Du har tyvärr inte tillräckligt med guldmynt.\n")
                    break
                #---------------------------järnrustning--------------------------#
                #kortsvärd
                elif val_av_rustning_eller_vapen in ["kortsvärd", "3"] and len(spelarens_attacker) < 4 and antal_guldmynt >= 7:
                    print("Du valde att köpa en kortsvärd.\n")
                    spelarens_attacker.append("kortsvärd")
                    antal_guldmynt -= 7
                    break
                elif val_av_rustning_eller_vapen in ["kortsvärd", "3"] and len(spelarens_attacker) >= 4 and antal_guldmynt >= 7:
                    print("Du måste sälja en av dina vapen, eftersom du kan inte bära mer än två vapen.\n")
                    break
                elif val_av_rustning_eller_vapen in ["kortsvärd", "3"] and len(spelarens_attacker) > 4 and antal_guldmynt < 7:
                    print("Du har tyvärr inte tillräckligt med guldmynt.\n")
                    break
                #---------------------kortsvärd--------------------#
                #kniv
                elif val_av_rustning_eller_vapen in ["kniv", "4"] and len(spelarens_attacker) < 4 and antal_guldmynt >= 3:
                    print("Du valde att köpa en kniv")
                    spelarens_attacker.append("kniv")
                    antal_guldmynt -= 3
                    break
                elif val_av_rustning_eller_vapen in ["kniv", "4"] and len(spelarens_attacker) >= 4 and antal_guldmynt >= 3:
                    print("Du måste sälja en av dina vapen, eftersom du kan inte bära mer än två vapen.\n")
                    break
                elif val_av_rustning_eller_vapen in ["kniv", "4"] and len(spelarens_attacker) < 4 and antal_guldmynt < 3:
                    print("Du har tyvärr inte tillräckligt med guldmynt.\n")
                    break
                #--------------------kniv------------------------------#
                #stridssvärd
                elif val_av_rustning_eller_vapen in ["stridssvärd", "5"] and len(spelarens_attacker) < 4 and antal_guldmynt >= 9:
                    print("Du valde att köpa en stridssvärd.\n")
                    spelarens_attacker.append("stridssvärd")
                    antal_guldmynt -= 9
                    break
                elif val_av_rustning_eller_vapen in ["stridssvärd", "5"] and len(spelarens_attacker) >= 4 and antal_guldmynt >= 9:
                    print("Du måste sälja en av dina vapen, eftersom du kan inte bära mer än två vapen.\n")
                    break
                elif val_av_rustning_eller_vapen in ["stridssvärd", "5"] and len(spelarens_attacker) < 4 and antal_guldmynt < 9:
                    print("Du har tyvärr inte tillräckligt med guldmynt.")
                    break

                #-----------------stridssvärd-----------------#
                #falx
                elif val_av_rustning_eller_vapen in ["falx", "6"] and len(spelarens_attacker) < 4 and antal_guldmynt >= 4:
                    print("Du valde att köpa en falx.\n")
                    spelarens_attacker.append("falx")
                    antal_guldmynt -= 4
                    break
                elif val_av_rustning_eller_vapen in ["falx", "6"] and len(spelarens_attacker) >= 4 and antal_guldmynt >= 4:
                    print("Du måste sälja en av dina vapen, eftersom du kan inte bära mer än två vapen.\n")
                    break
                elif val_av_rustning_eller_vapen in ["falx", "6"] and len(spelarens_attacker) < 4 and antal_guldmynt < 4:
                    print("Du har tyvärr inte tillräckligt med guldmynt.\n")
                    break
                #-------------------falx-----------------#

            elif val_av_rustning_eller_vapen == "nej" or val_av_rustning_eller_vapen == "0":
                print("Du valde att köpa ingenting.")
                input("Tryck enter för att fortsätta.")
                break
            else:
                print("Fel input!")
                print("Ange rätt val!")

    #Sälja vapen/rustning
    elif vill_köpa_eller_sälja == "sälja":
        if len(spelarens_attacker) > 2 and ingen_rustning == False and (järnrustning == True or läderrustning == True):
            rensa_skärm()
            print("Hos smeden Richard kan du sälja följande vapen och rustning.")
            if "läderrustning" in spelarens_attacker:
                print("Läderrustning")
            elif "järnrustning" in spelarens_attacker:
                print("Järnrustning")
            if "kortsvärd" in spelarens_attacker:
                print("Kortsvärd")
            if "stridssvärd" in spelarens_attacker:
                print("Stridssvärd")
            if "kniv" in spelarens_attacker:
                print("Kniv")
            if "falx" in spelarens_attacker:
                print("Falx")
            print(f"Just nu har du {antal_guldmynt} guldmynt.")
            while True:
                vill_sälja_x = input("Skriv ditt val här om du vill inte sälja något skriv 0 eller nej: ").lower()
                if vill_sälja_x == "läderrustning" and läderrustning == True:
                    print("Du valde att sälja din läderrustning.")
                    print("Du fick 3 guldmynt från smeden.\n")
                    ingen_rustning = True
                    läderrustning = False
                    järnrustning = False
                    antal_guldmynt += 3
                elif vill_sälja_x == "järnrustning" and järnrustning == True:
                    print("Du valde att sälja din järnrustning.")
                    print("Du fick 6 guldmynt från smeden.\n")
                    ingen_rustning = True
                    läderrustning = False
                    järnrustning = False
                    antal_guldmynt += 6
                elif vill_sälja_x == "kortsvärd" and "kortsvärd" in spelarens_attacker:
                    print("Du valde att sälja din kortsvärd.")
                    print("Du fick 4 guldmynt från smeden.")
                    spelarens_attacker.remove("kortsvärd")
                    antal_guldmynt += 4
                elif vill_sälja_x == "kniv" and "kniv" in spelarens_attacker:
                    print("Du valde att sälja din kniv:")
                    print("Du fick 2 guldmynt från smeden.")
                    spelarens_attacker.remove("kniv")
                    antal_guldmynt += 2
                elif vill_sälja_x == "stridssvärd" and "stridssvärd" in spelarens_attacker:
                    print("Du valde att sälja din stridssvärd.")
                    print("Du fick 5 guldmynt från smeden.")
                    spelarens_attacker.remove("stridssvärd")
                    antal_guldmynt += 5
                elif vill_sälja_x == "falx" and "falx" in spelarens_attacker:
                    print("Du valde att sälja din falx.")
                    print("Du fick 3 guldmynt från smeden.")
                    spelarens_attacker.remove("falx")
                    antal_guldmynt += 3
                elif vill_sälja_x == "nej" or vill_sälja_x == "0":
                    print("Du valde att sälja ingenting.")
                    input("Tryck enter för att fortsätta.")
        elif ingen_rustning == True and läderrustning == False and järnrustning == False and len(spelarens_attacker) == 2:
            print("Du har ingenting att sälja.")
            input("Tryck enter för att fortsätta.")


#-----------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------#SPEL KODET#-----------------------------------------#
while True:    
    handel_med_smeden = 0
    runda = 1
    if ingen_rustning == True:
        spelarens_hp = 26
    elif läderrustning == True:
        spelarens_hp = 32
    elif järnrustning == True:
        spelarens_hp = 48
    motståndarens_hp = 0


    if antal_kämpade_strider == 0:
        print(f"\nDu är gladiatorn {spelarens_namn}, nu ska du slåss mot en gladiator.\n" \
"Du får välja mellan vem du vill slå mot:\n"
f"1. Drako: {Fore.RED}26{Style.RESET_ALL}hp har ingen rustning och kan ingen strategi. (erforderlig rank = 1)\n" \
f"2. Maximus: {Fore.RED}34{Style.RESET_ALL}hp, har läderrustning, tar 1 mindre skada per attack, kör strategiskt och har vapnet den blodtörstiga kortsvärdet. (erforderlig rank = 2)\n" 
f"3. Domnious Aurelius Valcar: {Fore.RED}50{Style.RESET_ALL}hp, har bättre rustning än Maximus, tar 2 mindre skada per attack. Han har aldrig blivit besegrat och har sin egen ikoniska vapen: Den stora Morgonstjärnan. (erforderlig rank = 3)\n"
f"Just nu har du {Fore.BLUE}{spelarens_hp}{Style.RESET_ALL}hp.\n"
"Ni kommer att befinna er på en romersk arena omgivna av en förväntsfull publik.\n" \
"Just nu har ni inga vapen, men efter varje runda slänger publiken en vapen i arenan.\n" \
"Publiken kommer att ge er vapen endast i striden mot Drako annars kommer du behöva köpa själv.\n" \
"striden består av 3 rundor, om ni båda överlever då slutar stridet efter tredje rundan\n"    
"Målet är att befria sig genom att vinna mot alla 3 och vid död avslutar spelet.")
        
    if antal_kämpade_strider > 0:

        ####nedan ligger smeden####
        if besegrad_drako == True:
            vill_köpa_eller_sälja_mer_bool = True
            print("Du kommer snart få välja vem du vill slåss mot.")
            print("Men innan ska du få välja om du vill gå till smeden för att köpa eller sälja rustning/vapen.")
            while True:      
                vill_gå_till_smeden = input("Skriv ja eller nej beroende på om du vill gå till smeden eller inte: ").lower()
                if vill_gå_till_smeden != "ja" and vill_gå_till_smeden != "nej":
                    print("\nFel input!")
                    print("Ange ett giltigt val!\n")
                    
                elif vill_gå_till_smeden == "ja":
                    print("Du valde att gå till smeden.")
                    smeden()
                    while True:                       
                        vill_köpa_eller_sälja_mer = input("Vill du köpa eller sälja något mer? ja/nej: ").lower()
                        if vill_köpa_eller_sälja_mer != "nej" and vill_köpa_eller_sälja_mer != "ja":
                            print("Fel input!\n")
                        elif vill_köpa_eller_sälja_mer == "ja":
                            print("Du valde att köpa eller sälja något mer.")
                            smeden()
                        elif vill_köpa_eller_sälja_mer == "nej":
                            print("Du valde att inte köpa eller sälja något mer.")
                            input("Tryck enter för att fortsätta.")
                            rensa_skärm()
                            vill_köpa_eller_sälja_mer_bool = False
                            break  
                elif vill_gå_till_smeden == "nej":
                    print("Du valde att inte gå till smeden.")
                    input("Tryck enter för att fortsätta.")
                    break
                if vill_köpa_eller_sälja_mer_bool == False:
                    break
        

##############     #smeden avslutas     ###########

        print("\nNedan kan du välja vem du vill slå mot.")
        if besegrad_drako == True:
            print(f"1. Drako: {Fore.RED}26{Style.RESET_ALL}hp, har ingen rustning och kan ingen strategi. (Besegrad, död)")
        else:
            print(f"1. Drako: {Fore.RED}26{Style.RESET_ALL}hp, har ingen rustning och kan ingen strategi. (erforderlig rank = 1 (tiggare))")    
        if besegrad_maximus == True:
            print(f"2. Maximus: {Fore.RED}34{Style.RESET_ALL}hp, har rustning, kör strategiskt och har vapnet den blodtörstiga kortsvärdet. (Besegrad, död)")
        else:
            print(f"2. Maximus: {Fore.RED}34{Style.RESET_ALL}hp, har rustning, kör strategiskt och har vapnet den blodtörstiga kortsvärdet. (erforderlig rank = 2 (legosoldat))")
        if besegrad_dominous == True:
            print(f"3. Domnious Aurelius Valcar: {Fore.RED}50{Style.RESET_ALL}hp, har bättre rustning än Maximus och har aldrig blivit besegrat av någon förutom dig. (Besegrad, död)")
        else:
            print(f"3. Domnious Aurelius Valcar: {Fore.RED}50{Style.RESET_ALL}hp, har bättre rustning än Maximus och har aldrig blivit besegrat. (erforderlig rank = 3 (gladiator))")

    print(f"\nDin nuvarande rank är {rank_nummer}: {rank_namn}\n")

    val_av_motståndare = input("Här kan du skriva din val av motståndare: ").capitalize()

    while True:
        if val_av_motståndare == "1":
            val_av_motståndare = "Drako"
        elif val_av_motståndare == "2":
            val_av_motståndare = "Maximus"
        elif val_av_motståndare == "3":
            val_av_motståndare = "Dominous"

        if val_av_motståndare == "Drako" and rank_nummer == 1:
            motståndarens_hp += drako_hp
        elif val_av_motståndare == "Maximus" and rank_nummer == 2:
            motståndarens_hp += maximus_hp
            motståndarens_attacker.append("kortsvärd")
        elif val_av_motståndare == "Dominous" and rank_nummer == 3:
            motståndarens_hp += dominous_aurelius_valcar_hp
            motståndarens_attacker.append("morgonstjärna")#Dominous's ikoniska vapen morgonstjärnan

        if rank_nummer == 1 and val_av_motståndare == "Maximus":
            print("För att slåss mot Maximus måste din rank vara 2.")
            val_av_motståndare = input("Välj en motståndare som du kan slåss med  på din nuvarande rank. ").capitalize()
        elif rank_nummer == 1 and val_av_motståndare == "Dominous":
            print("För att slåss mot Dominous måste din rank vara 3.")
            val_av_motståndare = input("Välj en motståndare som du kan slåss med på din nuvarande rank. ").capitalize()
        elif rank_nummer == 2 and val_av_motståndare == "Dominous":
            print("För att slåss mot Dominous måste din rank vara 3.")
            val_av_motståndare = input("Välj en motståndare som du kan slåss med på din nuvarande rank. ").capitalize()        
        elif val_av_motståndare == "Drako" and besegrad_drako == True:
            print("Du har redan besegrat Drako och han är död.")
            val_av_motståndare = input("Välj en motståndare som du inte har besegrat än! ").capitalize()
        elif val_av_motståndare == "Maximus" and besegrad_maximus == True:
            print("Du har redan besegrat Maximus och han är död.")
            val_av_motståndare = input("Välj en motståndare som du inte har besegrat än! ").capitalize()
        elif val_av_motståndare == "Dominous" and besegrad_dominous == True:
            print("Du har redan besegrat Dominous och han är död.")
            val_av_motståndare = input("Välj en motståndare som du inte har besegrat än! ").capitalize()
        elif val_av_motståndare == "Maximus" or val_av_motståndare == "Drako" or val_av_motståndare == "Dominous":
            print(f"\nDu valde att slåss mot {val_av_motståndare} och han ser ut att göra sig redo till anfall.")
            input("Tryck enter för att påbörja striden.")
        else:
            print("FEL INPUT!")
            val_av_motståndare = input("Välj motståndare!: ").capitalize()

        if (val_av_motståndare == "Maximus" and besegrad_maximus == False and rank_nummer == 2 and motståndarens_hp == 34) or (val_av_motståndare == "Drako" and besegrad_drako == False and rank_nummer == 1 and motståndarens_hp == 26) or (val_av_motståndare == "Dominous" and besegrad_dominous == False and rank_nummer == 3 and motståndarens_hp == 50):
            break


    print("================================================================================================")
    while spelarens_hp > 1 and motståndarens_hp > 1:
        vid_ge_upp = ["avrätta", "fortsätta", "gå"]

        rensa_skärm()

        print(f"\n{Fore.BLUE}Runda{Fore.RED} {runda} {Style.RESET_ALL}{Fore.BLUE}börjar.{Style.RESET_ALL}")

        print("Du har följande attacker i rundan:")
        print("Näve: gör 2-3 skada och har träffchans 2 av 3.")
        print("Spark: gör 1-2 skada och har träffchans 4 av 5.")
        if "falx" in spelarens_attacker:
            print("Falx: gör 5 skada och har träffchans 8 av 11.")
        if "stridssvärd" in spelarens_attacker:
            print("Stridssvärd: gör 7-8 skada och har träffchans 7 av 10.")
        if "klubba" in spelarens_attacker:
            print("Klubba: gör 5 skada och har träffchans 3 av 5.")
        elif "kniv" in spelarens_attacker:
            print("Kniv: gör 4 skada och har träffchans 3 av 5.")
        if "yxa" in spelarens_attacker:
            print("Yxa: gör 5 skada och har träffchans 4 av 5.")
        elif "kortsvärd" in spelarens_attacker:
            if val_av_motståndare == "Drako":
                print("Kortsvärd: gör 6-7 skada och har träffchansen 1 av 1.(Kan användas endast en gång eftersom den är gammal och rostigt.)")
            else:
                print("Kortsvärd: gör 6-7 skada och har träffchancen 8 av 10.")
        

        for i in range(5):

            spelarens_attack = input("\nSkriv ditt val här: ").lower()

            while True:
                if spelarens_attack not in spelarens_attacker: 
                    print("Fel val av attack!")
                    spelarens_attack = input("Skriv ditt val här!!!!: ").lower()
                if spelarens_attack in spelarens_attacker:
                    break

            träffskada(spelarens_attack)
        
            if motståndarens_hp > 0 and spelarens_hp > 0:
                visa_hp()
            if motståndarens_hp < 1 or spelarens_hp < 1:
                break


####################   NEDAN VÄLJER SPELAREN OM HEN VILL HA VAPNET ELLER INTE.    Gäller endast i striden mot Drako   #################################


        if val_av_motståndare == "Drako":
            vapen_runda1 = ["kniv", "klubba"]
            vapen_runda2 = ["yxa", "kortsvärd"]
            vem_får_vapen_rundax = ["spelaren", "motståndaren"]
            sparad_vapen_runda1 = random.choice(vapen_runda1)
            sparad_vapen_runda2 = random.choice(vapen_runda2)

            if runda == 1:
                print(f"\nPubliken kastade en {sparad_vapen_runda1} i arenan.")
            elif runda == 2:
                print(f"\nPubliken kastade en {sparad_vapen_runda2} i arenan.")
            if runda == 1 or runda == 2:
                
                while True:
                    vill_ha_vapen = input(f"För att försöka ta vapnet före {val_av_motståndare} skriv ja annars nej. ").lower()
                    if vill_ha_vapen == "ja":
                    
                        if ingen_rustning == True:
                            vem_får_vapen_rundax.append("spelaren")
                            sparad_vem_får_vapen_rundax = random.choice(vem_får_vapen_rundax)
                        elif järnrustning == True:
                            vem_får_vapen_rundax.append("motståndaren")
                            sparad_vem_får_vapen_rundax = random.choice(vem_får_vapen_rundax)

                        if runda == 1 and sparad_vapen_runda1 == "kniv" and sparad_vem_får_vapen_rundax == "spelaren":
                            print(f"Du fick tag i vapnet före {val_av_motståndare}.")
                            spelarens_attacker.append("kniv")
                        elif runda == 1 and sparad_vapen_runda1 == "kniv" and sparad_vem_får_vapen_rundax == "motståndaren":
                            print(f"{val_av_motståndare} fick tag i vapnet före dig")
                            motståndarens_attacker.append("kniv")
                        elif runda == 1 and sparad_vapen_runda1 == "klubba" and sparad_vem_får_vapen_rundax == "spelaren":
                            print(f"Du fick tag i vapnet före {val_av_motståndare}.")
                            spelarens_attacker.append("klubba")
                        elif runda == 1 and sparad_vapen_runda1 == "klubba" and sparad_vem_får_vapen_rundax == "motståndaren":
                            print(f"{val_av_motståndare} fick tag i vapnet före dig")
                            motståndarens_attacker.append("klubba")

                        elif runda == 2 and sparad_vapen_runda2 == "yxa" and sparad_vem_får_vapen_rundax == "spelaren":
                            print(f"Du fick tag i vapnet före {val_av_motståndare}.")
                            spelarens_attacker.append("yxa")
                        elif runda == 2 and sparad_vapen_runda2 == "yxa" and sparad_vem_får_vapen_rundax == "motståndaren":
                            print(f"{val_av_motståndare} fick tag i vapnet före dig")
                            motståndarens_attacker.append("yxa")
                        elif runda == 2 and sparad_vapen_runda2 == "kortsvärd" and sparad_vem_får_vapen_rundax == "spelaren":
                            print(f"Du fick tag i vapnet före {val_av_motståndare}.")
                            spelarens_attacker.append("kortsvärd")
                        elif runda == 2 and sparad_vapen_runda2 == "kortsvärd" and sparad_vem_får_vapen_rundax == "motståndaren":
                            print(f"{val_av_motståndare} fick tag i vapnet före dig")
                            motståndarens_attacker.append("kortsvärd")

                    elif vill_ha_vapen == "nej":
                        if runda == 1 and sparad_vapen_runda1 == "kniv":
                            print(f"{val_av_motståndare} fick tag i vapnet.")
                            motståndarens_attacker.append("kniv")
                        elif runda == 1 and sparad_vapen_runda1 == "klubba":
                            print(f"{val_av_motståndare} fick tag i vapnet.")
                            motståndarens_attacker.append("klubba")
                        elif runda == 2 and sparad_vapen_runda2 == "yxa":
                            print(f"{val_av_motståndare} fick tag i vapnet.")
                            motståndarens_attacker.append("yxa")
                        elif runda == 2 and sparad_vapen_runda2 == "kortsvärd":
                            print(f"{val_av_motståndare} fick tag i vapnet.")
                            motståndarens_attacker.append("kortsvärd")
                    else: 
                        print("Fel input!")

                    if vill_ha_vapen == "ja" or vill_ha_vapen == "nej":
                        input("Tryck enter för att fortsätta. ")
                        break

        if runda == 3 and spelarens_hp > 0 and motståndarens_hp > 0:
            print("Spelet har avslutats och ingen dog.")
            antal_kämpade_strider += 1


        if (runda == 1 or runda == 2) and (val_av_motståndare == "Maximus" or val_av_motståndare == "Dominous"):
            vill_spelaren_ge_upp = input("\nVill du ge upp(ja/nej). Vid ja röstar folket om om du får gå, avrättas, eller att du måste fortsätta. ").lower()
            
            if vill_spelaren_ge_upp == "ja":
                print("\nDu valde att ge upp.")

                if (motståndarens_hp - spelarens_hp) > 10 and runda == 1:
                    vid_ge_upp.remove("gå")
                    vid_ge_upp.extend(["fortsätta", "fortsätta", "avrätta", "avrätta", "avrätta", "fortsätta", "fortsätta"])
                elif (motståndarens_hp - spelarens_hp) > 15 and runda == 2:
                    vid_ge_upp.remove("gå")
                    vid_ge_upp.extend(["avrätta", "avrätta", "avrätta", "fortsätta", "fortsätta"])
                elif (spelarens_hp - motståndarens_hp) > 9 and runda == 1:
                    vid_ge_upp.remove("avrätta",)
                    vid_ge_upp.extend(["gå", "gå", "gå", "gå", "gå", "fortsätta"])
                elif (spelarens_hp - motståndarens_hp) > 9 and (runda == 2 or runda == 1):
                    vid_ge_upp.remove("avräta")
                    vid_ge_upp.extend(["gå", "gå", "gå", "gå", "fortsätta"])
                else:
                    vid_ge_upp.extend(["fortsätta", "fortsätta", "fortsätta", "fortsätta", "gå", "gå"])


                sparad_vid_ge_upp = random.choice(vid_ge_upp)
                if sparad_vid_ge_upp == "avrätta":
                    print("Folket röstade på att du ska avrättas.")
                    print("╔══════════════════════════════════╗\n"
                    "║  ☠️       D U   D Ö R       ☠️  ║\n"
                    "╚══════════════════════════════════╝\n")
                    exit()
                elif sparad_vid_ge_upp == "gå":
                    print("Folket röstade på att du ska få gå eftersom kungen var något nöjd med ditt presterande.")
                    print("╔════════════════════════════════════╗\n"
                    "║  ☠️  D U   F Ö R L O R A D E  ☠️  ║\n"
                    "╚════════════════════════════════════╝\n")
                    break
                
                elif sparad_vid_ge_upp == "fortsätta":
                    print("Folket röstade på att du måste fortsätta eftersom kungen är inte riktigt nöjd än.")
                    input("tryck enter för att fortsätta.")

        runda += 1
        if runda > 3:
            break

    if besegrad_drako == True and besegrad_dominous == True and besegrad_maximus == True:
        print(f"{Fore.LIGHTGREEN_EX}\nGrattis{Style.RESET_ALL}!")
        print("Du har fortjänat din frihet.\n")
        exit()
    
    if val_av_motståndare == "Drako":
        spelarens_attacker = ["näve", "spark"]
        motståndarens_attacker = ["näve", "spark"]
    
    while True:
        vill_fortsätta = input("\nVill du fortsätta spela? ja/nej ").lower()
        if vill_fortsätta == "nej":
            print("\nSpelet avslutas.")
            exit()
        elif vill_fortsätta == "ja":
            print("Du valde att fortsätta.")
            input("Tryck enter.")
        else: 
            print("Ange giltig input!")

        if vill_fortsätta == "ja" or vill_fortsätta == "nej":
            break

    rensa_skärm()

    print("=================================================================================================")

    if antal_kämpade_strider == 1:
        print("Bra jobbat!")
        print("Du har kämpat din första strid.")
    
    if val_av_motståndare == "Drako" and besegrad_drako == True:
        if antal_kämpade_strider > 1:
            print("Bra jobbat!")
        print("Kungen har erkänt dig och från och med nu kommer han vara med och titta på dig medan du slåss.")
        print("Så försök att inte göra honom besviken.\n")
