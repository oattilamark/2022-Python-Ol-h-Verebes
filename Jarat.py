class Jarat:
    def __init__(self, jaratszam, indulas_hely, erkezes_hely, indulas_ido):
        self.jaratszam = jaratszam
        self.indulas_hely = indulas_hely
        self.erkezes_hely = erkezes_hely
        self.indulas_ido = indulas_ido
        self.ferohely = 48
        self.szabad = 48
        self.foglalt = 0

    def tulfoglalt(self, darab):
        # Ha a foglalandó darabszám eléri vagy meghaladja a szabad férőhelyek számát :Igaz - túlfoglalt
        if (self.szabad <= darab):
            return True
        else:
        # Ha nem haladja meg, akkor van még foglalható hely
            return False

    def foglalas(self, darab):
        # Ha van még lefoglalható hely:
        if (self.tulfoglalt(darab) == False):
            self.foglalt += darab
            self.szabad = (self.ferohely - self.foglalt)
        else:
            #nemLefoglalhato = darab-self.szabad
            self.szabad = 0

    def vonatinfo(self):
        return f"{self.jaratszam:<8}{self.indulas_hely:<20}{self.erkezes_hely:<20}{self.indulas_ido:<20}{self.ferohely:<3}{self.foglalt:<3}{self.szabad:<3}"
    
    #jaratszam, indulas_hely, erkezes_hely, indulas_ido
    def getJaratszam(self):
        return self.jaratszam
    def getHonnan(self):
        return self.indulas_hely
    def getHova(self):
        return self.erkezes_hely
    def getMikor(self):
        return self.indulas_ido
    def getFerohely(self):
        return self.ferohely
    def getFoglalt(self):
        return self.foglalt
    def getSzabad(self):
        return self.szabad
    