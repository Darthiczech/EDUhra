# ███╗░░░███╗ ░█████╗░ ██████╗░ ███████╗   ██████╗░ ██╗░░░██╗   ████████╗ ░█████╗░ ███╗░░░███╗   ░█████╗░ ██████╗░ ░█████╗░ ███╗░░░███╗
# ████╗░████║ ██╔══██╗ ██╔══██╗ ██╔════╝   ██╔══██╗ ╚██╗░██╔╝   ╚══██╔══╝ ██╔══██╗ ████╗░████║   ██╔══██╗ ██╔══██╗ ██╔══██╗ ████╗░████║
# ██╔████╔██║ ███████║ ██║░░██║ █████╗░░   ██████╦╝ ░╚████╔╝░   ░░░██║░░░ ██║░░██║ ██╔████╔██║   ███████║ ██║░░██║ ███████║ ██╔████╔██║
# ██║╚██╔╝██║ ██╔══██║ ██║░░██║ ██╔══╝░░   ██╔══██╗ ░░╚██╔╝░░   ░░░██║░░░ ██║░░██║ ██║╚██╔╝██║   ██╔══██║ ██║░░██║ ██╔══██║ ██║╚██╔╝██║
# ██║░╚═╝░██║ ██║░░██║ ██████╔╝ ███████╗   ██████╦╝ ░░░██║░░░   ░░░██║░░░ ╚█████╔╝ ██║░╚═╝░██║   ██║░░██║ ██████╔╝ ██║░░██║ ██║░╚═╝░██║
# ╚═╝░░░░░╚═╝ ╚═╝░░╚═╝ ╚═════╝░ ╚══════╝   ╚═════╝░ ░░░╚═╝░░░   ░░░╚═╝░░░ ░╚════╝░ ╚═╝░░░░░╚═╝   ╚═╝░░╚═╝ ╚═════╝░ ╚═╝░░╚═╝ ╚═╝░░░░░╚═╝
'''
---STATUS---
Program/Hra by měla být plně funkční, ale je možné, že je někdě nějaká skrytá chyba.

---ZÁKLADNÍ POPIS---
Celá hra je RPG, nachází se zde Vesnice - obchod se zbraněmi, "klinika" - zdravotnice pro léčení. Bojiště - boje s nepříteli. Ve hře jsou rozmístěné eastereggy a vtipy.

---ZDROJE/PLÁN---
Jak jsem na to šel: Používal jsem POUZE: mé vědomosti z hodin PRG; můj CHEATSHEET; u import random jsem použil dokumentaci PY popř. nějaký tutoral na internetu, jak to použít; pokud jsem si v nějakou chybou nevěděl rady (zhruba 2x si mi stalo), tak jsem použil ChatGPT, který mi vždy popsal chybu v kódu a ukázal mi, jak to přesně opravit, s touto pomocí už jsem chybu zvládl úspěšně opravit.

---FUNKCIONALITY---
 1) Zadání jména hráče
 2) XP systém - XP jsou za zabité enemy, ubírání XP jako penalizace
 3) Výběr zbraní za XP - lepší damage
 4) Hod kostkou při vstoupení na bojiště - po nějaké úrovni XP se vybírají enemy random
 5) Lektvar - poslední možnost záchranny při boji, skryté získání

---POCIT Z PROJEKTU---
Z celého kódu hry jsem velmi šťastný, že jsem dokončil takto "velký" projekt. Vše se mi povedlo, až na dvě funkce, které mi nefungovali kvůli True/False. Po vysvětlení bych to asi zvládl opravit a dodělat. Na funkčnost programu do nemá vliv, pouze je menší přehlednost v kódu. Celkově bych tedy toto označil jako ÚSPĚCH!
'''

# Import time a random
import time
import random

# Základní proměnné
rada = 0
lektvar = False
zbranVypsana = False
typBoje = 0
Wisboj = 0

# Začátek hry
jmenoHrace = input("Vítej dobrodruhu jak tě mám nazývat?:") #Zjištění/otázání se jména hráče

# Všechny entity
hrac = {
    "jmeno": jmenoHrace,
    "xp": 0,
    "hp": 100,
    "dmg": 10
}

enemy1 = { # Základní enemy - je na začátku
    "jmeno": "Krysa",
    "xp": 5,
    "hp": 10,
    "dmg": 5
}

enemy2 = { # Pokročilejší enemy, ale pořád lehčí
    "jmeno": "Zombie",
    "xp": 10,
    "hp": 20,
    "dmg": 10
}

enemy3 = { # Nejtěžší enemy
    "jmeno": "Louskáček",
    "xp": 20,
    "hp": 40,
    "dmg": 20
}

boss = { # Final boss/enemy, velmi těžký
    "jmeno": "Wisman",
    "xp": 999999999,
    "hp": 100,
    "dmg": 50
}

# Zbraně
Weapon1 = { # Základní zbraň
    "jmeno": "Meč",
    "xp": 10,
    "dmg": 10
}

Weapon2 = { # Lepší zbraň
    "jmeno": "PifPaf",
    "xp": 20,
    "dmg": 15
}

Weapon3 = { # Nejlepší zbraň, nutná pro poražení Bosse
    "jmeno": "Notebook",
    "xp": 30,
    "dmg": 50
}

# Herní cyklusy
hraJede = True # cyklus celkové hry
vesniceJede = False # cyklus vesnice
bojJede = False # cyklus boje

# Funkce vrátí jestli je entita naživu (True/False)
## Chtěl jsem to udělat do funkce, ale nešlo mi to. Ani to nevadí, protože to je v kódu pouze jednou. Samozřejmě by to ale bylo lepší ve funkci, kvůli přehlednosti kódu.

def resetEnemy(): # Funkce, která resetuje životy Enemy po každém cyklu hraJede
    enemy1['hp'] = 10
    enemy2['hp'] = 20
    enemy3['hp'] = 40
    boss['hp'] = 100

def obrana(): # Funkce, hod kostkou, jestli se hráč ubrání, nebo ne. Pokud ne, tak mu Enemy ubere životy
    padenapade = random.randint(1, 2)
    if padenapade == 1:
        print("Ubránil ses!")
    if padenapade == 2:
        print("Ani svatý Janko ti už nepomůže, neubránil ses!")
        #Výběr, s kterým Enemy hráč bojuje
        if typBoje == 1:
            hrac['hp'] = hrac['hp'] - enemy1['dmg']
        if typBoje == 2:
            hrac['hp'] = hrac['hp'] - enemy2['dmg']
        if typBoje == 3:
            hrac['hp'] = hrac['hp'] - enemy3['dmg']
        if typBoje == 4:
            hrac['hp'] = hrac['hp'] - boss['dmg']

def utok(): # Funkce, hráč dá dmg Enemy a Enemy dá dmg Hráči
    # Výběr, jaký typBoje je
    if typBoje == 1:
        hrac['hp'] = hrac['hp'] - enemy1['dmg']
        enemy1['hp'] = enemy1['hp'] - hrac['dmg']
    if typBoje == 2:
        hrac['hp'] = hrac['hp'] - enemy2['dmg']
        enemy2['hp'] = enemy2['hp'] - hrac['dmg']
    if typBoje == 3:
        hrac['hp'] = hrac['hp'] - enemy3['dmg']
        enemy3['hp'] = enemy3['hp'] - hrac['dmg']
    if typBoje == 4:
        hrac['hp'] = hrac['hp'] - boss['dmg']
        boss['hp'] = boss['hp'] - hrac['dmg']

def penal(): # Funkce, pokud hráč odejde z boje. Použito i u zdravotnice, která taky bere 5 XP za uzdravení
    hrac['xp'] = hrac['xp'] - 5

def addxp(): # Funkce, přidá hráči XP
    # Výběr, jaký typBoje je
    if typBoje == 1:
        hrac['xp'] = hrac['xp'] + enemy1['xp']
    if typBoje == 2:
        hrac['xp'] = hrac['xp'] + enemy2['xp']
    if typBoje == 3:
        hrac['xp'] = hrac['xp'] + enemy3['xp']
    if typBoje == 4:
        hrac['xp'] = hrac['xp'] + boss['xp']

def heal(): # Funkce, použito při uzdravení u zdravotnice
    hrac['hp'] = 100

def healLektvar(): # Funkce, použito při použití lektvaru od zdravotnice. Oproti heal() ještě bere hráči lektvar - lektvar = False
    hrac['hp'] = 100
    lektvar = False

# Začátek hry 2, celkový herní cyklus
while(hraJede):
    resetEnemy()
    print(f"Máš {hrac['hp']} HP, zbraň se sílou {hrac['dmg']} a {hrac['xp']} XP") # Vypsání takového "Summary"
    volba = input("Vyber akci: \n 1) Vesnice \n 2) Bojiště \n 0) rageQUIT") # input, kam hráč půjde, rageQUIT ukončí hru
    if volba == "1":
        print("Jdeš do vesnice...")
        time.sleep(2)
        vesniceJede = True # Zapnutí cyklusu vesnice
    if volba == "2":
        print("Jdeš na bojiště...")
        time.sleep(2)
        # Zjištění, jaký "level" má hráč podle XP
        if hrac['xp'] <= 10: # Pokud 10 a méně XP
            typBoje = 1 # Enemy bude Krysa (enemy1)
            bojJede = True # Zapnutí cyklusu boje
        elif hrac['xp'] > 40: # Pokud více než 40
            bojNebo = input("Můžeš jít na bosse, chceš? Nebo radši jít do normáního boje? \n 1) Boss \n 2) Normální boj") # Input v proměnné, otázka, zda hráč chce na Bosse, nebo na normální Enemy
            if bojNebo == "1": # Pokud 1, tak zapnutí boje s Bossem
                typBoje = 4
                bojJede = True # Zapnutí cyklusu boje
                print("Jdeš na Bosse Wismana... Good Luck!")
                time.sleep(2)
            if bojNebo == "2": # Pokud 2, tak zapnutí normálního Enemy
                typBoje = random.randint(1, 3) # Generace random čísla od 1 do 3 se dosadí do typBoje
                bojJede = True # Zapnutí cyklusu boje
        else: #hrac['xp'] > 10:
            typBoje = random.randint(1, 3) # Generace random čísla od 1 do 3 se dosadí do typBoje
            bojJede = True
    if volba == "0":
        print("Tak pápá")
        hraJede = False # Ukončení celé hry
    while(vesniceJede): # Cyklus vesnice
        print("Jsi ve vesnici EDUCAnet")
        vesVolba = input("Vyber akci: \n 1) Zdravotnice Šišková \n 2) Zbrojmistr Severa \n 0) Zpátky na rozcestí")
        if vesVolba == "1":
            print("Jdeš ke zdravotnici Šiškové...")
            time.sleep(2)
            sisVolba = input(f"Ahoj {hrac['jmeno']}, jak ti mohu pomoct? \n 1) Uzdravit \n 2) Rada do života \n 0) Odejít")
            if sisVolba == "1":
                heal()
                print("Jsi uzdraven za 5 XP!")
                penal()
                time.sleep(2)
            if sisVolba == "2":
                print("Chceš tedy radu jo?")
                time.sleep(1)
                rada = rada + 1 # Counter, kolik rad už bylo hráči řečeno
                if rada >= 3: # Zjištění, jestli hráč zažádal o 3 nebo více rad
                    if lektvar == True: # Pokud hráč už lektvar má
                        print("Dala bych ti lektvar, ale už jeden máš! Až ho mít nebudeš, tak se stav")
                    if lektvar == False: # Pokud lektvar ještě hráč nemá, tak se hráči dá lektvar
                        print("Celkem dost zde chodíš, tady máš lektvar na uzdravení. Můžeš ho použít během boje!")
                        lektvar = True
                        time.sleep(2)
                else: # Pokud hráč ještě nepožádal o 3 nebo více rad
                    print("Řeknu ti ji někdy později...")
                    time.sleep(1)
            if sisVolba == "3":
                print("Tak zase někdy příště!")
        if vesVolba == "2":
            print("Jdeš ke zbrojmistrovi Severovi...")
            time.sleep(2)
            sevVolba = input(f"Jak to jde {hrac['jmeno']}? Kdyby jsi nevěděl, tak máš {hrac['xp']} XP \n 1) Zbraně \n 0) Odejít")
            if sevVolba == "1":
                if Weapon3['dmg'] != hrac['dmg'] and hrac['xp'] >= Weapon3['xp']: # Ověření 1. jestli zbraň už hráč nemá 2. jestli hráč má dostatečně XP
                    print(f"2) {Weapon3['jmeno']}")
                    zbranVypsana = True
                if Weapon2['dmg'] != hrac['dmg'] and hrac['xp'] >= Weapon2['xp'] and Weapon3['dmg'] != hrac['dmg']: # Ověření 1. jestli zbraň už hráč nemá 2. jestli hráč má dostatečně XP 3. jestli hráč již nemá lepší zbraŇ
                    print(f"1) {Weapon2['jmeno']}")
                    zbranVypsana = True
                print("Tohle jsou všechny zbraně, které ti teď můžu nabídnout")
                time.sleep(1)
                if zbranVypsana == True: # Pokud byla vypnána nějaká zbraň, tak otázka
                    vyberZbrane = input("Jakou zbraň chceš? (0 pro žádnou)")
                    if vyberZbrane == "1":
                        print("Skvělá volba! Tímto sejmeš skoro všechno, co potkáš")
                        hrac['dmg'] = Weapon2['dmg']
                    if vyberZbrane == "2":
                        print("Výborně! Pro tebe ideální... třeba ti to pomůže i u Wismana")
                        hrac['dmg'] = Weapon3['dmg']
                    if vyberZbrane == "0":
                        print("Asi si tedy dost spokojen... Zatím!")
                time.sleep(1)
            if sevVolba == "0":
                print("Nezapoměň se vrátit pro nové zbraně!")
                time.sleep(1)
        if vesVolba == "0":
            print("Jdeš zpátky na rozcestí...")
            time.sleep(2)
            vesniceJede = False

    while(bojJede): # Cyklus boje
        # Zjištění, který typBoje byl zvolen a podle toho vypíše zprávu
        if typBoje == 1:
            print(f"Máš {hrac['hp']} HP a enemy {enemy1['jmeno']} má {enemy1['hp']} HP a sílu útoku {enemy1['dmg']}")
        if typBoje == 2:
            print(f"Máš {hrac['hp']} HP a enemy {enemy2['jmeno']} má {enemy2['hp']} HP a sílu útoku {enemy2['dmg']}")
        if typBoje == 3:
            print(f"Máš {hrac['hp']} HP a enemy {enemy3['jmeno']} má {enemy3['hp']} HP a sílu útoku {enemy3['dmg']}")
        if typBoje == 4:
            print(f"Máš {hrac['hp']} HP a Boss {boss['jmeno']} má {boss['hp']} HP a sílu útoku {boss['dmg']}")
            Wisboj = Wisboj + 1 # Protože chci, aby při každým cyklusu bojJede byla rochu jiná zpráva od Bosse, tak přidáváme 1 při každým cyklusu
            if Wisboj == 1:
                time.sleep(1)
                print("Co To ZnAmEnÁ?")
            if Wisboj == 2:
                time.sleep(1)
                print("Co To ReÁlNě ZnAmEnÁ???")
        volba = input("Vyber akci: \n 1) Útok \n 2) Obrana \n 0) Odejít")
        if volba == "1":
            print("Útočíš na enemy...")
            time.sleep(2)
            utok() # Volání funkce
        if volba == "2":
            print("Bráníš se, snad se ubráníš...")
            time.sleep(2)
            obrana() # Volání funkce
        if volba == "0":
            sure = input("Opravdu chceš odejít? Budeš za to mít penalizaci od svatého Janka! \n 1) ANO \n 2) NE")
            if sure == "1":
                bojJede = False # Zastavení cyklusu
                print("Odcházíš z boje... Svatý Janko je zklamán")
                penal() # Volání funkce
                typBoje = 0
                time.sleep(2)
            else:
                print("Jsem si myslel!")
        if hrac['hp'] <= 50 and lektvar == True: # Nabídnutí lektvaru, pokud má hráč méně nebo rovno 50 HP a pokud má lektvar dostupný
            lekVolba = input(f"Máš lektvar a {hrac['hp']} HP! Chceš ho využít? \n 1) ANO \n 2) NE")
            if lekVolba == "1":
                print("Využil jsi lektvar od zdravotnice Šiškové! Buď zdráv!")
                healLektvar() # Volání funkce
                time.sleep(2)
            if lekVolba == "2":
                print("Dobrá! Ale možná teď umřeš... sorry jako")
                time.sleep(2)
        if hrac['hp'] <= 0: # Tohle jsem chtěl dát do funkce, ale nefungovalo to, jinak: kontZivotH() - kontrola, zda hráč má méně nebo rovno 0 HP, pokud ano, ukončí se cyklus
            bojJede = False
            if Wisboj > 0: # Pokud je boss, tak to vypíše tuto zprávu
                print("Dostanete alespoň 10% za snahu")
                time.sleep(1)
            print("Zklamal jsi svatého Janka! Umřel jsi...") # Zpráva a ukončení cyklusu celkové hry - hráč zemřel
            hraJede = False
        if enemy1['hp'] <= 0 and bojJede == True or enemy2['hp'] <= 0 and bojJede == True or enemy3['hp'] <= 0 and bojJede == True or boss['hp'] <= 0 and bojJede == True: # Tohle jsem chtěl dát do funkce, ale nefungovalo to, jinak: kontZivotE - kontrola, zda enemy/boss má má méně nebo rovno 0 HP, pokud ano, ukončí se cyklus
                bojJede = False
                print("VÝHRA! Svatý Janko byl asi s tebou při boji")
                if Wisboj > 0: # Pokud je boss, tak to vypíše tuto zprávu a ukončí celkový cyklus hry - hráč hru DOHRÁL
                    print("Porazil jsi Wismana! Máš prezentaci bez chyby!!!")
                    hraJede = False
                addxp() # Volání funkce
                time.sleep(1)