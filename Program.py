from Jarat import Jarat
from InputOutput import Bemenet

'''vonat = Jarat("1000", "Budapest", "Bécs", "6")
vonat4 = Jarat("1000", "Budapest", "Bécs", "12")
vonat2 = Jarat("1001", "Budapest", "Debrecen", "12")
vonat3 = Jarat("1002", "Budapest", "Szeged", "18")

print(vonat.vonatinfo())
#print(vonat2.vonatinfo())
#print(vonat3.vonatinfo())
vonat.foglalas(18)

print("\n\nFoglalás után")
print(vonat.vonatinfo())
vonat.foglalas(6)
print(vonat.vonatinfo())
vonat.foglalas(50)'''

Bemenet.beolvas("input.txt")
for jarat in Bemenet.getJaratTomb():
    print(jarat)