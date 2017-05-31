def normalize(name):
    def lowerC(ch):
        if not ch.islower():
            ch.lower()
        return ch
    
    return list(map(lowerC, name))

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)