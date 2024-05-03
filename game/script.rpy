# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image bg maison blanche = "backgrounds/bg_whitehouse.jpg"

# Déclarez les personnages utilisés dans le jeu.
define leon = Character("Leon")


# Le jeu commence ici
label start:
    scene bg maison blanche
    with dissolve

    "Vous venez de créer un nouveau jeu Ren'Py."

    "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    return
