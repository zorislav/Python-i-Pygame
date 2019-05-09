#
# L16_Selekcijsko_sortiranje
#

def selection_sort(my_list):
    # Funkcija za sortiranje liste korištenjem selekcijskog sortiranja
 
    # Petlja koja prolazi kroz cijelu listu
    for cur_pos in range(len(my_list)):
        # Trazi najmanji broj, pocni od trenutne pozicije 
        min_pos = cur_pos
 
        # Provjeri od trenutne pozicije u desno do kraja liste
        for scan_pos in range(cur_pos + 1, len(my_list)):
 
            # Da li je trenutna pozicija najmanja?
            if my_list[scan_pos] < my_list[min_pos]:
 
                # Ako da, zapamnti je 
                min_pos = scan_pos
 
        # Zamijeni trenutnu poziciju i najmanju poziciju
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

    # Vrati sortirani niz
    return(my_list)
 
# Definiraj listu
pocetna_lista = [15, 57, 14, 22, 72, 79, 26, 56, 42, 40]

# Ispisi pocetnu listu
print(pocetna_lista)

# Sortiraj pocetnu listu
sortirana_lista = selection_sort(pocetna_lista)

# Ispisi sortiranu listu
print(sortirana_lista)
