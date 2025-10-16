import random
from colorama import Style, Fore, Back 

antal_rundor = 4

spelarens_hp = 20 

motståndarens_hp = 0

drako_hp = 20
maximus_hp =30
   
attack_val = ["näve", "Spark"] 

#-----------------------------------------TRÄFFCHANS FÖR NÄVE OCH SPARK----------------------------------#

#Träffchanset för näve:
def träffchans_näve():
    träffchans_näve = random.choice(["träff", "miss", "miss"])
    return träffchans_näve

#Träffchans för spark:
def träffchans_spark():
    träffchans_spark = random.choice(["träff", "träff", "miss"])
    return träffchans_spark
#-------------------------------------------------------------------------------------------------------#

                                    ###---------INTRO--------###

val_av_svårhet = input("Du är gladiatorn Rikke, nu ska du sloss mot en gladiator, Du får välja mellan vem du vill slo mot:\n" 
"1. Drako(20hp, tar lika mycket skada som dig)\n2. Maximus(30hp, tar mindre skada än Drako)\nOavsett motståndare har du 20hp.\n" 
"Ni kommer att befinna er på en romersk arena omgivna av en förväntsfull publik, just nu har ni inga vapen, men efter varje runda får vinnaren en slumpmässigt vapen vald av publiken, striden består av 3 rundor, om ni båda lever efter tredje rundan då slutar  stridet.\n" 
"Här kan du skriva din val av motsåndare:").lower()

'''def maximus_val_runda1():
    if motståndarens_hp ='''

#------------------------Bestämmer motståndarens hp baserad på val av svårhet/motståndare och bestämmer ochså mostsåndarens val av attack------------------------------#

if val_av_svårhet == "drako":
    motståndarens_hp += 20
elif val_av_svårhet == "maximus":
    motståndarens_hp += 30

drako_val = random.choice(attack_val)


                                      #INTRO/

# funktionen nedan hanterar alla möjliga kombinationer av attacker
#Jag frågade AIn om möjliga kombinationer och den gav mig 16 kombinationer och sedan skrev jag if satsen enligt de.
#Jag använde AIn endast för att få reda på möjliga utfall.

def träff_skada():
    sparad_träffchans_näve1 = träffchans_näve()
    sparad_träffchans_näve2 = träffchans_näve()
    sparad_träffchans_spark1 = träffchans_spark()
    sparad_träffchans_spark2 = träffchans_spark()

    global motståndarens_hp
    global drako_hp 
    global spelarens_hp
                        #Jag delar if satsen i 4 delar för enklighetens skuld. Del 1 är nedan:
    if spelarens_val == "näve" and sparad_träffchans_näve1 == "träff" and drako_val == "näve" and sparad_träffchans_näve2 == "miss":
        print(f"{val_av_svårhet} missar och din järnhård näve träffar honom rakt i käken.")
        motståndarens_hp -= random.randint(2,3)
   
    elif spelarens_val == "näve" and sparad_träffchans_näve1 == "miss" and drako_val == "näve" and sparad_träffchans_näve2 == "träff":
        print(f"Du missar och {val_av_svårhet}'s näve träffar dig rakt i käken.")
        motståndarens_hp -= random.randint(2,3)
    
    elif spelarens_val == "näve" and sparad_träffchans_näve1 == "träff" and drako_val == "näve" and sparad_träffchans_näve2 == "träff":
        print(f"Ni båda träffar varann i ansiktet.")
        spelarens_hp -= random.randint(2,3)
        motståndarens_hp -= random.randint(2,3)

    elif spelarens_val == "näve" and sparad_träffchans_näve1 == "miss" and drako_val == "näve" and sparad_träffchans_näve2 == "miss":
        print(f"Ni båda missar och stirrar på varann med lömsk blick.")
                        #Del 2:
    elif spelarens_val == "näve" and sparad_träffchans_näve1 == "träff" and drako_val == "spark" and sparad_träffchans_spark2 == "miss":
        print(f"{val_av_svårhet} missar och du träffar {val_av_svårhet} rakt i ansiktet.")
        motståndarens_hp -= random.randint(2,3)
    
    elif spelarens_val == "näve" and sparad_träffchans_näve1 == "miss" and drako_val == "spark" and sparad_träffchans_spark2 == "träff":
        print(f"Du missar och {val_av_svårhet} sparkar dig rakt i magen.")
        spelarens_hp -= random.randint(1,2)
    
    elif spelarens_val == "näve" and sparad_träffchans_näve1 == "träff" and drako_val == "spark" and sparad_träffchans_spark2 == "träff":
        print(f"Du träffar {val_av_svårhet} i ansiktet samtidigt som han sparkar dig rakt i magen.")
        spelarens_hp -= random.randint(1,2)
        motståndarens_hp -= random.randint(2,3)
    
    elif spelarens_val == "näve" and sparad_träffchans_näve1 == "miss" and drako_val == "spark" and sparad_träffchans_spark2 == "miss":
        print(f"Ni båda missar och stirrar på varandra med lömsk blick")
                        #Del 3:
    elif spelarens_val == "spark" and sparad_träffchans_spark1 == "träff" and drako_val == "näve" and sparad_träffchans_näve2 == "miss":
        print(f"Drako missar och du träffar {val_av_svårhet} drako i benet.")
        motståndarens_hp -= random.randint(1,2)
    
    elif spelarens_val == "spark" and sparad_träffchans_spark1 == "miss" and drako_val == "näve" and sparad_träffchans_näve2 == "träff":
        print(f"Du missar och {val_av_svårhet} träffar dig rakt i revbenet.")
        spelarens_hp -= random.randint(2,3)

    elif spelarens_val == "spark" and sparad_träffchans_spark1 == "träff" and drako_val == "näve" and sparad_träffchans_näve2 == "träff":
        print(f"Din spark träffar {val_av_svårhet} i benet men samtidigt träffar han dig i ansiktet.")
        spelarens_hp -= random.randint(2,3)
        motståndarens_hp -= random.randint(1,2)
    
    elif spelarens_val == "spark" and sparad_träffchans_spark1 == "miss" and drako_val == "näve" and sparad_träffchans_näve2 == "miss":
        print(f"Ni båda missar och stirrar på varandra med lömsk blick.")
                        #Del 4
    elif spelarens_val == "spark" and sparad_träffchans_spark1 == "träff" and drako_val == "spark" and sparad_träffchans_spark2 == "miss":
        print(f"{val_av_svårhet} missar och du träffar honom i benet.")
        motståndarens_hp -= random.randint(1,2)
    
    elif spelarens_val == "spark" and sparad_träffchans_spark1 == "miss" and drako_val == "spark" and sparad_träffchans_spark2 == "träff":
        print(f"Du missar och {val_av_svårhet} träffar dig i benet.")
        spelarens_hp -= random.randint(1,2)

    elif spelarens_val == "spark" and sparad_träffchans_spark1 == "träff" and drako_val == "spark" and sparad_träffchans_spark2 == "träff":
        print(f"Ni båda träffar varandra i benet.")
        spelarens_hp -= random.randint(1,2)
        motståndarens_hp -= random.randint(1,2)

    elif spelarens_val == "spark" and sparad_träffchans_spark1 == "miss" and drako_val == "spark" and sparad_träffchans_spark2 == "miss":
        print(f"Ni båda missar och stirrar på varandra med lömsk blick.")
#----------------------------------------------------------------------------------------------------------------------------------------------------#


#-----funktionen visar hp-----#

def visa_hp():
    print(f"Din hp är {Fore.BLUE}{spelarens_hp}.{Style.RESET_ALL}")

    print(f"Fiendens hp är {Fore.RED}{motståndarens_hp}.{Style.RESET_ALL}")


#-----------------------------------------------------------------------------#

'''val_av_svårhet = input("Du är gladiatorn Rikke, nu ska du sloss mot en gladiator, Du får välja mellan vem du vill slo mot:\n" 
"1. Drako(20hp, tar lika mycket skada som dig)\n2. Maximus(30hp, tar mindre skada än Drako)\nOavsett motståndare har du 20hp.\n" 
"Ni kommer att befinna er på en romersk arena omgivna av en förväntsfull publik, just nu har ni inga vapen, men efter varje runda får vinnaren en slumpmässigt vapen vald av publiken, striden består av 3 rundor, om ni båda lever efter tredje rundan då slutar  stridet.\n" 
"Här kan du skriva din val av motsåndare:").lower()'''
#Här får spelaren välja motståndare.

if val_av_svårhet == "drako" or val_av_svårhet == "maximus":
    print(f"\nDu valde att slo mot {val_av_svårhet} och han ser ut att göra sig redo till att gå till anfall.")
    input("Tryck enter för att påbörja striden.")
else:
    print("Fel input")
    val_av_svårhet = input("\nVälj motståndare. Drako eller Maximus.\nVid fel input igen kommer spelet att avslutas!").lower()
    if val_av_svårhet == "drako" or val_av_svårhet == "maximus":
        input("Tryck enter för att påbörja striden.")
    else:
        exit()

if val_av_svårhet == "drako":
    print("\nStriden mellan dig och Drako har börjat.")
elif val_av_svårhet == "maximus":
    print("\nStriden mellan dig och Maximus har börjat.")


#visa_hp()
#spelarens_val = input("Du och din fiende har följande attacker i första rundan:\nJärnhård näve: gör mellan 2-3 skada. Träffchansen är 1 av 3\nKvick spark: Gör mellan 1-2 skada. Träffchansen är 2 av 3.\n Skriv din val här(näve eller spark):").lower()


                                                            #SPEL KODET BÖRJAR HÄR 
while antal_rundor > 0:
    for i in range(5):
        spelarens_val = input("Välj en av följande attacker:\n" \
    "näve: 2-3 skada och har träffchans 1 i 3\n" \
    "spark: 1-2 skada och har träffchans 2 i 3\n" \
    "\nSkriv ditt val här:\n")
    
        träff_skada()
        visa_hp()

        if spelarens_hp < 1:
            print("\nDu förlorade")
            break
        elif drako_hp < 1:
            print("\nDu vann")
            break
    if spelarens_hp < 1 or drako_hp < 1:
        break

    input("Tryck enter för att fortsätta.\n")
if antal_rundor == 4:
    print("\nRunda 2 börjar\n")
elif antal_rundor == 3:
    print("\nRunda 3 börjar.\n")
elif antal_rundor == 2:
    print("\nRunda 4 börjar.\n")
elif antal_rundor == 4:
    print("\nRunda 5 börjar.\n")
antal_rundor -= 1

    