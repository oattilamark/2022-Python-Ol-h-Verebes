from Jarat import Jarat

class Bemenet():
    global napTomb
    global jaratTomb
    global jarat

    napTomb=[]
    jaratTomb = []
    jarat = [["", "", ""], ["", ""], ["", ""], ["", ""]]

    @staticmethod
    def beolvas(fajlnev):
        try:
            with open(fajlnev, "r", encoding="utf-8") as bemenet:
                elsoSor = bemenet.readline()
                
                for sor in bemenet:
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
                            else:
                                #jarat[1],2,3
                                #jarat[1][0] = tomb[0]
                                #jarat[1][1] = tomb[1]

                                segedlista = []
                                for x in range(1,4):
                                    jarat[x] = tomb
                                
                        else:
                            print(jarat)
                    else:                                                       #NAP VÉGE
                        #Listához adás
                        jarat.clear()
                        print()
        except FileNotFoundError:
            print("A megadott forrásfájl nem található")
            exit()

    @staticmethod
    def getJaratTomb():
        return jaratTomb

    @staticmethod
    def getNapTomb():
        return napTomb