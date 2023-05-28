#Python függvények 1.feladat 7-tel osztható de 5-tel nem 
nums = [3,4,9,6,2]
a = [] 
k = 2000
v = 3200
i = 0

for i in range(k,v):
      if (i % 7 == 0):
 #           print(i,": osztható 7-tel") 
            if (i % 5 != 0):
                print(i," osztható 7-tel, nem osztható 5-tel")
#     else: 
#         print(i,": nem  osztható")
    