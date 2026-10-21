#3!
import numpy as np

def main():
    k = 2
    n = np.array([7, 9, 6, 3, 5, 4])
    vysledek = 0
    zasebou = 0

    print(n)

    for i in range(len(n)):
        if i >= k:
            # print(np.lib.stride_tricks.sliding_window_view(n, i))
            s = np.lib.stride_tricks.sliding_window_view(n, i)
            # print(s)
            
            v =  np.sort(s)
            
            # print("sorted: " + str(v))

            for j in v:  # pro kazdy array serazenych subarrayu
                # print("j: " + str(j))
                
                for m in range(len(j)):     # pro kazdy index v serazenem subarray
                    
                    print("\n" + str(j))
                    print(j[m])

                    try:
                        if j[m + 1] - j[m] == 1:    # jestli number[i+1] - number[i] se rovna 1, to znamena jsou za sebou, pricte se mezivysledek +1
                            zasebou += 1            # zasebou znamena, kolik cisel je prave za sebou
                            print(j[m + 1] - j[m])  # toto funguje.

                        elif zasebou >= 2:      # pokud je zasebou Vetsi, nebo rovno poctu cisel za sebou ktery hledam, vysledek je +1 pro ten subarray
                            vysledek += 1       # subarray je uspesne solved
                            zasebou = 0         # vyresetuji counter prubezneho souctu za sebou
                            print("elif")
                            break               # breaknu loop pro tento subarray?
                        
                        else:                   #pokud ale nejsou za sebou, je prerusena rada
                            print("else")
                            zasebou = 0
                    
                    finally:
                        continue


                    
                

    
               
    vysledek += 1 # muj vysledek je momentalne OFF BY ONE, pro vcely array, staci pricist 1 a mam to.      
    print('\n' + "vysledek: " + str(vysledek))

main()