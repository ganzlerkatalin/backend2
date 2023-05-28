nevsor = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

print('\n1.Feladat:User generálás')
for index in range(0, len(nevsor)):
    vezeteknev = nevsor[index][0]
    keresztnev = nevsor[index][0]
    print('name:',nevsor[index],',')
#   print('email:',nevsor[index],',')
    print('email:',nevsor[index][0]+'.'+nevsor[index][1]+"@company.hu"',')
#   print('password:',nevsor[index],',')
    print('password:',nevsor[index][0]+"123Start",',')
    print("")
    
    