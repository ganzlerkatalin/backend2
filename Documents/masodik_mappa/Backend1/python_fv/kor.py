#Python függvények 4.Feladat - Kör kerület és terület számítás
from math import pi

#def kerulet(szam)
 #  # kerulet = 2 * db * pi
 #   return 2 * db * pi

szam = input('Kérem a kör sugarát!')
r = int(szam)

kerulet = 2*r*pi
terulet = r*r*pi

print("Kör kerülete: ",kerulet)
print("Kör területe: ",terulet)

