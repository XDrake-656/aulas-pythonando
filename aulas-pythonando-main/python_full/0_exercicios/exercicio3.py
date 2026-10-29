number = int(input())
survavors = [i for i in range(1,number + 1)]
pos = 1
while len(survavors) != 1:
    survavors.remove(survavors[pos])
    pos += 1
    if pos == len(survavors):
        pos = 0
    elif pos > len(survavors):
        pos = 1
        
print(survavors[0])
