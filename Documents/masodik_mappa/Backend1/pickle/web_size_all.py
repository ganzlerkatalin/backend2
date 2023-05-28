#sites_new-ban a weboldalak mérete összesen
#Házi feladat  -Python webstatistics 1.Feladat
import pickle

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

print("Python web statistics\n")
print("1.Feladat össz weboldal együttesen foglalt területe GB-ban és átlagos weboldal méret")
sum = 0
empty_sites = 0

for index in range(0, len(sites_new)):
#    print(sites_new[index]['domain'], sites_new[index]['size'])
    if(sites_new[index]['size'] == 0):
        empty_sites = empty_sites + 1
    sum = sum + sites_new[index]['size']
    
    
sum_GB = round(sum/(len(sites_new))/1024, 2)

#1.Feladat - Oldalak összmérete és átlaguk     
print('Total size is:', round(sum/1024, 2), 'GB')
print('Average site size is:', round(sum/(len(sites_new))/1024, 2), 'GB')

#3.Feladat- üres site száma a sites_new tömbben
print("\n3.Feladat Üres site-ok száma:")
print('there are', empty_sites, 'empty sites')      

#4.Feladat
#Kiírja az összes weblap méretét- sites_new méret kivéve ha 0. Egyébként ha nagyobb 
# mint 1024 MB akkor átszámítja GB-ba (/1024) egyébként MB-ban marad.

#for index in range(0, len(sites_new)):
 #   if(sites_new[index]['size'] == 0):
    # nothing
 #   elif(sites_new[index]['size'] < 1024):
# print(sites_new[index]['domain'], sites_new[index]['size'])
 #   elif(sites_new[index]['size'] > 1024)():
 #       print(sites_new[index]['domain'], round(sites_new[index]['size']/1024,2), 'GB')
   
    
    
    

