#
# l14_binarno_pretrazivanje
#


file = open("L14_bad_guys.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)
file.close()

# Binarno pretrazivanje
key = "Morgiana the Shrew"
donja_granica = 0
gornja_granica = len(name_list)-1
found = False

# Ponavljaj dok ne pronadjes ili dodjes do donje / gornje granice
while donja_granica <= gornja_granica and not found:
 
    # Pronadji sredinu
    middle_pos = (donja_granica + gornja_granica) // 2
 
    # Odluci da li povisujemo donju granicu
    # ili snizujemo gornju granicu
    # ili smo pronasli
    if name_list[middle_pos] < key:
        donja_granica = middle_pos + 1
    elif name_list[middle_pos] > key:
        gornja_granica = middle_pos - 1
    else:
        found = True
 
if found:
    print( "The name is at position", middle_pos)
else:
    print( "The name was not in the list." )
        
