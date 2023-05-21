def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod 
    
print(f'Pole i obwod trójkąta wynosza: {trojkat(10,15,12,8)}')

# trapez

def trapez(bok_a, bok_b, bok_c, h_a):
    pole = 1/2 * (bok_a + bok_b) * h_a
    obwod = bok_a + bok_b + 2 * bok_c
    return pole, obwod

print(f'Pole i obwod trapeza wynosza: {trapez(10, 8, 6, 3)}')

# rownoległobok

def rownoleglobok(bok_a, bok_b, h_a):
    pole = bok_a * h_a
    obwod = 2 * bok_a + 2 * bok_b 
    return pole, obwod

print(f'Pole i obwod wynosza rownolegloboku: {rownoleglobok(7, 12, 5)}')


