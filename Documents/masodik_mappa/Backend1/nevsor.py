student = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']
x=sorted(student)
r=len(student)
l=int(r/2)

print(x)
print("Diákok száma:",r)
print("Csoport létszám:",l)
print("\n1.csoport")
for i in range(0,l):
    print(x[i])
print("\n2.csoport")
for i in range(l,r):
    print(x[i])
 
                