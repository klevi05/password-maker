import random


vector = []
password = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','?','1','2','3','4','5','6','7','8','9']
for i in range(0,12):
    n = random.randint(0,35)
    if n != vector:
        vector.append(n)
    else:
        vector.append(n)
for j in range(0,12):
    var = vector[j]
    for b in range(0,35):
        if var == b:
            password.append(letters[b])
for c in range(0,len(vector)):
    print(password[c],end='')
