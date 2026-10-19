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
            # hledam rozdil mezi nejvetsim a nejmensim cislem v k sized subarray, coz ale neni idealni reseni a mel bych to zahodit.                       
            for x in s: 
                if x > max:
                    max = x
                if x < min:
                    min = x
                print("max: " + str(max))
                print("min: " + str(min))
                if (max - min) == k-1:
                    print("ted se to scita")
                    vysledek += 1
            min = 1000000000
            max = 0
        
    print("vysledek: " + str(vysledek))


# 7 9 6 3 5 4
# 1 1 1 1 1 1 1 1 1 1

# proste jit od nejmensich k, a pak pricitat 1, nejmensi neni treba sortovat, vetsi asi ano. Pak uz je to easy/ surely...

main()