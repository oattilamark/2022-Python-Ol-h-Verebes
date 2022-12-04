from Jarat import Jarat
from InputOutput import Bemenet

Bemenet.beolvas("bemenet.txt")
for jaratInfo in Bemenet.getJaratInfoTomb():
    print(jaratInfo)

for jarat in Bemenet.getJaratTomb():
    print(jarat.vonatinfo())
    #print(jarat.getJaratszam())
    #print(jarat.getHova())

#A szegedi vonatra lefoglalunk 20 helyet, nézzük változik-e a táblázat
    if (jarat.getJaratszam() == "1069"):
        jarat.foglalas(20)
    
        print("\nFoglalás után:")
        print(jarat.vonatinfo())
    
#