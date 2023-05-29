#Python függvények 4.Feladat - Kör kerület és terület számítás
from math import pi

def kor_kerulet(radius):
   return 2*radius*pi

def kor_terulet(radius):
    return radius * radius * pi

r = int(input('Kérem a kör sugarát!'))

kerulet = kor_kerulet(r)
terulet = kor_terulet(r)

print(f'Kör kerülete: {kerulet}')
print(f'Kör területe: {terulet}')

