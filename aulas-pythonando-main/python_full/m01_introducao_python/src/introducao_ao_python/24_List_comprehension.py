x = [i for i in range(10)] #List comprehension
print(x)

y = []
for i in range(10): #forma tradicional
    y.append(i)
print(y)

z = [i for i in range(10) if i > 4] #List comprehension com if
print(z)

w = []
for i in range(10): #forma tradicional
    if i > 4:
        w.append(i)
print(w)
