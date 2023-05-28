#sites_new-ban a weboldalak mérete összesen
#Házi feladat  -Python webstatistics 1.Feladat
import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
empty_sites = 0

for index in range(0, len(sites_new)):
    print(sites_new[index]['domain'], sites_new[index]['size'],sites[index]['size'] )
    
    sum = sum + sites_new[index]['size']
    
    
sum_GB = round(sum/(len(sites_new))/1024, 2)
    
print('Total size is:', round(sum/1024, 2), 'GB')
print('Average site size is:', round(sum/(len(sites_new))/1024, 2), 'GB')
      
