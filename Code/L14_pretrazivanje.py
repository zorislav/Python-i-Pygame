# 
# L14_pretrazivanje
#

file = open("L14_bad_guys.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)
file.close()

# Linearno pretrazivanje
key = "Morgiana the Shrew"
i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1
if i < len(name_list):
    print( "The name is at position", i)
else:
    print( "The name was not in the list." )
        
