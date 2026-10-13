import time
import numpy as np
# Vstup
# 1         číslo 1–8, znamená kolikrát 3 radky pod nim budou
# 4 3       m stanic, q skútrů
# 5 2 4 1   spotreba na stanicich ––– vzdálenost
# 10 4 12   pocatecni palivo skutru ––– dojezd
# Výstup
# 6

# Máme 4 stanice a 3 skútry:
# • první skútr projede 2 stanice (5 + 2 = 7 ≤ 10), ale ke třetí už nepřijede (5 + 2 + 4 = 11 > 10)
# • druhý skútr nepřijede ani k první stanici
# • třetí skútr navštíví všechny 4 stanice
# Skútry navštívily celkem 2 + 0 + 4 = 6 stanic.


vstup = []
with open("2/input.txt") as f:
    for x in f:
        vstup.append(x)

vstupNP = np.array([vstup])

def main():
    x = 0
    output = 0
    r = 2
    r = int(vstup[0])   #mám r = 1-8 pro počet zadání
    for n in range(r):      
        p = n + 1                   # gotta avoid that off by one         
        vzdalenosti = vstup[(3 * p) - 1]    #načtu si správné řádky pro vzdálenost a dojezd, jsou to indeed proste jen nasobky 3
        dojezd = vstup[3 * p]

        vzdalenosti_var = vzdalenosti.split(' ')         #ulozim do listu jen hodnoty bez mezer
        vzdal_list = np.array([int(n) for n in vzdalenosti_var])   #prevedu je na INT
        dojezd_v = dojezd.split(' ')                    #rinse and repeat
        dojezd_list = np.array([int(n) for n in dojezd_v])

        cumsumA = np.cumsum(vzdal_list)
        vysledek = np.searchsorted(cumsumA, dojezd_list[n], 'left')


        for i in dojezd_list:                   # pro kazdej skútr check:
            for z in range(len(vzdal_list)):    # z je 0 - max index vzdáleností
                x += vzdal_list[z]              # k x přičtu aktuální vzdálenost   
                if x > i:                       # pokud je soucet vzdalenosti vetsi nez aktualní dojezd
                    x = 0                       # nastav x na 0
                    break                       # break, protoze prvni hodnota je diskvalifikujici
                else:                           # pokud je soucet mensi nebo roven vzdalenosti
                   output += 1                 # output se rovná + 1 pro tu stanici, kterou projedu

        print(output)
        output = 0    
        vysledek = 0

main()
