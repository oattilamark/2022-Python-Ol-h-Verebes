from Jarat import Jarat
#ELÉG LESZ tagolva elmenteni, nem kell többdimenziós tömb
class Bemenet():
    global jaratTomb
    jaratTomb = []

    @staticmethod
    def beolvas(fajlnev):
        try:
            with open(fajlnev, "r", encoding="utf-8") as bemenet:
                elsoSor = bemenet.readline()

                while True:
                    info = []       #Járatszám, Honnan, Hová
                    r = []          # Reggel, Foglalt, Szabad
                    d = []          # Délben, Foglalt, Szabad
                    e = []          # Este, Foglalt, Szabad

                    jaratDb = 0
                    for x in range(0,5):
                        sor = bemenet.readline().strip()
                        adat = sor.split(";")
                            
                        if (x < 4):
                            if (len(adat) == 3):
                                    info.append(adat)
                            elif (len(adat) == 2):
                                if (x == 1):
                                        r.append(adat)
                                elif (x == 2):
                                        d.append(adat)
                                elif (x == 3):
                                        e.append(adat)
                            elif (adat[0] == ":"):
                                print("ÚJ NAP")

                        x += 1

                        print(f"{x-1}sor {adat}")

                    if not sor:
                        break
                    jaratTomb.append(info + r + d + e)

                '''for sor in bemenet:
                    adat = sor.strip()

                    if(adat != ":"):                                            #NAP FOLYAMATBAN
                    
                    #EGY ADOTT JÁRAT BLOKKJA
                        #jarat = [["", "", ""], ["", ""], ["", ""], ["", ""]]

                        if(adat != "."):
                            tomb = adat.split(";")
                            
                            if (len(tomb) == 3):
                                #jarat[0]
                                i = 0
                                for elem in tomb:
                                    jarat[0][i] = tomb[i]
                                    i+=1

                                #print(jarat)
                            elif (len(tomb) == 2):

                                #jarat[1],2,3
                                #jarat[1][0] = tomb[0]
                                #jarat[1][1] = tomb[1]
                                line = 0
                                szoveg = ""
                                for elem in tomb:
                                    if (line % 2 == 0):
                                        szoveg = tomb
                                    else:
                                        szoveg = szoveg + tomb

                                    print(szoveg)
                                    line += 1
                        else:
                            #print(jarat)
                            print()
                    else:                                                       #NAP VÉGE
                        #Listához adás
                        jarat.clear()
                        print()'''
        except FileNotFoundError:
            print("A megadott forrásfájl nem található")
            exit()

    @staticmethod
    def getJaratTomb():
        return jaratTomb