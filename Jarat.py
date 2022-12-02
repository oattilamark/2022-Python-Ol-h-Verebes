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
        return f"""Indulás\t\tÉrkezés\t\tIndulási idő\tFérőhely\tFoglalt\tSzabad
{self.indulas_hely}\t{self.erkezes_hely}\t\t{self.indulas_ido}\t\t{self.ferohely}\t\t{self.foglalt}\t{self.szabad}
        """
        