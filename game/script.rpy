# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image bg maison blanche = "backgrounds/bg_whitehouse.jpg"

# Déclarez les personnages utilisés dans le jeu.
define nouvelle_fille = Character('Elen', color="#e4a6e1")


# Le jeu commence ici
label start:
    show bg maison blanche
    with dissolve

    nouvelle_fille "Vous venez de créer un nouveau jeu Ren'Py."

    nouvelle_fille "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    return
