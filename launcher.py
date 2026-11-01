import subprocess
import sys
import tkinter as tk

exercices = [
    ("2.py", "Exercice 2 : premières manipulations de pixels"),
    ("3.py", "Exercice 3 : faire afficher une image"),
    ("4.py", "Exercice 4 : manipulation des pixels"),
    ("5.py", "Exercice 5 : niveaux de gris"),
    ("6.py", "Exercice 6 : filtrage par seuil"),
    ("7.py", "Exercice 7 : noir et blanc"),
    ("8.py", "Exercice 8 : convolution (netteté)"),
    ("9.py", "Exercice 9 : réalisation d'un flou"),
    ("10.py", "Exercice 10 : un plus"),
    ("11.py", "Exercice 11 : détection des contours"),
    ("12.py", "Exercice 12 : transformations géométriques"),
    ("13.py", "Exercice 13 : recréation"),
    ("14.py", "Exercice 14 : image 2D en 3D"),
    ("15.py", "Exercice 15 : éliminer le bruit d'une image"),
]


def lancer(fichier):
    subprocess.Popen([sys.executable, fichier], cwd="src")


fenetre = tk.Tk()
fenetre.title("Projet NSI")

titre = tk.Label(fenetre, text="Exercices", font=("Arial", 16))
titre.pack(pady=10)

for fichier, texte in exercices:
    bouton = tk.Button(fenetre, text=texte, width=45,
                       command=lambda f=fichier: lancer(f))
    bouton.pack(padx=20, pady=3)

quitter = tk.Button(fenetre, text="Quitter", command=fenetre.destroy)
quitter.pack(pady=10)

fenetre.mainloop()