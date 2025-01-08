import random

punteggio_utente = 0
punteggio_computer = 0

def gioca():
    global punteggio_utente, punteggio_computer
    utente = input("Scegli 'sasso' (s), 'carta' (c) o 'forbice' (f): ").lower()
    computer = random.choice(['s', 'c', 'f'])

    if utente == computer:
        return "Pareggio!"

    if hai_vinto(utente, computer):
        punteggio_utente += 1
        return f"Hai vinto! Punteggio: Tu {punteggio_utente} - Computer {punteggio_computer}"
    
    punteggio_computer += 1
    return f"Hai perso! Punteggio: Tu {punteggio_utente} - Computer {punteggio_computer}"

def hai_vinto(giocatore, computer):
    # s > f, c > s, f > c
    if (giocatore == 's' and computer == 'f') or \
       (giocatore == 'c' and computer == 's') or \
       (giocatore == 'f' and computer == 'c'):
        return True
    return False

while True:
    print(gioca())
    if input("Vuoi giocare ancora? (s/n): ").lower() != 's':
        break

print(f"Punteggio finale: Tu {punteggio_utente} - Computer {punteggio_computer}")
print("Grazie per aver giocato!")


