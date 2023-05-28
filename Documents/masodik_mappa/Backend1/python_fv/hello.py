#python függvények -3.Feladat

# Ask a number, then convert it to number and print the hello string, as many times  as 
# reach the number and increase the line number  
# 

#def convert_to_number(text)
def print_hello(count):
    print(count,'Hello')

szam = input('Kérek egy számot!')
db = int(szam)

for i in range(1,db+1):
    print_hello(i)