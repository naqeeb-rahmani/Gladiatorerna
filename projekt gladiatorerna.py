import random
from colorama import Style, Fore, Back 
import os

#---------------------------------------VARIABLER-----------------------------------------#

runda = 1

spelarens_hp = 26

motståndarens_hp = 0

drako_hp = 26
maximus_hp =34

spelarens_attacker = ["näve", "spark"]
motståndarens_attacker = ["näve", "spark"]

vapen_runda1_vinnare = random.choice(["kniv", "klubba"])
vapen_runda2_vinnare = random.choice(["yxa", "kortsvard"])

vid_ge_upp = random.choice(["avrätta", "fortsätta", "gå"])

#-----------------------------------------------------------------------------------------#


#----------------------------------------------INTRO-------------------------------------------#

print(f"===========\n{Fore.RED}GLADIATORER{Style.RESET_ALL}\n===========")

print("Välkommen till spelet gladiatorer!")
spelarens_namn = input("Ange din gladiators namn:").capitalize()

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

print(f"\nDu är gladiatorn {spelarens_namn}, nu ska du sloss mot en gladiator.\n" \
"Du får välja mellan vem du vill slo mot:\n"
"1. Drako (26hp, har ingen armour och kan ingen strategi)\n" \
"2. Maximus (34hp, har armour och kör strategiskt)\n" \
"Oavsett motståndare har du 26hp.\n"
"Ni kommer att befinna er på en romersk arena omgivna av en förväntsfull publik.\n" \
"Just nu har ni inga vapen, men efter varje runda får spelaren med mest hp en slumpmässigt vapen vald av publiken.\n" \
"Vid lika mycket hp i slutet av rundan får ingen en vapen.\n" \
"striden består av 3 rundor, om ni båda överlever då  slutar stridet efter tredje rundan.")
val_av_motståndare = input("Här kan du skriva din val av motståndare:").capitalize()

if val_av_motståndare == "Maximus" or val_av_motståndare == "Drako":
    print(f"Du valde att sloss mot {val_av_motståndare} och han ser ut att göra sig redo till anfall.")
    input("Tryck enter för att påbörja striden.")

else:
    print("FEL INPUT!")
    val_av_motståndare = input("Välj motståndare:").capitalize()
    if val_av_motståndare == "Drako" or val_av_motståndare == "Maximus":
        print(f"Du valde att sloss mot {val_av_motståndare} och han ser ut att göra sig redo till anfall.")
        input("Tryck enter för att påbörja striden.")
    else:
        exit()

#------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------FUNKTIONER----------------------------------------------------------#

def visa_hp():
    print(f"Din hp är {Fore.BLUE}{spelarens_hp}.{Style.RESET_ALL}")
    print(f"Fiendens hp är {Fore.RED}{motståndarens_hp}.{Style.RESET_ALL}")

def drako_val_av_attack(): # I funktionen väljer drako fram slumpmässigt en attack
    return random.choice(motståndarens_attacker)

def maximus_val_av_attack(): # Här väljer maxmimus fram en attack baserad på spelarens och sin hp.
    if spelarens_hp < 6 and "kortsvärd" in motståndarens_attacker:
        return "kortsvärd"
    elif spelarens_hp < 3 and "yxa" in motståndarens_attacker:
        return "yxa"
    elif spelarens_hp > 20:
        return "spark"
    elif spelarens_hp < 2:
        return "spark"
    elif motståndarens_hp < 10:
        return "spark"
    else: 
        return random.choice(motståndarens_attacker)
    
#Funktionen nedan rensar kärmet.
def rensa_skärm():
    os.system("cls") 



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
        return "träff"


#---#FUNKTIONEN NEDAN HANTERAR ALLA ATTACKER, SKADA OCH SKRIVER UT OM SPELAREN HAR VUNNIT ELLER INTE#---#

def träffskada(spelarens_attack):

    global spelarens_hp
    global motståndarens_hp

    if val_av_motståndare == "Drako":
        motståndarens_attack = drako_val_av_attack()
    elif val_av_motståndare == "Maximus":
        motståndarens_attack = maximus_val_av_attack()

    spelarens_träffchans_näve = träffchans_näve()
    spelarens_träffchans_spark = träffchans_spark()
    spelarens_träffchans_yxa = träffchans_yxa()
    spelarens_träffchans_kniv = träffchans_kniv()
    spelarens_träffchans_klubba = träffchans_klubba()
    spelarens_träffchans_kortsvärd = träffchans_kortsvärd()

    motståndarens_träffchans_näve = träffchans_näve()
    motståndarens_träffchans_spark = träffchans_spark()
    motståndarens_träffchans_yxa = träffchans_yxa()
    motståndarens_träffchans_kniv = träffchans_kniv()
    motståndarens_träffchans_klubba = träffchans_klubba()
    motståndarens_träffchans_kortsvärd = träffchans_kortsvärd()


    if spelarens_attack == "näve" and spelarens_träffchans_näve == "träff":
        if groteskt == False:
            print(f"\nDin näve träffar {val_av_motståndare} i magen.")
        elif groteskt == True:
            print(f"\nDin järnhård näve träffar {val_av_motståndare} så hårt i magen att han börjar spitta blod.")
        motståndarens_hp -= random.randint(2,3)
    elif spelarens_attack == "näve" and spelarens_träffchans_näve == "miss":
        print("Du missar.")  

    elif spelarens_attack == "spark" and spelarens_träffchans_spark == "träff":
        if groteskt == False:
            print(f"\nDin spark träffar {val_av_motståndare}.")
        elif groteskt == True:
            print(f"\nDin kraftfull spark träffar {val_av_motståndare} i sidan av magen och han tappade nästan ballansen. ")
        motståndarens_hp -= random.randint(1,2) 
    elif spelarens_attack == "spark" and spelarens_träffchans_spark == "miss":
        print("Du missar.")     

    elif spelarens_attack == "yxa" and spelarens_träffchans_yxa == "träff":
        if groteskt == False:
            print(f"\nDu träffar {val_av_motståndare} med yxan.")
        elif groteskt == True:
            print(f"\nDu träffar {val_av_motståndare} i axeln och sanden blir fylld av blod.")
        motståndarens_hp -= 5
    elif spelarens_attack == "yxa" and spelarens_träffchans_yxa == "miss":
        print("Du missar.") 

    elif spelarens_attack == "kniv" and spelarens_träffchans_kniv == "träff":
        if groteskt == False:
            print(f"\nDu träffar {val_av_motståndare} med knivet.")
        elif groteskt == True:
            print(f"\nDu hugger {val_av_motståndare} rakt i magen medan han skriker av smärta.")
        motståndarens_hp -= 4
    elif spelarens_attack == "kniv" and spelarens_träffchans_kniv == "miss":
        print("Du missar.") 

    elif spelarens_attack == "klubba" and spelarens_träffchans_klubba == "träff":
        if groteskt == False:
            print(f"\nDu träffar {val_av_motståndare} i huvudet med klubban.")
        elif groteskt == True:
            print(f"\nDu träffar {val_av_motståndare} rakt i huvudet med klubban.")
        motståndarens_hp -= 3
    elif spelarens_attack == "klubba" and spelarens_träffchans_klubba == "miss":
        print("Du missar.") 

    elif spelarens_attack == "kortsvärd" and spelarens_träffchans_kortsvärd == "träff":
        if groteskt == False:
            print(f"\nDu träffar {val_av_motståndare} med kortsvärdet.")
        elif groteskt == True:
            if motståndarens_hp > 7:
                print(f"Du huggar {val_av_motståndare} i magen.")
            elif motståndarens_hp < 7:
                print(f"\nDu huggar av {val_av_motståndare}'s huvud och sanden blir rött fylld av blod.")
            else:
                print(f"\nDu träffar {val_av_motståndare} rakt i magen och blodet rinner snabbt från såret.")
        motståndarens_hp -= random.randint(6,7)
        spelarens_attacker.remove("kortsvärd")

    if motståndarens_hp < 1: 
        print(f"{val_av_motståndare} faller till marken.")
        print("╔══════════════════════════╗\n"
              "║  ⚔️  D U   V A N N  ⚔️  ║\n" 
              "╚══════════════════════════╝\n") 
        exit()


    if motståndarens_attack == "näve" and motståndarens_träffchans_näve == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i magen.")
        elif groteskt == True:
            print(f"{val_av_motståndare} träffar dig rakt i magen och du börjar att spitta blod.")
        spelarens_hp -= random.randint(2,3)
    elif motståndarens_attack == "näve" and motståndarens_träffchans_näve == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "spark" and motståndarens_träffchans_spark == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i benet.")
        elif groteskt == True:
            print(f"{val_av_motståndare} träffar dig rakt i magen och du skrek av smärtan.")
        spelarens_hp -= random.randint(1,2)
    elif motståndarens_attack == "spark" and motståndarens_träffchans_spark == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "yxa" and motståndarens_träffchans_yxa == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i axeln med en yxa.")
        elif groteskt == True:
            print(f"{val_av_motståndare} träffar dig vid axeln och blodet rinner snabbt från såret.")
        spelarens_hp -= 5
    elif motståndarens_attack == "yxa" and motståndarens_träffchans_yxa == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "kniv" and motståndarens_träffchans_kniv == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i magen med en kniv.")
        elif groteskt == True:
            print(f"{val_av_motståndare} huggar dig i magen och blod börjar rinna väldigt snabbt från såret.")
        spelarens_hp -= 4
    elif motståndarens_attack == "kniv" and motståndarens_träffchans_kniv == "miss":
        print(f"{val_av_motståndare} missar.")

    elif motståndarens_attack == "klubba" and motståndarens_träffchans_klubba == "träff":
        if groteskt == False:
            print(f"{val_av_motståndare} träffar dig i huvudet med en klubba.")
        elif groteskt == True:
            print(f"{val_av_motståndare} träffar dig rakt i ansiktet med klubban.")
        spelarens_hp -= 3
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
        spelarens_hp -= random.randint(6,7)
        motståndarens_attacker.remove("kortsvärd")

    if spelarens_hp < 1:
        print("Du faller til marken.")
        print("╔════════════════════════════════════╗\n"
              "║  ☠️  D U   F Ö R L O R A D E  ☠️  ║\n"
              "╚════════════════════════════════════╝\n")
        exit()



#-----------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------IF SATSER-------------------------------------------------------------#

if val_av_motståndare == "Drako":
    motståndarens_hp += drako_hp
elif val_av_motståndare == "Maximus":
    motståndarens_hp += maximus_hp


#----------------------------------------------------------------------------------------------------------------------------------# 

#-----------------------------------------#SPEL KODET#-----------------------------------------#

print("================================================================================================")
while spelarens_hp > 1 or motståndarens_hp > 1:
    print(f"\n{Fore.BLUE}Runda{Fore.RED} {runda} {Style.RESET_ALL}{Fore.BLUE}börjar.{Style.RESET_ALL}")

    print("Du har följande attacker i rundan:")
    print("Näve: gör 2-3 skada och har träffchans 2 av 3.")
    print("Spark: gör 1-2 skada och har träffchans 4 av 5.")
    if "klubba" in spelarens_attacker:
        print("Klubba: gör 5 skada och har träffchans 3 av 5.")
    elif "kniv" in spelarens_attacker:
        print("Kniv: gör 4 skada och har träffchans 3 av 5.")
    if "yxa" in spelarens_attacker:
        print("Yxa: gör 5 skada och har träffchans 4 av 5.")
    elif "kortsvärd" in spelarens_attacker:
        print("Kortsvärd: gör 6-7 skada och har träffchansen 1 av 1.(Kan användas endast en gång eftersom den är gammal och rostigt.)")

    for i in range(5):

        spelarens_attack = input("\nSkriv ditt val här: ").lower()

        if spelarens_attack not in spelarens_attacker: 
            print("Fel val av attack!")
            spelarens_attack = input("Skriv ditt val här(vid fel input avslutas spelet!): ").lower()
        if spelarens_attack not in spelarens_attacker:
            print("spelet avslutas")
            exit()

        träffskada(spelarens_attack)
     
        visa_hp()
    
    if runda == 1 and spelarens_hp > motståndarens_hp:
        spelarens_attacker.append(vapen_runda1_vinnare)
    elif runda == 1 and motståndarens_hp > spelarens_hp:
        motståndarens_attacker.append(vapen_runda1_vinnare)
    elif runda == 2 and spelarens_hp > motståndarens_hp:
        spelarens_attacker.append(vapen_runda2_vinnare)
    elif runda == 2 and motståndarens_hp > spelarens_hp:
        motståndarens_attacker.append(vapen_runda2_vinnare)

    if runda == 3 and spelarens_hp > 0 and motståndarens_hp > 0:
        print("Spelet har avslutats och ingen dog.")
        

    runda += 1

    if runda > 3:
        break

    vill_spelaren_ge_upp = input("Vill du ge upp(ja/nej). Vid ja röstar folket om om du får gå, avrättas, eller att du måste fortsätta. ").lower()
     
    if vill_spelaren_ge_upp == "ja":
        print("\nDu valde att ge upp.")
        sparad_vid_ge_upp = vid_ge_upp
        if sparad_vid_ge_upp == "avrätta":
            print("Folket röstade på att du ska avrättas.")
            print("╔══════════════════════════════════╗\n"
            "║  ☠️       D U   D Ö R       ☠️  ║\n"
            "╚══════════════════════════════════╝\n")
            exit()
        elif sparad_vid_ge_upp == "gå":
            print("Folket röstade på att du ska få gå.")
            print("╔════════════════════════════════════╗\n"
              "║  ☠️  D U   F Ö R L O R A D E  ☠️  ║\n"
              "╚════════════════════════════════════╝\n")
            exit()
        elif sparad_vid_ge_upp == "fortsätta":
            print("Folket röstade på att du måste fortsätta.")
            input("tryck enter för att fortsätta.")

        
    rensa_skärm()
print("=================================================================================================")