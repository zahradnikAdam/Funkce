def obvod(a, b, c):
    return a + b + c
 
def obsah_trojuhelniku(a, b):
    return 0.5 * (a * b)
 
volba = input("Co chcete spočítat? Vyberte 'obvod' nebo 'obsah': ")
 
if volba == 'obvod':
    strana_a = int(input("Zadejte délku strany a: "))
    strana_b = int(input("Zadejte délku strany b: "))
    strana_c = int(input("Zadejte délku strany c: "))
    vysledek = obvod(strana_a, strana_b, strana_c)
    print("Obvod trojúhelníku je:", vysledek)
elif volba == 'obsah':
    strana_a = int(input("Zadejte délku základny trojúhelníku: "))
    strana_b = int(input("Zadejte délku výšky trojúhelníku: "))
    vysledek = obsah_trojuhelniku(strana_a, strana_b)
    print("Obsah trojúhelníku je:", vysledek)
else:
    print("Neplatná volba.")