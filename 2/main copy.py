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
    výsledek = 0
    r = 2 
    r = int(vstup[0])   #mám r = 1-8 pro počet zadání
    for n in range(r):      
        n += 1 # gotta avoid that multiplication by 0    
        #Pro každé zadání si načtu správný řádek    
        vzdalenosti = vstup[(3 * n) - 1]    #načtu si správné řádky pro vzdálenost a dojezd, jsou to indeed proste jen nasobky 3 a 3-1
        dojezd = vstup[3 * n]

        vzdalenosti_var = vzdalenosti.split(' ')                        # ulozim do listu jen hodnoty bez mezer
        vzdal_list = np.array([int(n) for n in vzdalenosti_var])   # prevedu je na INT
        dojezd_var = dojezd.split(' ')                                  # rinse and repeat
        dojezd_list = np.array([int(m) for m in dojezd_var])


        #cumulative sum  vzdáleností
        cumsumA = np.cumsum(vzdal_list)
        #print("cumsum: " + str(cumsumA))
        debug = []
        #print()
        for i in range(len(cumsumA)):
            debug.append(i)
        #print("debug indexes of cumsums: " + str(debug))

        #print()
        #print("dojezd: " + str(dojezd_list))
        #print()

        # pro každý dojezd kazdeho skutru
        for i in range(len(dojezd_list)):
            step = np.searchsorted(cumsumA, dojezd_list[i], 'right')
            # cumsum[i-1] <= dojezd_list[n] < cumsum[i]
            #print("index where dojezd goes: " + str(step) + " | dojezd val: " + str(dojezd_list[i]))
            výsledek += step
            
        #print("výsledek: " + str(výsledek))
        #print()
        print(výsledek)
        step = 0
        výsledek = 0


# 6
# 5178
# 125292
# 526005
# 1997322
# 12387321
# 49915776

# 6
# 5178
# 125292
# 526005
# 1997322
# 12387321
# 49915776
# 1199140091700


main()

# For some unexplicable reason je #2 a #8 špatně. Nějak? Ale jak?
# Můj originál je ale dobře pro #2 a #8 nedopočítá?
# Mohl bych zkusit to bruteforcnout? Jakože udělám cumsum a pak misto searchsorted to projedu for loopem?