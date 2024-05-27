import numpy as np
import os
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageTk
import tkinter as tk
from tkinter import filedialog


def open_image():
    """
    Ouvre une boîte de dialogue pour choisir un fichier image. Récupère le nom du fichier sélectionné
    et l'affiche dans un champ de texte spécifique de l'interface utilisateur.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Ouvre une boîte de dialogue de sélection de fichier pour les types de fichiers image (*.png, *.jpg, *.jpeg) 
       en utilisant filedialog.askopenfilename.
    2. Récupère le nom du fichier sélectionné sans le chemin complet en utilisant os.path.basename.
    3. Active la modification du champ de texte label_read, insère le nom du fichier, puis désactive à nouveau 
       la modification du champ.

    - Les modules os, tkinter (ou une autre interface graphique), et filedialog doivent être importés.
    - Un champ de texte label_read doit être défini dans l'interface utilisateur.

    - Le champ de texte label_read contiendra le nom du fichier sélectionné et sera en état de lecture seule.
    """
    # Ouvre une boîte de dialogue pour choisir un fichier image
    charger = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    # Récupère le nom du fichier sélectionné
    filename = os.path.basename(charger)
    
    # Autorise la modification du champ de texte et insère le nom du fichier
    label_read.config(state="normal")
    label_read.delete(0, tk.END)
    label_read.insert(0, filename)
    label_read.config(state="readonly")


def open_image2():
    """
    Ouvre une boîte de dialogue pour choisir un deuxième fichier image. Récupère le nom du fichier sélectionné
    et l'affiche dans un champ de texte spécifique de l'interface utilisateur.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Ouvre une boîte de dialogue de sélection de fichier pour les types de fichiers image (*.png, *.jpg, *.jpeg) 
       en utilisant filedialog.askopenfilename.
    2. Récupère le nom du fichier sélectionné sans le chemin complet en utilisant os.path.basename.
    3. Active la modification du champ de texte label_read2, insère le nom du fichier, puis désactive à nouveau 
       la modification du champ.

    - Les modules os, tkinter (ou une autre interface graphique), et filedialog doivent être importés.
    - Un champ de texte label_read2 doit être défini dans l'interface utilisateur.

    - Le champ de texte label_read2 contiendra le nom du fichier sélectionné et sera en état de lecture seule.
    """
    # Ouvre une boîte de dialogue pour choisir un deuxième fichier image
    charger = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    # Récupère le nom du fichier sélectionné
    filename = os.path.basename(charger)
    
    # Autorise la modification du champ de texte et insère le nom du fichier
    label_read2.config(state="normal")
    label_read2.delete(0, tk.END)
    label_read2.insert(0, filename)
    label_read2.config(state="readonly")


def crop(x):
    """
    Extrait la partie du nom d'un fichier avant le premier point ('.') dans une chaîne de caractères donnée.

    Entrées :
    - x (str) : une chaîne de caractères représentant le nom d'un fichier

    Sorties :
    - nom3 (str) : la partie de la chaîne x avant le premier point ('.')

    1. Initialise une chaîne vide nom3.
    2. Parcourt chaque caractère de la chaîne x jusqu'à rencontrer un point ('.').
    3. Si le caractère actuel n'est pas un point, il est ajouté à nom3.
    4. Si un point est rencontré, la fonction retourne immédiatement nom3.
    5. Si aucun point n'est rencontré, la fonction retourne nom3 à la fin de la boucle.

    - x doit être une chaîne de caractères

    - Retourne la partie de x avant le premier point, ou toute la chaîne si aucun point n'est présent.
    """
    nom3 = ""
    for i in x:
        if i != ".":
            nom3 = nom3 + i
        else:
            return nom3
    return nom3


def init():
    """
    Récupère le nom du fichier image à partir du champ de texte, ouvre l'image, redimensionne pour l'affichage
    et crée une nouvelle image vide de même taille que l'image originale. Efface également l'affichage de l'image B.

    Entrées :
    - Aucune

    Sorties :
    - nom (str) : le nom du fichier image
    - img (PIL.Image) : l'objet image PIL ouvert
    - image_tk (ImageTk.PhotoImage) : l'objet image redimensionné pour l'affichage
    - l (int) : la largeur de l'image originale
    - h (int) : la hauteur de l'image originale
    - img2 (PIL.Image) : une nouvelle image vide de même taille que l'image originale

    1. Récupère le nom du fichier image à partir du champ de texte label_read.
    2. Ouvre l'image en utilisant PIL.Image.open et récupère ses dimensions (largeur et hauteur).
    3. Redimensionne l'image pour l'affichage dans l'interface graphique.
    4. Affiche l'image redimensionnée dans le label_image.
    5. Crée une nouvelle image vide de même taille que l'image originale.
    6. Efface l'affichage de l'image B et replace le label.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, et label_imageB doivent être définis dans l'interface utilisateur.

    - Le champ de texte label_read contient le nom du fichier image.
    - Le label_image affiche l'image redimensionnée.
    - Le label_imageB est réinitialisé.
    """
    # Récupère le nom du fichier image à partir du champ de texte
    nom = label_read.get()
    
    # Ouvre l'image et récupère ses dimensions
    img = Image.open(nom)
    l, h = img.size
    
    # Redimensionne l'image pour l'affichage dans l'interface graphique
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Crée une nouvelle image vide de même taille que l'image originale
    img2 = Image.new("RGB",(l,h))
    
    # Efface l'affichage de l'image B et replace le label
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    return nom, img, image_tk, l, h, img2


def copier():
    """
    Copie chaque pixel de l'image originale dans une nouvelle image et affiche cette dernière.
    Crée également un bouton pour sauvegarder l'image copiée.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Parcourt chaque pixel de l'image originale et les copie dans une nouvelle image.
    3. Redimensionne l'image copiée pour l'affichage dans l'interface graphique.
    4. Affiche l'image copiée redimensionnée dans le label_image2.
    5. Crée un bouton "Sauvegarder" pour sauvegarder l'image copiée avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image copiée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image copiée.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image et les copie dans une nouvelle image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            img2.putpixel((x, y), (r, g, b))
    
    # Redimensionne l'image pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("copie de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def gris():
    """
    Convertit chaque pixel de l'image originale en niveaux de gris et affiche l'image résultante.
    Crée également un bouton pour sauvegarder l'image en niveaux de gris.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Parcourt chaque pixel de l'image originale et convertit les couleurs en niveaux de gris.
    3. Redimensionne l'image en niveaux de gris pour l'affichage dans l'interface graphique.
    4. Affiche l'image en niveaux de gris redimensionnée dans le label_image2.
    5. Crée un bouton "Sauvegarder" pour sauvegarder l'image en niveaux de gris avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image en niveaux de gris redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image en niveaux de gris.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image et convertit en niveaux de gris
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            c = int((r + g + b) / 3)
            img2.putpixel((x, y), (c, c, c))
    
    # Redimensionne l'image pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("noir et blanc de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def inverser():
    """
    Inverse les couleurs de chaque pixel de l'image originale et affiche l'image résultante.
    Crée également un bouton pour sauvegarder l'image avec les couleurs inversées.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Parcourt chaque pixel de l'image originale et inverse les couleurs (255 - valeur de chaque composante RGB).
    3. Redimensionne l'image inversée pour l'affichage dans l'interface graphique.
    4. Affiche l'image inversée redimensionnée dans le label_image2.
    5. Crée un bouton "Sauvegarder" pour sauvegarder l'image inversée avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image inversée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image inversée.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image et inverse les couleurs
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            r2 = 255 - r
            g2 = 255 - g
            b2 = 255 - b
            img2.putpixel((x, y), (r2, g2, b2))
    
    # Redimensionne l'image pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("couleurs inversées de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def haut_bas():
    """
    Inverse l'image verticalement et affiche l'image résultante.
    Crée également un bouton pour sauvegarder l'image inversée verticalement.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Parcourt chaque pixel de l'image originale et inverse les positions verticales.
    3. Redimensionne l'image inversée verticalement pour l'affichage dans l'interface graphique.
    4. Affiche l'image inversée verticalement redimensionnée dans le label_image2.
    5. Crée un bouton "Sauvegarder" pour sauvegarder l'image inversée verticalement avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image inversée verticalement redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image inversée verticalement.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # Place le pixel à la position correspondante, mais inversée verticalement
            img2.putpixel((x, h - y - 1), (r, g, b))
    
    # Redimensionne l'image pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("image retournée (haut-bas) de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def gauche_droite():
    """
    Inverse l'image horizontalement et affiche l'image résultante.
    Crée également un bouton pour sauvegarder l'image inversée horizontalement.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Parcourt chaque pixel de l'image originale et inverse les positions horizontales.
    3. Redimensionne l'image inversée horizontalement pour l'affichage dans l'interface graphique.
    4. Affiche l'image inversée horizontalement redimensionnée dans le label_image2.
    5. Crée un bouton "Sauvegarder" pour sauvegarder l'image inversée horizontalement avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image inversée horizontalement redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image inversée horizontalement.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # Place le pixel à la position correspondante, mais inversée horizontalement
            img2.putpixel((l - x - 1, y), (r, g, b))
    
    # Redimensionne l'image pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("image retournée (gauche-droite) de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def rouge():
    """
    Conserve les pixels rouges de l'image originale et convertit les autres pixels en niveaux de gris.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image modifiée.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Parcourt chaque pixel de l'image originale.
    3. Si la composante rouge est dominante, conserve les couleurs originales, sinon convertit en niveaux de gris.
    4. Redimensionne l'image modifiée pour l'affichage dans l'interface graphique.
    5. Affiche l'image modifiée redimensionnée dans le label_image2.
    6. Crée un bouton "Sauvegarder" pour sauvegarder l'image modifiée avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image modifiée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image modifiée.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # Si le rouge est la composante dominante, conserve la couleur rouge, sinon la convertit en niveau de gris
            if r > g and r > b:
                img2.putpixel((x, y), (r, g, b))
            else:
                c = int((r + g + b) / 3)
                img2.putpixel((x, y), (c, c, c))
    
    # Redimensionne l'image pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("le rouge a été gardée dans " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def vert():
    """
    Conserve les pixels verts de l'image originale et convertit les autres pixels en niveaux de gris.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image modifiée.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Parcourt chaque pixel de l'image originale.
    3. Si la composante verte est dominante, conserve les couleurs originales, sinon convertit en niveaux de gris.
    4. Redimensionne l'image modifiée pour l'affichage dans l'interface graphique.
    5. Affiche l'image modifiée redimensionnée dans le label_image2.
    6. Crée un bouton "Sauvegarder" pour sauvegarder l'image modifiée avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image modifiée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image modifiée.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # Si le vert est la composante dominante, conserve la couleur verte, sinon la convertit en niveau de gris
            if g > r and g > b:
                img2.putpixel((x, y), (r, g, b))
            else:
                c = int((r + g + b) / 3)
                img2.putpixel((x, y), (c, c, c))
    
    # Redimensionne l'image pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("le vert a été gardée dans " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def bleu():
    """
    Conserve les pixels bleus de l'image originale et convertit les autres pixels en niveaux de gris.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image modifiée.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Parcourt chaque pixel de l'image originale.
    3. Si la composante bleue est dominante, conserve les couleurs originales, sinon convertit en niveaux de gris.
    4. Redimensionne l'image modifiée pour l'affichage dans l'interface graphique.
    5. Affiche l'image modifiée redimensionnée dans le label_image2.
    6. Crée un bouton "Sauvegarder" pour sauvegarder l'image modifiée avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image modifiée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image modifiée.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # Si le bleu est la composante dominante, conserve la couleur bleue, sinon la convertit en niveau de gris
            if b > r and b > g:
                img2.putpixel((x, y), (r, g, b))
            else:
                c = int((r + g + b) / 3)
                img2.putpixel((x, y), (c, c, c))
    
    # Redimensionne l'image pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("le bleu a été gardée dans " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def diminuer():
    """
    Réduit l'image à la moitié de ses dimensions originales et affiche l'image résultante.
    Crée également un bouton pour sauvegarder l'image réduite.

    Entrées :
    - Aucune

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables et récupère l'image en appelant la fonction init().
    2. Calcule les nouvelles dimensions de l'image réduite de moitié.
    3. Crée une nouvelle image de dimensions réduites.
    4. Parcourt chaque pixel de l'image originale en sautant de deux en deux et copie les valeurs dans l'image réduite.
    5. Redimensionne l'image réduite pour l'affichage dans l'interface graphique.
    6. Affiche l'image réduite redimensionnée dans le label_image2.
    7. Crée un bouton "Sauvegarder" pour sauvegarder l'image réduite avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image réduite redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image réduite.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Calcule les nouvelles dimensions de l'image réduite de moitié
    l2 = int(l / 2)
    h2 = int(h / 2)
    
    # Crée une nouvelle image de dimensions réduites
    img2 = Image.new("RGB", (l2, h2))
    
    # Parcourt chaque pixel de l'image en sautant de deux en deux et copie les valeurs dans l'image réduite
    for x in range(0, l, 2):
        for y in range(0, h, 2):
            r, g, b = img.getpixel((x, y))
            img2.putpixel((int(x / 2) - 1, int(y / 2) - 1), (r, g, b))
    
    # Redimensionne l'image réduite pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l / 2), int(h / (l / (l * 250 / l / 2)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image réduite
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("diminution de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def filtre_rouge(value):
    """
    Applique un filtre rouge à l'image en augmentant l'intensité du rouge.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image filtrée.

    Entrées :
    - value : intensité du filtre rouge (valeur du scale)

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Récupère l'intensité à partir de la valeur du scale.
    2. Récupère le nom du fichier de l'image à partir de l'étiquette de lecture.
    3. Ouvre l'image et obtient ses dimensions.
    4. Redimensionne l'image pour l'affichage dans l'interface graphique.
    5. Convertit l'image en tableau numpy pour une manipulation plus efficace.
    6. Applique le filtre rouge en augmentant l'intensité du rouge.
    7. Convertit le tableau numpy résultant en image PIL.
    8. Redimensionne l'image filtrée pour l'affichage.
    9. Affiche l'image filtrée redimensionnée dans le label_image2.
    10. Crée un bouton "Sauvegarder" pour sauvegarder l'image filtrée avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les modules numpy doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image filtrée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image filtrée.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Obtenir l'intensité à partir de la valeur du scale
    intensite = int(value)
    
    # Obtenir le nom du fichier de l'image à partir de l'étiquette de lecture
    nom = label_read.get()
    
    # Ouvrir l'image
    img = Image.open(nom)
    
    # Obtenir les dimensions de l'image
    l, h = img.size
    
    # Redimensionner l'image pour l'affichage
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Conversion de l'image en tableau numpy pour une manipulation plus efficace
    img_array = np.array(img)
    
    # Appliquer le filtre rouge en augmentant l'intensité du rouge
    img_array[:,:,0] = np.minimum(img_array[:,:,0] + 255 * intensite / 100, 255)
    
    # Assurer que les valeurs restent dans l'intervalle [0, 255]
    img_array[:,:,0] = np.minimum(img_array[:,:,0], 255)
    
    # Convertir le tableau numpy résultant en image PIL
    img_filtree = Image.fromarray(np.uint8(img_array))
    
    # Redimensionner l'image filtrée pour l'affichage
    img2_resized = img_filtree.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Redimensionner l'image filtrée pour la sauvegarde
    img_save = img_filtree.resize((l, h))
    
    # Créer le bouton "Sauvegarder" pour enregistrer l'image filtrée
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img_save.save("filtre rouge sur " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def filtre_vert(value):
    """
    Applique un filtre vert à l'image en augmentant l'intensité du vert.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image filtrée.

    Entrées :
    - value : intensité du filtre vert (valeur du scale)

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Récupère l'intensité à partir de la valeur du scale.
    2. Récupère le nom du fichier de l'image à partir de l'étiquette de lecture.
    3. Ouvre l'image et obtient ses dimensions.
    4. Redimensionne l'image pour l'affichage dans l'interface graphique.
    5. Convertit l'image en tableau numpy pour une manipulation plus efficace.
    6. Applique le filtre vert en augmentant l'intensité du vert.
    7. Convertit le tableau numpy résultant en image PIL.
    8. Redimensionne l'image filtrée pour l'affichage.
    9. Affiche l'image filtrée redimensionnée dans le label_image2.
    10. Crée un bouton "Sauvegarder" pour sauvegarder l'image filtrée avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les modules numpy doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image filtrée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image filtrée.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Obtenir l'intensité à partir de la valeur du scale
    intensite = int(value)
    
    # Obtenir le nom du fichier de l'image à partir de l'étiquette de lecture
    nom = label_read.get()
    
    # Ouvrir l'image
    img = Image.open(nom)
    
    # Obtenir les dimensions de l'image
    l, h = img.size
    
    # Redimensionner l'image pour l'affichage
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Conversion de l'image en tableau numpy pour une manipulation plus efficace
    img_array = np.array(img)
    
    # Appliquer le filtre vert en augmentant l'intensité du canal vert
    img_array[:,:,1] = np.minimum(img_array[:,:,1] + 255 * intensite / 100, 255)
    
    # Assurer que les valeurs restent dans l'intervalle [0, 255]
    img_array[:,:,1] = np.minimum(img_array[:,:,1], 255)
    
    # Convertir le tableau numpy résultant en image PIL
    img_filtree = Image.fromarray(np.uint8(img_array))
    
    # Redimensionner l'image filtrée pour l'affichage
    img2_resized = img_filtree.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Redimensionner l'image filtrée pour la sauvegarde
    img_save = img_filtree.resize((l, h))
    
    # Créer le bouton "Sauvegarder" pour enregistrer l'image filtrée
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img_save.save("filtre vert sur " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def filtre_bleu(value):
    """
    Applique un filtre bleu à l'image en augmentant l'intensité du bleu.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image filtrée.

    Entrées :
    - value : intensité du filtre bleu (valeur du scale)

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Récupère l'intensité à partir de la valeur du scale.
    2. Récupère le nom du fichier de l'image à partir de l'étiquette de lecture.
    3. Ouvre l'image et obtient ses dimensions.
    4. Redimensionne l'image pour l'affichage dans l'interface graphique.
    5. Convertit l'image en tableau numpy pour une manipulation plus efficace.
    6. Applique le filtre bleu en augmentant l'intensité du bleu.
    7. Convertit le tableau numpy résultant en image PIL.
    8. Redimensionne l'image filtrée pour l'affichage.
    9. Affiche l'image filtrée redimensionnée dans le label_image2.
    10. Crée un bouton "Sauvegarder" pour sauvegarder l'image filtrée avec un nouveau nom.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les modules numpy doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image filtrée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image filtrée.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Obtenir l'intensité à partir de la valeur du scale
    intensite = int(value)
    
    # Obtenir le nom du fichier de l'image à partir de l'étiquette de lecture
    nom = label_read.get()
    
    # Ouvrir l'image
    img = Image.open(nom)
    
    # Obtenir les dimensions de l'image
    l, h = img.size
    
    # Redimensionner l'image pour l'affichage
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Conversion de l'image en tableau numpy pour une manipulation plus efficace
    img_array = np.array(img)
    
    # Appliquer le filtre bleu en augmentant l'intensité du bleu
    img_array[:,:,2] = np.minimum(img_array[:,:,2] + 255 * intensite / 100, 255)
    
    # Assurer que les valeurs restent dans l'intervalle [0, 255]
    img_array[:,:,2] = np.minimum(img_array[:,:,2], 255)
    
    # Convertir le tableau numpy résultant en image PIL
    img_filtree = Image.fromarray(np.uint8(img_array))
    
    # Redimensionner l'image filtrée pour l'affichage
    img2_resized = img_filtree.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Redimensionner l'image filtrée pour la sauvegarde
    img_save = img_filtree.resize((l, h))
    
    # Créer le bouton "Sauvegarder" pour enregistrer l'image filtrée
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img_save.save("filtre bleu sur " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def clair(value):
    """
    Applique un filtre d'éclaircissement à l'image en augmentant l'intensité des couleurs.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image éclaircie.

    Entrées :
    - value : intensité du filtre d'éclaircissement (valeur du scale)

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Récupère l'intensité à partir de la valeur du scale.
    2. Récupère le nom du fichier de l'image à partir de l'étiquette de lecture.
    3. Ouvre l'image et obtient ses dimensions.
    4. Convertit l'image en tableau numpy pour une manipulation plus efficace.
    5. Calcule les valeurs de luminosité à ajouter à chaque couleur.
    6. Applique l'éclaircissement à l'image en ajoutant les valeurs de luminosité aux pixels.
    7. Assure que les valeurs restent dans l'intervalle [0, 255].
    8. Convertit le tableau numpy résultant en image PIL.
    9. Redimensionne l'image d'origine pour l'affichage dans l'interface graphique.
    10. Affiche l'image d'origine redimensionnée dans le label_image.
    11. Redimensionne l'image éclaircie pour l'affichage.
    12. Affiche l'image éclaircie redimensionnée dans le label_image2.
    13. Redimensionne l'image éclaircie pour la sauvegarde.
    14. Crée un bouton "Sauvegarder" pour enregistrer l'image éclaircie.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les modules numpy doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image éclaircie redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image éclaircie.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Obtenir l'intensité à partir de la valeur du scale
    intensite = int(value)
    
    # Obtenir le nom du fichier de l'image à partir de l'étiquette de lecture
    nom = label_read.get()
    
    # Ouvrir l'image
    img = Image.open(nom)
    
    # Obtenir les dimensions de l'image
    l, h = img.size
    
    # Conversion de l'image en tableau numpy pour une manipulation plus efficace
    img_array = np.array(img)
    
    # Calcul des valeurs de luminosité à appliquer à chaque couleur
    bright_values = np.array([intensite, intensite, intensite]) * 255 / 100
    
    # Appliquer l'éclaircissement à l'image en ajoutant les valeurs de luminosité aux pixels
    img_eclairee_array = img_array + bright_values
    
    # Assurer que les valeurs restent dans l'intervalle [0, 255]
    img_eclairee_array = np.minimum(img_eclairee_array, 255)
    
    # Convertir le tableau numpy résultant en image PIL
    img_eclairee = Image.fromarray(np.uint8(img_eclairee_array))
    
    # Redimensionner l'image d'origine pour l'affichage
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Redimensionner l'image éclaircie pour l'affichage
    img2_resized = img_eclairee.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Redimensionner l'image éclaircie pour la sauvegarde
    img_save = img_eclairee.resize((l, h))
    
    # Créer le bouton "Sauvegarder" pour enregistrer l'image éclaircie
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img_save.save("eclaircicement de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def sombre(value):
    """
    Applique un filtre d'assombrissement à l'image en réduisant l'intensité des couleurs.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image assombrie.

    Entrées :
    - value : intensité du filtre d'assombrissement (valeur du scale)

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Récupère l'intensité à partir de la valeur du scale.
    2. Récupère le nom du fichier de l'image à partir de l'étiquette de lecture.
    3. Ouvre l'image et obtient ses dimensions.
    4. Convertit l'image en tableau numpy pour une manipulation plus efficace.
    5. Calcule les valeurs sombres à appliquer à chaque couleur.
    6. Applique l'assombrissement à l'image en soustrayant les valeurs sombres des pixels.
    7. Assure que les valeurs restent dans l'intervalle [0, 255].
    8. Convertit le tableau numpy résultant en image PIL.
    9. Redimensionne l'image assombrie pour l'affichage dans l'interface graphique.
    10. Affiche l'image assombrie redimensionnée dans le label_image2.
    11. Redimensionne l'image assombrie pour la sauvegarde.
    12. Crée un bouton "Sauvegarder" pour enregistrer l'image assombrie.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les modules numpy doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image assombrie redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image assombrie.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Obtenir l'intensité à partir de l'échelle de sombre
    intensite = int(value)
    
    # Obtenir le nom du fichier de l'image à partir de l'étiquette de lecture
    nom = label_read.get()
    
    # Ouvrir l'image
    img = Image.open(nom)
    
    # Obtenir les dimensions de l'image
    l, h = img.size
    
    # Redimensionner l'image pour affichage
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    
    # Convertir l'image redimensionnée en ImageTk pour l'affichage
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Conversion de l'image en tableau numpy pour une manipulation plus efficace
    img_array = np.array(img)
    
    # Calcul des valeurs sombres à appliquer à chaque couleur
    dark_values = np.array([intensite, intensite, intensite]) * 255 / 100
    
    # Appliquer l'assombrissement à l'image en soustrayant les valeurs sombres des pixels
    img2_array = img_array - dark_values
    
    # Assurer que les valeurs restent dans l'intervalle [0, 255]
    img2_array = np.maximum(img2_array, 0)
    
    # Convertir le tableau numpy résultant en image PIL
    img2 = Image.fromarray(np.uint8(img2_array))
    
    # Redimensionner l'image assombrie pour affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    
    # Mettre à jour l'image dans l'interface graphique
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Redimensionner l'image assombrie pour la sauvegarde
    img_save = img2.resize((l,h))
    
    # Créer le bouton "Sauvegarder" pour enregistrer l'image assombrie
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img_save.save("assombrissement de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def pixel(value):
    """
    Applique un effet de pixelisation à l'image en remplaçant les blocs de pixels par des pixels uniques.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image pixelisée.

    Entrées :
    - value : intensité de la pixelisation (valeur du scale)

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Récupère l'intensité à partir de la valeur du scale.
    2. Récupère le nom du fichier de l'image à partir de l'étiquette de lecture.
    3. Ouvre l'image et obtient ses dimensions.
    4. Convertit l'image en tableau numpy pour une manipulation plus efficace.
    5. Applique la pixelisation en remplaçant les blocs de pixels par des pixels uniques.
    6. Convertit le tableau numpy résultant en image PIL.
    7. Redimensionne l'image pixelisée pour l'affichage dans l'interface graphique.
    8. Affiche l'image pixelisée redimensionnée dans le label_image2.
    9. Redimensionne l'image pixelisée pour la sauvegarde.
    10. Crée un bouton "Sauvegarder" pour enregistrer l'image pixelisée.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les modules numpy doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB, et label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image pixelisée redimensionnée.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image pixelisée.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Obtenir l'intensité à partir de l'échelle de sombre
    intensite = int(value)
    
    # Obtenir le nom du fichier de l'image à partir de l'étiquette de lecture
    nom = label_read.get()
    
    # Ouvrir l'image
    img = Image.open(nom)
    
    # Obtenir les dimensions de l'image
    l, h = img.size
    
    # Redimensionner l'image pour affichage
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    
    # Convertir l'image redimensionnée en ImageTk pour l'affichage
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Conversion de l'image en tableau numpy pour une manipulation plus efficace
    img_array = np.array(img)
    img2_array = np.zeros_like(img_array)
    
    # Pixelisation de l'image en remplaçant les blocs par des pixels uniques
    for x in range(0, img_array.shape[0], intensite):
        for y in range(0, img_array.shape[1], intensite):
            img2_array[x:x+intensite, y:y+intensite] = img_array[x, y]
            
    # Conversion du tableau numpy résultant en image PIL
    img2 = Image.fromarray(img2_array)

    # Redimensionner l'image pixelisée pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Redimensionner l'image pour la sauvegarde
    img2_resized = img2.resize((l,h))

    # Créer le bouton "Sauvegarder" pour enregistrer l'image pixelisée
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2_resized.save("pixelisation de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def vive():
    """
    Applique un effet "vive" à l'image en augmentant l'intensité des couleurs dominantes.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image résultante.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image avec l'effet "vive".
    - Un bouton "Sauvegarder" permet de sauvegarder l'image résultante.
    """
    # Initialise les variables et récupère l'image
    nom, img, image_tk, l, h, img2 = init()
    
    # Parcourt chaque pixel de l'image et ajuste les valeurs pour rendre l'image "vive"
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # Si le canal rouge est le plus grand, intensifie la couleur rouge et supprime les autres canaux
            if r > b and r > g:
                r = 255
                g = 0
                b = 0
            
            # Si le canal vert est le plus grand, intensifie la couleur verte et supprime les autres canaux
            if g > r and g > b:
                g = 255
                r = 0
                b = 0
            
            # Si le canal bleu est le plus grand, intensifie la couleur bleue et supprime les autres canaux
            if b > r and b > g:
                b = 255
                r = 0
                g = 0
            
            # Place les valeurs ajustées dans l'image résultante
            img2.putpixel((x, y), (r, g, b))
    
    # Redimensionne l'image résultante pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image résultante
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("vive de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def melange():
    """
    Mélange deux images en plaçant alternativement les pixels de chacune dans une nouvelle image.
    Affiche l'image résultante. Crée également un bouton pour sauvegarder l'image résultante.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_read2, label_image, label_imageB, label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image résultante du mélange.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image résultante.
    """
    # Initialise les variables et récupère les images
    nom, img, image_tk, l, h, img2 = init()
    nom2 = label_read2.get()
    img2 = Image.open(nom2)
    l2, h2 = img2.size
    
    # Détermine les dimensions de l'image résultante en fonction des dimensions des deux images d'entrée
    L = min(l, l2)
    H = min(h, h2)
    
    # Crée une nouvelle image résultante
    img3 = Image.new("RGB", (L, H))
    
    # Affiche la deuxième image dans une zone dédiée de l'interface graphique
    label_imageB.place(x=700, y=int(h / (l / (l * 250 / l)) + 60))
    img2_resized = img2.resize((int(l2 * 250 / l2), int(h2 / (l2 / (l2 * 250 / l2)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_imageB.config(image=image_tk)
    label_imageB.image = image_tk
    
    # Parcourt chaque pixel des deux images et les place alternativement dans l'image résultante
    for x in range(0, L, 2):
        for y in range(0, H, 2):
            r, g, b = img.getpixel((x, y))
            img3.putpixel((x, y), (r, g, b))
    
    for x in range(1, L, 2):
        for y in range(1, H, 2):
            r, g, b = img2.getpixel((x, y))
            img3.putpixel((x, y), (r, g, b))
    
    # Redimensionne l'image résultante pour l'affichage
    img3_resized = img3.resize((int(L * 250 / L), int(H / (L / (L * 250 / L)))))
    image_tk = ImageTk.PhotoImage(img3_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image résultante
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img3.save("melange de " + crop(nom) + " et " + nom2), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def agrandir():
    """
    Agrandit l'image en doublant la taille de chaque pixel.
    Affiche l'image agrandie. Crée également un bouton pour sauvegarder l'image agrandie.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_image2 doivent être définis dans l'interface utilisateur.

    - Le label_image2 affiche l'image agrandie.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image agrandie.
    """
    # Initialise les variables et récupère l'image d'origine
    nom, img, image_tk, l, h, img2 = init()
    
    # Calcule les nouvelles dimensions de l'image agrandie
    l2 = int(l * 2)
    h2 = int(h * 2)
    
    # Crée une nouvelle image agrandie avec les nouvelles dimensions
    img2 = Image.new("RGB", (l2, h2))
    
    # Parcourt chaque pixel de l'image d'origine et les place dans la nouvelle image agrandie
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            # Place le pixel d'origine et ses copies dans la nouvelle image agrandie
            img2.putpixel((int(x * 2) - 1, int(y * 2) - 1), (r, g, b))
            img2.putpixel((int(x * 2) - 1 + 1, int(y * 2) - 1), (r, g, b))
            img2.putpixel((int(x * 2) - 1, int(y * 2) - 1 + 1), (r, g, b))
            img2.putpixel((int(x * 2) - 1 + 1, int(y * 2) - 1 + 1), (r, g, b))
    
    # Redimensionne l'image agrandie pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l * 2), int(h / (l / (l * 250 / l * 2)))))
    
    # Met à jour l'image affichée dans l'interface graphique
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image agrandie
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("agrandissement de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def contraste(value):
    """
    Applique un filtre de contraste à l'image.
    Affiche l'image résultante avec le contraste ajusté.
    Crée également un bouton pour sauvegarder l'image résultante.

    Entrées :
    - value : intensité du filtre de contraste (valeur du scale)

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables nom, img, image_tk, l, h et img2 avec la fonction init().
    2. Récupère l'intensité du filtre de contraste à partir de la valeur du scale.
    3. Applique le filtre de contraste à l'image.
    4. Redimensionne l'image résultante pour l'affichage dans l'interface graphique.
    5. Affiche l'image résultante redimensionnée dans le label_image2.
    6. Crée un bouton "Sauvegarder" pour enregistrer l'image résultante.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB et label_image2 doivent être définis dans l'interface utilisateur.
    - La fonction init() doit être définie et renvoyer les variables nom, img, image_tk, l, h et img2.

    - Le label_image2 affiche l'image résultante avec le contraste ajusté.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image résultante avec le contraste ajusté.
    """
    nom, img, image_tk, l, h, img2 = init()
    intensite = scale_contraste.get()
    contrast = ImageEnhance.Contrast(img)
    img2 = contrast.enhance(intensite)
    
    # Redimensionne l'image résultante pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image résultante
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("contraste de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def flou(value):
    """
    Applique un effet de flou à l'image.
    Affiche l'image résultante avec l'effet de flou.
    Crée également un bouton pour sauvegarder l'image résultante.

    Entrées :
    - value : intensité de l'effet de flou (valeur du scale)

    Sorties :
    - Aucune (mais modifie l'état de l'interface utilisateur)

    1. Initialise les variables nom, img, image_tk, l, h et img2 avec la fonction init().
    2. Récupère l'intensité de l'effet de flou à partir de la valeur du scale.
    3. Applique l'effet de flou à l'image.
    4. Redimensionne l'image résultante pour l'affichage dans l'interface graphique.
    5. Affiche l'image résultante redimensionnée dans le label_image2.
    6. Crée un bouton "Sauvegarder" pour enregistrer l'image résultante.

    - Les modules os, tkinter, filedialog et PIL doivent être importés.
    - Les champs de texte et labels label_read, label_image, label_imageB et label_image2 doivent être définis dans l'interface utilisateur.
    - La fonction init() doit être définie et renvoyer les variables nom, img, image_tk, l, h et img2.

    - Le label_image2 affiche l'image résultante avec l'effet de flou.
    - Un bouton "Sauvegarder" permet de sauvegarder l'image résultante avec l'effet de flou.
    """
    nom, img, image_tk, l, h, img2 = init()
    intensite = scale_flou.get()
    img2 = img.filter(ImageFilter.GaussianBlur(radius=intensite))
    
    # Redimensionne l'image résultante pour l'affichage
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Crée le bouton "Sauvegarder" pour sauvegarder l'image résultante
    button_save = tk.Button(fenetre, text="Sauvegarder", command=lambda: img2.save("flou de " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Retouche Photo")
fenetre.geometry("1400x800")
fenetre.config(bg="white")

# Création des label de texte
label_nom = tk.Label(fenetre, text="Chargez l'image que vous souhaiter modifier", bg="white")
label_nom.place(x=50, y=50)
label_nom2 = tk.Label(fenetre, text="Chargez la deuxième image", bg="white")
label_nom2.place(x=135, y=510)
label_couleur = tk.Label(fenetre, text="Choisissez la couleur :", bg="white")
label_couleur.place(x=250, y=265)
label_sens = tk.Label(fenetre, text="Choisissez le sens :", bg="white")
label_sens.place(x=145, y=230)

# Création des entry inchengeables
label_read = tk.Entry(fenetre, readonlybackground="grey", relief="flat", foreground="white")
label_read.config(state="readonly")
label_read.place(x=50, y=75)
label_read2 = tk.Entry(fenetre, readonlybackground="grey", relief="flat", foreground="white")
label_read2.config(state="readonly")
label_read2.place(x=415, y=510)

# Création des boutons pour toutes les fonctions
button = tk.Button(fenetre, text="Ouvrir une image", command=open_image)
button.place(x=300, y=50)
button = tk.Button(fenetre, text="Ouvrir une image", command=open_image2)
button.place(x=305, y=510)
button_copier = tk.Button(fenetre, text="Copier", command=copier, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_copier.place(x=50, y=125)
button_gris = tk.Button(fenetre, text="Mettre en noir et blanc", command=gris, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_gris.place(x=50, y=160)
button_inverser = tk.Button(fenetre, text="Inverser les couleurs", command=inverser, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_inverser.place(x=50, y=195)
button_retourner = tk.Button(fenetre, text="Retourner", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_retourner.place(x=50, y=230)
button_valoriser = tk.Button(fenetre, text="Valoriser une couleur", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_valoriser.place(x=50, y=265)
button_diminuer = tk.Button(fenetre, text="Diminuer la taile", command=diminuer, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_diminuer.place(x=50, y=300)
button_filtre = tk.Button(fenetre, text="Filtre de couleur", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_filtre.place(x=50, y=335)
button_clair = tk.Button(fenetre, text="Eclaircir", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_clair.place(x=50, y=370)
button_sombre = tk.Button(fenetre, text="Assombrir", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_sombre.place(x=50, y=405)
button_pixel = tk.Button(fenetre, text="Pixéliser", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_pixel.place(x=50, y=440)
button_vive = tk.Button(fenetre, text="RVB", command=vive, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_vive.place(x=50, y=475)
button_melange = tk.Button(fenetre, text="Mélanger", command=melange, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_melange.place(x=50, y=510)
button_agrandir = tk.Button(fenetre, text="Agrandir", command=agrandir, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_agrandir.place(x=50, y=545)
button_contraste = tk.Button(fenetre, text="Contraste", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_contraste.place(x=50, y=580)
button_flou = tk.Button(fenetre, text="Flou", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_flou.place(x=50, y=615)
button_rouge = tk.Button(fenetre, text="Rouge", command=rouge)
button_rouge.place(x=400, y=265)
button_vert = tk.Button(fenetre, text="Vert", command=vert)
button_vert.place(x=455, y=265)
button_bleu = tk.Button(fenetre, text="Bleu", command=bleu)
button_bleu.place(x=500, y=265)
button_hb = tk.Button(fenetre, text="Haut/Bas", command=haut_bas)
button_hb.place(x=270, y=230)
button_gd = tk.Button(fenetre, text="Gauche/Droite", command=gauche_droite)
button_gd.place(x=345, y=230)

# Création des labels image pour l'affichage des images
label_image = tk.Label(fenetre, bg="white")
label_image.place(x=700, y=50)
label_image2 = tk.Label(fenetre, bg="white")
label_image2.place(x=975, y=50)
label_imageB = tk.Label(fenetre, bg="white")
label_imageB.place(x=0, y=0)

# Création des echelles utiles aux fonctions
scale_filtreR = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", label="Rouge", command=lambda value: filtre_rouge(value), showvalue=False, font=("Helvetica", 8))
scale_filtreR.place(x=185, y=335)
scale_filtreV = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", label="Vert", command=lambda value: filtre_vert(value), showvalue=False, font=("Helvetica", 8))
scale_filtreV.place(x=305, y=335)
scale_filtreB = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", label="Bleu", command=lambda value: filtre_bleu(value), showvalue=False, font=("Helvetica", 8))
scale_filtreB.place(x=425, y=335)
scale_clair = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", command=lambda value: clair(value), showvalue=False)
scale_clair.place(x=130, y=375)
scale_sombre = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", command=lambda value: sombre(value), showvalue=False)
scale_sombre.place(x=145, y=410)
scale_pixel = tk.Scale(fenetre, from_=1, to=100, orient=tk.HORIZONTAL, bg="white", command=lambda value: pixel(value), showvalue=False)
scale_pixel.place(x=135, y=445)
scale_contraste = tk.Scale(fenetre, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL, bg="white", command=lambda value: contraste(value), showvalue=False)
scale_contraste.place(x=140, y=580)
scale_contraste.set(1)
scale_flou = tk.Scale(fenetre, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL, bg="white", command=lambda value: flou(value), showvalue=False)
scale_flou.place(x=140, y=615)

# Garder la fenêtre ouverte
fenetre.mainloop()