#
# L16_Sortiranje_umetanjem
#

def insertion_sort(my_list):
    # Funkcija za sortiranje liste korištenjem sortiranja umetanjem
 
    # Kreni od drugog elementa niza (pos 1)
    # i umetni ga u listu
    for key_pos in range(1, len(my_list)):
 
        # Procitaj vrijednost trenutnog elementa
        key_value = my_list[key_pos]
 
        # Kreni od trenutnog elementa u lijevo prema pocetku liste
        scan_pos = key_pos - 1
 
        # Provjeravaj svaki elemente dok ne stignes do pocetka liste
        # ili ne nadjes manji element
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            # Postavi trenutni element ispred tekuceg u petlji
            my_list[scan_pos + 1] = my_list[scan_pos]
            # pomakni se za jedno mjesto u lijevo
            scan_pos = scan_pos - 1
 
        # Postavi trenutnu vrijednost na pravu lokaciju
        my_list[scan_pos + 1] = key_value

    # Vrati sortirani niz
    return(my_list)
 
# Definiraj listu
pocetna_lista = [15, 57, 14, 22, 72, 79, 26, 56, 42, 40]

# Ispisi pocetnu listu
print(pocetna_lista)

# Sortiraj pocetnu listu
sortirana_lista = insertion_sort(pocetna_lista)

# Ispisi sortiranu listu
print(sortirana_lista)
