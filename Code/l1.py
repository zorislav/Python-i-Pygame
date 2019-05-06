#
# l1.py
#
# Izračunaj i ispiši kinetičku energiju objekta koji se giba
print("Ovaj program racuna kinetičku energiju objekta koji se giba.")
m1 = input("Upisi masu objekta u kg: ")
m2 = float(m1) 
v1 = input("Upisi brzinu objekta u m/s: ")
v2 = float(v1) 
e1 = 0.5 * m2 * v2 * v2
e2 = str(e1)
print("Objekt ima kineticku energiju od " + e2 + " Joula.")
