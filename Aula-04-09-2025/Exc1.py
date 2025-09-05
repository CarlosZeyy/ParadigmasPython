import random 

t1, t2, t3 = random.randint(0, 100)

print(t1)
print(t2)
print(t3)

nota_final = (t1 * 0.2) + (t2 * 0.3) + (t3 * 0.5)

print(round(nota_final, 2))