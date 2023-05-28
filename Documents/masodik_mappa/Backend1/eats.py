#Nested loops -4.feladat- person eats in restaurant 
persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican",
"French"]

for i in range(0,4):
    for j in range(0,4):
        print(i+1,'.',persons[i], 'eats',restaurants[j])  
        