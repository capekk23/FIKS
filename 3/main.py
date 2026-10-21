#3!
import numpy as np

def main():
    k = 2
    n = np.array([7, 9, 6, 3, 5, 4])
    vysledek = 0

    print(n)

    for i in range(len(n)):
        if i >= k:
            # print(np.lib.stride_tricks.sliding_window_view(n, i))
            s = np.lib.stride_tricks.sliding_window_view(n, i)
            v =  np.sort(s)
            # print("sorted: " + str(v))
            for j in v:
                for m in range(len(j)):
                    print(str(j[m]) + " @ " + str(m))



    
    # for i in range(len(n)): 
    #     s = np.array(n[i:i+k]) #subarray pro minimalne velke substringy
    #     if len(s)==k: # jen pokud je substring velky jako minimalni pocet znaku, bereme ho. 
    #         print(s)
    #         max = np.max(s)
    #         min = np.min(s)
    #         if (max - min) == k-1:
    #             vysledek += 1

        
            
    #         min = 1000000000
    #         max = 0


            # Protoze ja nehledam jen nejmensi zakladni. Ja hledam veskere subarrays, v kterych je k pocet cislic za sebou, unordered. 
            # To takhle nikdy neudelam
            # Ja potrebuju kontrolovat vsecky. 
            # To znamena zacit od nejmensich a jit po vetsi a vetsi arrays.
            # Coz da ale crazy runtimes prolly.
            # Ale pokud to nenapisu, jak to muzu vedet?
            # Urcite.
            # Ma na tohle neco numpy?

            


        
    print("vysledek: " + str(vysledek))


# 7 9 6 3 5 4
# 1 1 1 1 1 1 1 1 1 1

main()