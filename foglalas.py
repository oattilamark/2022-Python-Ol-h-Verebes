# Budapest - Debrecen (egyirányú)
# Budapest - Bécs (egyirányú)
# Budapest - Szeged (egyirányú)

# 1 nagy kocsi, 12asztal, 1asztal 4fő = 48férőhley

#jegyar = 4000

#! Választás
#! Kiindulási pont: Budapest
#! Cél: Bécs, Debrecen, Szeged
#! Időpont: Reggel 06:00, délben 12:00, este 18:00

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
            #!teszt
            #print("foglalható:", self.szabad)
            #print("lefoglalt:", self.foglalt)
            #print("most szeretné lefoglalni:", darab)

            self.foglalt += darab
            self.szabad = (self.ferohely - self.foglalt)

            #print("ezután szabad:", self.szabad)
        else:
            #TODO Ha nincs elég szabad hely akkor felajánlja hogy lefoglalja-e az elérhető helyeket (kevesebb mitn amit szeretne) vagy megjeleníti a következő vonatot 
            print(f"A vonaton {self.szabad} szabad hely volt, de {darab}-et szeretett volna lefoglalni. A nem lefoglalt {darab-self.szabad}db jegyet visszatérítjük")
            self.szabad = 0

    def vonatinfo(self):
        return f"""Indulás\t\tÉrkezés\t\tIndulási idő\tFérőhely\tFoglalt\tSzabad
{self.indulas_hely}\t{self.erkezes_hely}\t\t{self.indulas_ido}\t\t{self.ferohely}\t\t{self.foglalt}\t{self.szabad}
        """


vonat = Jarat("1000", "Budapest", "Bécs", "6")
vonat4 = Jarat("1001", "Budapest", "Bécs", "12")
vonat2 = Jarat("Budapest", "Debrecen", "12")
vonat3 = Jarat("Budapest", "Szeged", "18")

print(vonat.vonatinfo())
#print(vonat2.vonatinfo())
#print(vonat3.vonatinfo())
vonat.foglalas(18)

print("\n\nFoglalás után")
print(vonat.vonatinfo())
vonat.foglalas(6)
print(vonat.vonatinfo())
vonat.foglalas(50)