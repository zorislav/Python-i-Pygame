#
# l3_1.py
#
password = ""
while password != "1234":
    password = input("Uniesite lozinku: ")
    if password == "1234":
        print("Upisali ste ispravnu lozinku.")
    else:
        print("Upisali ste pogresnu lozinku, pokusajte ponovo.")


