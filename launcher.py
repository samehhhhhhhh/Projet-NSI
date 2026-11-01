import subprocess
import sys
import tkinter as tk

exercices = [
    ("2.py", "Exercice 2 : premières manipulations de pixels"),
    ("3.py", "Exercice 3 : faire afficher une image"),
    ("4.py", "Exercice 4 : manipulation des pixels"),
    ("6.py", "Exercice 6 : filtrage par seuil"),
    ("8.py", "Exercice 8 : convolution (netteté)"),
    ("10.py", "Exercice 10 : un plus"),
    ("12.py", "Exercice 12 : transformations géométriques"),
    ("14.py", "Exercice 14 : image 2D en 3D"),
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