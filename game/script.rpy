# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image chambre_jour = "backgrounds/bedroom/Bedroom_Day.png"

image cstl_assise_1 = "characters/christaul/cstl_assise_1.png"

image papa_cstl = "characters/papa_cstl/papa_cstl.png"

image mama_cstl = "characters/mama_cstl/mama_cstl.png"

# Déclarez les personnages utilisés dans le jeu.
define leon = Character("Leon", color="#171ac7")
define christaul = Character("Christaul", color="#ec3e9e")
define pere_de_christaul = Character("Père de Christaul", color="#44ec3e")
define mama_de_christaul = Character("Maman de Christaul", color="#ecda3e")


# Le jeu commence ici
label start:
    

    jump prologue

    

    return
