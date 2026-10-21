#3!
import numpy as np


def main():
    k = 3
    n = np.array([5, 1, 3, 4, 2])
        # 1 000 000 000
    min = 1000000000
    max = 0
    vysledek = 0

    print(n)
    
    for i in range(len(n)): 
        s = n[i:i+k] #subarray pro minimalne velke substringy
        if len(s)==k: # jen pokud je substring velky jako minimalni pocet znaku, bereme ho. 
            print(s)
            # takze mam substrings velke jako nejmensi
            # co ted?
            # mohl bych u nich jít try +1 na obě strany, postupně? nejdív right a pak left? Prolly not
            # jinak, MÁM ty base nejmenší substrings, potřebuju zjistit kolik je mezi nima místa a na
            # tom pak přičítat shit to them
            # takže potřebuju uložit start pozici subarraye, což je i. (i + k dá konec)
            # uložit všechny do nového arraye.
            # a s tím poíčtat mezery mezi nimi. 
            # Yup. Nice
        
    print("vysledek: " + str(vysledek))


# 7 9 6 3 5 4
# 1 1 1 1 1 1 1 1 1 1

# proste jit od nejmensich k, a pak pricitat 1, nejmensi neni treba sortovat, vetsi asi ano. Pak uz je to easy/ surely...

main()