#sites_new-ban a weboldalak mérete összesen
#Házi feladat  -Python webstatistics 1.Feladat
import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
empty_sites = 0

print('2.Feladat')

for index in range(0, len(sites_new)):
   # print(sites_new[index]['domain'], sites_new[index]['size'],sites[index]['size'] )
    if((sites_new[index]['size']) != (sites[index]['size'])):
        kulonbseg = sites_new[index]['size'] - sites[index]['size']
        valtozas = round(kulonbseg/(sites_new[index]['size']/100),2)
       # print(sites_new[index]['domain'], sites_new[index]['size'],sites[index]['size'])
        print(sites_new[index]['domain'],"changed by:", valtozas)
    if(sites_new[index]['size'] == 0):
        empty_sites = empty_sites + 1
    sum = sum + sites_new[index]['size']
    
    
sum_GB = round(sum/(len(sites_new))/1024, 2)
    
print('\n1.Feladat:')    
print('Total size is:', round(sum/1024, 2), 'GB')
print('Average site size is:', round(sum/(len(sites_new))/1024, 2), 'GB')
      
print('\n3.Feladat:')
#3.Feladat- üres site száma a sites_new tömbben
print('there are', empty_sites, 'empty sites') 

print('\n4.Feladat:')
for index in range(0, len(sites_new)):
       # print(sites_new[index]['domain'], sites_new[index]['size'],sites[index]['size'] )
    if((sites_new[index]['size']) != 0):
        if(sites_new[index]['size'] > 1024):
            print(sites_new[index]['domain'],round(sites_new[index]['size']/1024,2),"Gb")
        if(sites_new[index]['size'] < 1024):
            print(sites_new[index]['domain'],round(sites_new[index]['size'],2),"Mb")
       # kulonbseg = sites_new[index]['size'] - sites[index]['size']
       # valtozas = round(kulonbseg/(sites_new[index]['size']/100),2)
       # print(sites_new[index]['domain'], sites_new[index]['size'],sites[index]['size'])
       # print(sites_new[index]['domain'],"changed by:", valtozas)
    #if(sites_new[index]['size'] == 0):
     #   empty_sites = empty_sites + 1
    #sum = sum + sites_new[index]['size']