from Jarat import Jarat

class Bemenet():
    global jaratInfoTomb
    jaratInfoTomb = []
    global jaratTomb
    jaratTomb = [Jarat]

    @staticmethod
    def beolvas(fajlnev):
        try:
            with open(fajlnev, "r", encoding="utf-8") as bemenet:
                jaratInfoTomb.clear()
                jaratTomb.clear()
                elsoSor = bemenet.readline()

                #A fájl szerekezete szerint "elvágom" a # karakternél ami elkülöníti a járatok alapinformációit a lefoglalt helyek számától
                adat = bemenet.read().split("#")

                jaratInfo = adat[0].strip()
                jaratInfo = jaratInfo.split()

                #A járatokat eltárolom, később jól jöhet egy ilyen lista
                jaratInfoTomb.append(jaratInfo)

                jarat = adat[1].strip()
                jarat = jarat.split()

                #Itt pedig megszabadítom az adatot a másik információs szövegtől, úgy hogy azt a sort (0.) nem járom be
                #Valamint eltárolom az adatokat
                for j in range(1, len(jarat)):
                    #Kifutok a változónevekből :D járat a magánhangzók nélkül
                    jrt = jarat[j].split(";")

                    #Mondom..
                    ujJarat = Jarat(jrt[0], Bemenet.getHonnanByID(jrt[0]), Bemenet.getHovaByID(jrt[0]), "")

                    #print(ujJarat.vonatinfo())
                    jaratTomb.append(ujJarat)

        except FileNotFoundError:
            print("A megadott forrásfájl nem található")
            exit()

    @staticmethod
    def getJaratInfoTomb():
        return jaratInfoTomb
    
    @staticmethod
    def getJaratTomb():
        return jaratTomb

    @classmethod
    def getHonnanByID(cls, azonosito):
        x = 0
        for jarat in jaratInfoTomb[0]:
            j = jarat.split(";")

            if (j[0] == azonosito):
                x = j[1]
        return x

    @classmethod
    def getHovaByID(cls, azonosito):
        x = 0
        for jarat in jaratInfoTomb[0]:
            j = jarat.split(";")

            if (j[0] == azonosito):
                x = j[2]
        return x