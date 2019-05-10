#
# L17_Iznimke
#

def get_high_score():
    # Postavi varijablu high_score na 0
    high_score = 0
    # Procitaj vrijednost high score iz datoteke
    try:
        high_score_file = open("L17_high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Greska u citanju datoteke, ne postoji datoteka
        print("There is no high score yet.")
    except ValueError:
        # Postoji datoteka, ali ne razumijem procitanu vrijednost
        print("I'm confused. Starting with no high score.")
    # Vrati procitanu vrijednost u glavni program
    return high_score

def save_high_score(new_high_score):
    try:
        # Zapisi vrijednost high scoure u datoteku
        high_score_file = open("L17_high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Ne mogu zapisati
        print("Unable to save the high score.")

# Procitaj spremljeni high score iz datoteke
high_score = get_high_score()
# Postavi current score na 0
current_score = 0
try:
    # Pitaj igraca za njegou current score
    current_score = int(input("What is your score? "))
except ValueError:
    # Greska, ne mogu pretvoriti unesenu vrijednost u broj
    print("I don't understand what you typed.")

# Provjeri da li imamo novi high score
if current_score > high_score:
    # Imamo! Spremi vrijednost u datoteku
    print("Yea! New high score!")
    save_high_score(current_score)
else:
    print("Better luck next time.")


