# Vstup začíná řádkem s číslem t ≤ 500, což je počet zadání. Každé zadání je tvořeno dvěma řádky. Na
# prvním řádku zadání jsou celá čísla n, x, y, bd, bu, bl, br, kde n je počet vstupů (0 ≤ n ≤ 20 000), x a y
# jsou počáteční souřadnice (−106 ≤ x, y ≤ 106) a bd, bu, bl, br je dolní hranice, horní hranice, levá hranice,
# pravá hranice (−106 ≤ bd, bu, bl, br ≤ 106). Všechny tyto hranice jsou neostré. Na druhém řádku zadání
# je n mezerou oddělených instrukcí (R, L, U, D), které máš vykonat. Souřadnicový systém má počátek
# v levém dolním rohu. Je zaručeno, že počáteční souřadnice je uvnitř zadaných hranic.


#dostanu číslo <= 500 to jest počet zadání
#zadání = 2 řádky
#   1. řádek = má n, x, y, bd, bu, bl, br, kde:
#   n je počet vstupů od 0 do 20 000
#   x a y jsou počáteční souřednice ( -106 <= x, y <= 106)
#   bd, bu,bl, br jsou hradnice, down, up, left a right a jsou take -106 <= d, u, l a right <= 106
#   hranice jsou neostré, takže some fucking bullshit
#   
#   druhý řádek obsahuje n mezerou oddělených instrukcí, R, L, U, D, které máš vykonat
#   souřadnicový systém má počátek v levém dolním rohus
import time

vstup = []

f = open("1/1.1/1.2/input.txt")

with open("1/1.1/1.2/input.txt") as f:
    for x in f:
        vstup.append(x)


zdi_a = []
pos_a = ()
step = []
tmp = []
num_list_a = []
steps_list_a = []

current = 2





try:
    f = open("output.txt", "x")
except:
    print("uz existuje soubor, prepisuje se")


def main():
    slice = []
    tmp = []
    
    for z in range(1000):          #z ma range 0-499 a jsou to indexy radku vstupu
        if not z % 2 == 0: #Toto vrati jen "1. radek"
            #beru z co jsou lichá čísla right
            print("toto je Z: " + str(z))
            print("slice cislo:" + str(z))
            slice.append(vstup[z])
            slice.append(vstup[z+1])
            print(slice)

        
            tmp = slice
            print("toto je tmp: " + str(tmp))

            #reseni RADKU 1
            x = tmp[0] #nactu si prvni hodnotu z tmp, coz je prvni radek obsahujici moje cisla
            num_list_a = x.split(' ') #ulozim do listu jen hodnoty bez mezer
            int_values = [int(n) for n in num_list_a] #prevedu je na INT
            int_values = int_values[1:] #odstranit prvni value, coz je jen pocet kroku, useless
            pos = int_values[0:2]   #ulozim si je do lepcich variables, POS jsou prvni 2 hodnoty
            zdi_a = int_values[2:]  #Zdi jsou hodnoty od 2
            print("toto jsou zdia: " + str(zdi_a))

            #reseni RADKU 2
            y = tmp[1]		#nactu druhou value z listu temporary, ktera obsahuje jen DWLR instrukce
            steps_list_a = y.split(' ')		#rozdelim je na mezerách, ulozim do listu jednotlive hodnoty
            steps_list_a.remove(steps_list_a[-1]) 	#odeberu newline charakter (posledni value v listu)
            print("toto je step lista: " + str(steps_list_a))

            print("toto je POS: " + str(pos))
            #samotny algoritmus, go up, down, left, right, pokud nenarazis do zdi
            for v in steps_list_a:
                if v == 'U': #go 1 up
                    if pos[1] + 1 <= zdi_a[1]:
                        pos[1] += 1
                if v == 'D': #go 1 down
                    if pos[1] - 1 >= zdi_a[0]:
                        pos[1] -= 1
                if v == 'R': #go 1 right
                    if pos[0] + 1 <= zdi_a[3]:
                        pos[0] += 1
                if v == 'L': #go 1 left
                    if pos[0] -1 >= zdi_a[2]: 
                        pos[0] -= 1
            

            print("toto je POS PO algoritmu: " + str(pos))
            #upravuju str do outputu, delam z toho 2 cisla vedle sebe
            b = str(pos).replace('[', '')
            a = str(b).replace(']', '')
            c = str(a).replace(',', '')

            print("toto je co ukladam: " + str(c))
            with open("output.txt", "a") as output_file:
                output_file.write(str(c))
                output_file.write('\n')
            

            slice = []
            tmp = []

main()