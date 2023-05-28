#Ciklusok, függvények 3.feladat -elem osszes tipusa
x = ['', 4, True]

a = []

for i in range(0,3):
    if type(x[i]) is int:
        a.append('integer')
    elif type(x[i]) is str:
        a.append('string')
    elif type(x[i]) is bool:
        a.append('boolean')
        
#for i in range(0,3):
if i == 2:
    print(a)

# ['string','integer','boolean']